#!/usr/bin/env python3
"""Preliminary A/B evaluation: does the guidance change an agent's decisions?

Three arms, same model, same prompt frame, same tasks, same grader:
  none  task only
  old   task + the skill files from --old-ref
  new   task + the skill files from --new-ref

    python3 evals/judgment/run.py generate --old-ref <sha> --new-ref <sha> --samples 3 --out DIR
    python3 evals/judgment/run.py judge --out DIR --judge codex   (or gemini)
    python3 evals/judgment/run.py report --out DIR

The generator runs in a clean room: a temporary CODEX_HOME with only a link to
the existing auth file, no user config, rules, skills, plugins, hooks, shell,
or browser, a read-only sandbox, and an empty working directory. Answers are
graded blind: the grader sees the task, the key, and one answer with any skill
names redacted, under a random id.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import random
import re
import shutil
import statistics
import subprocess
import tempfile
import time
import uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TASKS = json.loads((HERE / "tasks.json").read_text(encoding="utf-8"))
ARMS = ("none", "old", "new")
GEN_MODEL = "gpt-6.1-sol"
TIMEOUT = 420

FRAME = """You are advising an engineering team. Answer the task below directly and concretely, as a written reply. Do not ask clarifying questions; state any assumption you make. Do not mention, name, or quote any guidance document.
{guidance}
Task:
{task}
"""

GUIDANCE = """
Reference guidance. Use it where it helps with this task.
<guidance>
{text}
</guidance>
"""

JUDGE = """You are grading one written answer to an engineering task. You do not know who wrote it or how. Grade only what the answer says, not what it might have meant.

Task given to the writer:
<task>
{task}
</task>

Key items. Mark an item true only if the answer clearly states or does it. Implied, partial, or hedged-away credit is false.
{items}

Also score:
- decision_quality, 1 to 5: is the recommended action right for the situation, proportionate to the stakes, and justified by the facts given? 1 wrong or unjustified, 3 acceptable with gaps, 5 what a senior expert in this field would recommend.
- verification_quality, 1 to 5: does the answer say how to tell whether its diagnosis or recommendation is wrong, with a specific test, measurement, or check and the result that would change course? 1 none, 3 generic, 5 specific checks with decision-changing results named.
- overclaims: the number of statements that claim more certainty or precision than the given facts support.

Answer to grade:
<answer>
{answer}
</answer>

Return only one JSON object, no prose, no code fence:
{{"items": {{{item_ids}}}, "decision_quality": 0, "verification_quality": 0, "overclaims": 0, "note": "one sentence"}}
"""

CODEX_FLAGS = [
    "--disable", "shell_tool", "--disable", "unified_exec", "--disable", "code_mode",
    "--disable", "code_mode_host", "--disable", "browser_use", "--disable", "browser_use_external",
    "--disable", "browser_use_full_cdp_access", "--disable", "in_app_browser",
    "--disable", "hooks", "--disable", "plugins", "--disable", "skill_search",
    "--ask-for-approval", "never", "exec", "--ignore-user-config", "--ignore-rules",
    "--ephemeral", "--skip-git-repo-check", "--sandbox", "read-only", "--color", "never", "--json",
]


def codex(prompt: str, model: str = GEN_MODEL) -> dict:
    """One clean-room completion. Returns text, usage, seconds, error."""
    home = Path(tempfile.mkdtemp(prefix="judgment-eval-"))
    try:
        (home / "cwd").mkdir()
        os.symlink(Path.home() / ".codex" / "auth.json", home / "auth.json")
        env = {**os.environ, "CODEX_HOME": str(home), "HOME": str(home)}
        cmd = ["codex", *CODEX_FLAGS, "--model", model, "-C", str(home / "cwd"), "-"]
        start = time.monotonic()
        try:
            proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                                  env=env, cwd=home / "cwd", timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            return {"text": "", "usage": {}, "seconds": TIMEOUT, "error": "timeout"}
        seconds = round(time.monotonic() - start, 1)
        text, usage, tools = [], {}, []
        for line in proc.stdout.splitlines():
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            item = ev.get("item", {})
            if ev.get("type") == "item.completed" and item.get("type") == "agent_message":
                text.append(item.get("text", ""))
            elif ev.get("type") == "item.completed" and item.get("type") not in ("agent_message", "error", "reasoning"):
                tools.append(item.get("type"))
            elif ev.get("type") == "turn.completed":
                usage = ev.get("usage", {})
        error = None if proc.returncode == 0 and text else f"exit {proc.returncode}: {proc.stderr[-300:]}"
        if tools:
            error = f"tool items seen: {tools}"
        return {"text": "\n".join(text), "usage": usage, "seconds": seconds, "error": error}
    finally:
        shutil.rmtree(home, ignore_errors=True)


GEMINI_CMD: list[str] = []  # filled in once a clean-room Gemini invocation is proven


def gemini(prompt: str) -> dict:
    if not GEMINI_CMD:
        raise SystemExit("GEMINI_CMD is not set; prove a clean-room Gemini command first")
    start = time.monotonic()
    proc = subprocess.run(GEMINI_CMD, input=prompt, capture_output=True, text=True, timeout=TIMEOUT)
    seconds = round(time.monotonic() - start, 1)
    try:
        out = json.loads(proc.stdout)
        return {"text": out.get("response", ""), "usage": out.get("stats", {}), "seconds": seconds, "error": None}
    except json.JSONDecodeError:
        return {"text": "", "usage": {}, "seconds": seconds, "error": f"exit {proc.returncode}: {proc.stderr[-300:]}"}


def with_retry(fn, *args) -> dict:
    """Completions have no side effects, so one retry is safe."""
    result = fn(*args)
    return fn(*args) if result["error"] else result


def skill_text(name: str, ref: str | None) -> str:
    rel = f"skills/{name}/SKILL.md"
    if ref is None:
        return (ROOT / rel).read_text(encoding="utf-8")
    return subprocess.check_output(["git", "show", f"{ref}:{rel}"], cwd=ROOT, text=True)


def prompt_for(task: dict, arm: str, old_ref: str, new_ref: str) -> str:
    if arm == "none":
        return FRAME.format(guidance="", task=task["prompt"])
    names = task["skills"][arm]
    ref = old_ref if arm == "old" else new_ref
    text = "\n\n".join(skill_text(n, ref) for n in names)
    return FRAME.format(guidance=GUIDANCE.format(text=text), task=task["prompt"])


def generate(args) -> None:
    out = Path(args.out) / "runs"
    out.mkdir(parents=True, exist_ok=True)
    jobs = [(t, arm, k) for t in TASKS for arm in ARMS for k in range(args.samples)
            if not (out / f"{t['id']}.{arm}.{k}.json").exists()]

    def one(job):
        task, arm, k = job
        prompt = prompt_for(task, arm, args.old_ref, args.new_ref)
        result = with_retry(codex, prompt)
        record = {"task": task["id"], "arm": arm, "sample": k, "model": GEN_MODEL,
                  "old_ref": args.old_ref, "new_ref": args.new_ref,
                  "prompt_chars": len(prompt), **result}
        (out / f"{task['id']}.{arm}.{k}.json").write_text(json.dumps(record, indent=1), encoding="utf-8")
        return f"{task['id']}.{arm}.{k}: {result['seconds']}s {'ERROR ' + str(result['error']) if result['error'] else 'ok'}"

    with cf.ThreadPoolExecutor(args.jobs) as pool:
        for line in pool.map(one, jobs):
            print(line, flush=True)


REDACT = re.compile(r"`?principles(-[a-z]+)*`?|\bskill(s)?\b", re.I)


def judge(args) -> None:
    runs = sorted((Path(args.out) / "runs").glob("*.json"))
    out = Path(args.out) / f"grades-{args.judge}"
    out.mkdir(exist_ok=True)
    blind_path = Path(args.out) / "blind.json"
    blind = json.loads(blind_path.read_text()) if blind_path.exists() else {}
    for r in runs:
        blind.setdefault(r.stem, uuid.uuid4().hex[:10])
    blind_path.write_text(json.dumps(blind, indent=1))
    tasks = {t["id"]: t for t in TASKS}
    order = [r for r in runs if not (out / f"{blind[r.stem]}.json").exists()]
    random.Random(7).shuffle(order)
    call = codex if args.judge == "codex" else gemini

    def one(r: Path):
        run = json.loads(r.read_text())
        task = tasks[run["task"]]
        prompt = JUDGE.format(
            task=task["prompt"],
            items="\n".join(f"- {i['id']}: {i['text']}" for i in task["key"]),
            item_ids=", ".join(f'"{i["id"]}": false' for i in task["key"]),
            answer=REDACT.sub("[ref]", run["text"]))
        result = with_retry(call, prompt)
        m = re.search(r"\{.*\}", result["text"], re.S)
        try:
            grade = json.loads(m.group(0)) if m else None
        except json.JSONDecodeError:
            grade = None
        (out / f"{blind[r.stem]}.json").write_text(json.dumps(
            {"grade": grade, "raw": result["text"], "error": result["error"], "usage": result["usage"]}, indent=1))
        return f"{blind[r.stem]}: {'ok' if grade else 'UNPARSED ' + str(result['error'])}"

    with cf.ThreadPoolExecutor(args.jobs) as pool:
        for line in pool.map(one, order):
            print(line, flush=True)


def mean(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.mean(xs), 2) if xs else None


def report(args) -> None:
    root = Path(args.out)
    blind = json.loads((root / "blind.json").read_text())
    tasks = {t["id"]: t for t in TASKS}
    rows = []
    for r in sorted((root / "runs").glob("*.json")):
        run = json.loads(r.read_text())
        kinds = {i["id"]: i["kind"] for i in tasks[run["task"]]["key"]}
        for gdir in sorted(root.glob("grades-*")):
            g = json.loads((gdir / f"{blind[r.stem]}.json").read_text()).get("grade") if (gdir / f"{blind[r.stem]}.json").exists() else None
            if not g:
                continue
            items = g.get("items", {})
            frac = lambda kind: mean([1.0 if items.get(i) else 0.0 for i, k in kinds.items() if k == kind])
            u = run["usage"]
            rows.append({"task": run["task"], "arm": run["arm"], "judge": gdir.name[7:],
                         "key": mean([1.0 if items.get(i) else 0.0 for i in kinds]),
                         "correct": frac("correctness"), "detect": frac("failure_detection"),
                         "decision": g.get("decision_quality"), "verify": g.get("verification_quality"),
                         "overclaims": g.get("overclaims"),
                         "in_tok": u.get("input_tokens"), "out_tok": u.get("output_tokens"),
                         "words": len(run["text"].split()), "seconds": run["seconds"]})
    cols = ["key", "correct", "detect", "decision", "verify", "overclaims", "in_tok", "out_tok", "words", "seconds"]

    def table(group_keys):
        groups = {}
        for row in rows:
            groups.setdefault(tuple(row[k] for k in group_keys), []).append(row)
        print("| " + " | ".join(group_keys + ["n"] + cols) + " |")
        print("|" + "---|" * (len(group_keys) + 1 + len(cols)))
        for key in sorted(groups):
            g = groups[key]
            print("| " + " | ".join([*map(str, key), str(len(g))] + [str(mean([x[c] for x in g])) for c in cols]) + " |")
        print()

    table(["judge", "arm"])
    table(["judge", "task", "arm"])
    (root / "rows.json").write_text(json.dumps(rows, indent=1))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate")
    g.add_argument("--old-ref", required=True)
    g.add_argument("--new-ref", required=True)
    g.add_argument("--samples", type=int, default=3)
    g.add_argument("--jobs", type=int, default=4)
    g.add_argument("--out", required=True)
    j = sub.add_parser("judge")
    j.add_argument("--judge", choices=["codex", "gemini"], required=True)
    j.add_argument("--jobs", type=int, default=4)
    j.add_argument("--out", required=True)
    r = sub.add_parser("report")
    r.add_argument("--out", required=True)
    args = ap.parse_args()
    {"generate": generate, "judge": judge, "report": report}[args.cmd](args)


if __name__ == "__main__":
    main()
