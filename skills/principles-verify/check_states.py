#!/usr/bin/env python3
"""Check every reachable state of a small model, then report each broken rule and chart it.

    python3 check_states.py MODEL.py [--out DIR] [--max-states N]

MODEL.py defines:
    init       a start state, or a list of them. A state is a tree of dicts, lists, tuples,
               sets, frozensets, enum members, and None, bool, int, float, complex, str,
               and bytes values, with no container in two places; anything else is refused
    steps(s)   yields (what the reader sees happen, next state); each yielded state is
               copied at once, so a model may edit and reuse one dict
    rules      {sentence the reader agrees to: predicate that is true in a good state};
               "No deadlock" is reserved for the built-in check
    end(s)     optional: true where stopping is correct, so no deadlock is reported there
    label(s)   optional: the chart's words for a state; states with one label share a box
    title      optional: the chart title

The search is breadth-first, so the path it reports to each broken rule is a shortest
one. A state with no step out that is not an end state breaks "No deadlock". Writes
DIR/report.md and DIR/chart.mmd and prints the report. Exit 0: every rule holds in every
reachable state. Exit 1: a rule breaks, even if the search stopped early, and nothing
else. Exit 2: no verdict, because the search stopped at --max-states (start states count)
with no rule broken, or the model or the check failed. Python 3.9 or later, standard
library only.
"""

from __future__ import annotations

import argparse
import copy
import enum
import json
import runpy
import struct
import sys
from collections import deque
from pathlib import Path

DEADLOCK = "No deadlock"
ARROW_BUDGET = 20
CHART_BUDGET = 500


class ModelError(Exception):
    pass


MODEL_FAILURES = (Exception, SystemExit)    # a model calling exit() must not set the exit code


PLAIN = (type(None), bool, int, str, bytes)
CONTAINERS = (dict, list, tuple, set, frozenset)


def freeze(v, inside=None):
    """A hashable key for a state. Two states share a key only when a copy of each looks
    the same to every rule and step: same types, same float bits, same order in every
    container. The state contract is closed, because an object with its own equality, or
    one container in two places, could make two different states look equal."""
    t = type(v)
    if t in PLAIN or isinstance(v, enum.Enum):
        return (t, v)
    if t is float:
        return (t, struct.pack("!d", v))
    if t is complex:
        return (t, struct.pack("!dd", v.real, v.imag))
    if t not in CONTAINERS:
        raise ModelError(f"a state holds a {t.__name__}; use dicts, lists, tuples, sets, frozensets, "
                         "enum members, and None, bool, int, float, complex, str, or bytes values")
    inside = set() if inside is None else inside
    if t in (dict, list, set):
        if id(v) in inside:
            raise ModelError(f"a state holds one {t.__name__} in two places; give each place its own copy")
        inside.add(id(v))
    if t is dict:
        return (t, tuple((freeze(k, inside), freeze(x, inside)) for k, x in v.items()))
    return (t, tuple(freeze(x, inside) for x in v))


def call(fn, s, what):
    try:
        return fn(copy.deepcopy(s))
    except MODEL_FAILURES as e:
        raise ModelError(f"{what} failed in state {s!r}: {type(e).__name__}: {e}") from e


def successors(model: dict, s) -> list:
    """Each (step, next state), copied as it is yielded, so a model may edit and reuse one dict."""
    out = []
    try:
        for step in model["steps"](copy.deepcopy(s)):
            if not (isinstance(step, tuple) and len(step) == 2):
                raise ModelError(f"steps() must yield (label, next state); got {step!r} in state {s!r}")
            out.append((str(step[0]), copy.deepcopy(step[1])))
    except ModelError:
        raise
    except MODEL_FAILURES as e:
        raise ModelError(f"steps() failed in state {s!r}: {type(e).__name__}: {e}") from e
    return out


def explore(model: dict, max_states: int):
    starts = model["init"] if isinstance(model["init"], list) else [model["init"]]
    rules = dict(model.get("rules", {}))
    end = model.get("end", lambda s: False)
    seen: dict = {}            # key -> (state, parent key, step that reached it)
    order: list = []           # keys in breadth-first order
    queue: deque = deque()
    complete = True
    for s in starts:
        s = copy.deepcopy(s)
        k = freeze(s)
        if k in seen:
            continue
        if len(seen) >= max_states:
            complete = False
            continue
        seen[k] = (s, None, None)
        queue.append(k)
    arrows: set = set()        # (from key, step, to key)
    bad: dict = {name: [] for name in [*rules, DEADLOCK]}
    while queue:
        k = queue.popleft()
        order.append(k)
        s = seen[k][0]
        for name, ok in rules.items():
            if not call(ok, s, f"rule {name!r}"):
                bad[name].append(k)
        out = successors(model, s)
        if not out and not call(end, s, "end()"):
            bad[DEADLOCK].append(k)
        for name, t in out:
            tk = freeze(t)
            if tk not in seen:
                if len(seen) >= max_states:
                    complete = False
                    continue
                seen[tk] = (t, k, name)
                queue.append(tk)
            arrows.add((k, name, tk))
    return seen, order, arrows, bad, complete


def path(seen: dict, k) -> list:
    out = []
    while k is not None:
        out.append(k)
        k = seen[k][1]
    return out[::-1]


MERMAID_ESCAPES = {"#": "#35;", '"': "#quot;", ":": "#58;", ";": "#59;", "\n": " ", "\r": " "}


def mermaid_text(t: str) -> str:
    return "".join(MERMAID_ESCAPES.get(c, c) for c in t)


def plural(n: int, word: str) -> str:
    return f"{n} {word}{'' if n == 1 else 's'}"


def build(model: dict, seen, order, arrows, bad, complete, max_states: int, source: str):
    label = model.get("label", lambda s: repr(s))
    end = model.get("end", lambda s: False)
    title = model.get("title", Path(source).stem)
    box: dict = {}             # chart label -> node id
    node: dict = {}            # state key -> node id
    behind: dict = {}          # node id -> state keys
    for k in order:
        text = str(call(label, seen[k][0], "label()"))
        nid = box.setdefault(text, f"s{len(box)}")
        node[k] = nid
        behind.setdefault(nid, []).append(k)
    names = {nid: text for text, nid in box.items()}
    broken = {r: ks for r, ks in bad.items() if ks}
    marks: dict = {}           # node id -> [(rule, states behind it that break it)]
    for r, ks in broken.items():
        hit = set(ks)
        for nid, keys in behind.items():
            n = sum(k in hit for k in keys)
            if n:
                marks.setdefault(nid, []).append((r, n))
    drawn = sorted({(node[a], str(step), node[b]) for a, step, b in arrows
                    if a in node and b in node})

    lines = ["---", f"title: {json.dumps(str(title))}", "---", "stateDiagram-v2"]
    lines += [f'    state "{mermaid_text(text)}" as {nid}' for text, nid in box.items()]
    starts = [k for k in order if seen[k][1] is None]
    lines += [f"    [*] --> {nid}" for nid in dict.fromkeys(node[k] for k in starts)]
    lines += [f"    {a} --> {b} : {mermaid_text(str(step))}" for a, step, b in drawn]
    ends = dict.fromkeys(node[k] for k in order if call(end, seen[k][0], "end()"))
    lines += [f"    {nid} --> [*]" for nid in ends]
    lines += ["    classDef breaks fill:#f8d7da,stroke:#b02a37,color:#58151c",
              "    classDef mayBreak fill:#fff3cd,stroke:#997404,color:#332701"]
    for nid, rs in marks.items():
        lines.append(f"    class {nid} {'breaks' if any(n == len(behind[nid]) for _, n in rs) else 'mayBreak'}")
    chart = "\n".join(lines) + "\n"

    rep = [f"# State check: {title}", "",
           f"Explored {len(seen)} states and {len(arrows)} steps from {plural(len(starts), 'start state')}. "
           + ("The search was complete." if complete else
              f"The search stopped at {max_states} states, so a rule that held is not proven."),
           (f"The chart has {len(box)} states and {len(drawn)} arrows." if len(box) <= CHART_BUDGET else
            f"No chart: {len(box)} chart states is over the budget of {CHART_BUDGET}. Merge labels in label()."),
           "", "## Rules", ""]
    for r in bad:
        status = "Breaks" if bad[r] else ("Holds" if complete else "Not proven")
        rep.append(f"- {status}: {r}")
    for r, ks in broken.items():
        rep += ["", f"## Shortest path to break: {r}", ""]
        for i, k in enumerate(path(seen, ks[0]), 1):
            s, _, step = seen[k]
            rep.append(f"{i}. {'start' if step is None else step}: {names[node[k]]} `{s!r}`")
    if marks:
        rep += ["", "## Chart marks", ""]
        for nid, rs in marks.items():
            for r, n in rs:
                full = n == len(behind[nid])
                rep.append(f"- {names[nid]}: {'breaks' if full else 'may break'} {r!r}"
                           + ("" if full else f" ({n} of {len(behind[nid])} states behind it)"))
    return (chart if len(box) <= CHART_BUDGET else None), "\n".join(rep) + "\n", len(drawn), bool(broken)


def positive(text: str) -> int:
    n = int(text)
    if n < 1:
        raise argparse.ArgumentTypeError("must be 1 or more")
    return n


def load(path: Path) -> dict:
    try:
        model = runpy.run_path(str(path))
    except MODEL_FAILURES as e:
        raise ModelError(f"could not load {path}: {type(e).__name__}: {e}") from e
    missing = [n for n in ("init", "steps") if n not in model]
    if missing:
        raise ModelError(f"{path} does not define {', '.join(missing)}")
    if not isinstance(model.get("rules", {}), dict):
        raise ModelError("rules must be a dict of {sentence: predicate}")
    if DEADLOCK in model.get("rules", {}):
        raise ModelError(f"{DEADLOCK!r} is the built-in deadlock check; give your rule another name")
    return model


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("model", type=Path)
    ap.add_argument("--out", type=Path, help="output folder (default: MODEL.check next to the model)")
    ap.add_argument("--max-states", type=positive, default=100_000)
    args = ap.parse_args(argv)
    out = args.out or args.model.with_suffix(".check")
    try:
        model = load(args.model)
        found = explore(model, args.max_states)
        chart, report, n_arrows, broken = build(model, *found, args.max_states, str(args.model))
        out.mkdir(parents=True, exist_ok=True)
        (out / "report.md").write_text(report, encoding="utf-8", errors="backslashreplace")
        if chart is None:
            (out / "chart.mmd").unlink(missing_ok=True)
        else:
            (out / "chart.mmd").write_text(chart, encoding="utf-8", errors="backslashreplace")
        print(report, end="")
        print(f"\nWrote {out / 'report.md'}" + ("" if chart is None else f" and {out / 'chart.mmd'}"))
    except ModelError as e:
        print(f"check_states: {e}", file=sys.stderr)
        return 2
    except Exception as e:     # exit 1 means a rule breaks, so no other failure may end with it
        print(f"check_states: could not finish: {type(e).__name__}: {e}", file=sys.stderr)
        return 2
    if chart is not None and n_arrows > ARROW_BUDGET:
        print(f"check_states: the chart has {n_arrows} arrows; merge labels in label() "
              f"toward {ARROW_BUDGET} so a reader can follow it", file=sys.stderr)
    return 1 if broken else (0 if found[4] else 2)


if __name__ == "__main__":
    sys.stdout.reconfigure(errors="backslashreplace")
    raise SystemExit(main())
