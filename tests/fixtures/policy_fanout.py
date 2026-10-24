"""Read-only policy excerpt from agent-hooks, not a success-only fanout mock.

Source: https://github.com/benpham3206/agent-hooks/blob/c018b7e678c3d2854ac2c56dfd8ef3ea079abef4/skills/propagate-across-harnesses/fanout.py
Upstream file SHA-256: 550618129f467f5475b6813f0f0e7b597fbee357ee59e2f171b0eab52197a364
Extracted verbatim: instruction_targets, render, install_rule (including their I/O).
Only module imports and HOME initialization are reduced to their dependencies.
TestPolicy sets HOME to a temporary directory after install.load_fanout() imports it.
Do not edit these definitions; refresh from a reviewed upstream commit instead.
This pins CI behavior; TestPolicyRealFanout also checks the installed dependency.
"""
from __future__ import annotations

import re
from pathlib import Path

HOME = Path.home()


def instruction_targets(tag: str, title: str) -> list[tuple[str, Path, str | None]]:
    """(harness, file, head). head None: edit only if the file exists. Else create with head."""
    return [
        ("canonical", HOME / "FABLE/AGENTS.md", None),
        ("claude-code", HOME / ".claude/CLAUDE.md", None),
        ("codex", HOME / ".codex/AGENTS.md", None),
        ("grok", HOME / ".grok/AGENTS.md", None),
        ("kimi", HOME / ".kimi/AGENTS.md", None),
        ("gemini", HOME / ".gemini/GEMINI.md", None),
        ("copilot", HOME / ".copilot/copilot-instructions.md", None),
        ("opencode", HOME / ".config/opencode/AGENTS.md", ""),
        ("cursor", HOME / f".cursor/rules/ben-{tag}.mdc",
         f"---\ndescription: {title} (Ben fleet)\nalwaysApply: true\n---\n\n"),
        ("kiro", HOME / f".kiro/steering/{tag}.md", f"---\ntitle: {title}\ninclusion: always\n---\n\n"),
    ]


def render(text: str, tag: str, body: str, source: str) -> str:
    """Return text with exactly one managed block for tag holding body."""
    begin = f"<!-- BEGIN ben-{tag} "
    end = f"<!-- END ben-{tag} -->"
    if text.count(begin) > 1:
        raise ValueError(f"more than one ben-{tag} block; fix by hand")
    block = f"{begin}(managed by propagate-across-harnesses; edit {source}, then rerun) -->\n{body}\n{end}"
    pattern = re.compile(re.escape(begin) + ".*?" + re.escape(end), re.S)
    if pattern.search(text):
        return pattern.sub(lambda _: block, text)
    text = text.rstrip("\n")
    return f"{text}\n\n{block}\n" if text else f"{block}\n"


def install_rule(tag: str, body: str, source: str, targets, check: bool) -> int:
    drift = 0
    for harness, path, head in targets:
        if not path.parent.is_dir():
            print(f"skip     {harness:12} absent: {path.parent}")
            continue
        if not path.exists() and head is None:
            print(f"skip     {harness:12} no instruction file: {path}")
            continue
        old = path.read_text(encoding="utf-8") if path.exists() else head
        new = render(old, tag, body, source)
        if new == old:
            print(f"ok       {harness:12} {path}")
        elif check:
            drift += 1
            print(f"STALE    {harness:12} {path}")
        else:
            path.write_text(new, encoding="utf-8")
            print(f"wrote    {harness:12} {path}")
    return drift
