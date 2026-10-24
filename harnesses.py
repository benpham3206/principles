"""Built-in harness map, so install.py works on a machine without agent-hooks.

Source: https://github.com/benpham3206/agent-hooks/blob/a9e6c61a68526612a2fc39195b96a7e2f5628005/skills/propagate-across-harnesses/fanout.py
Upstream file SHA-256: 47651f55cfafaa9c66b897acebabcc82f35e421a752f86099236ac8f4d8d38d7
Extracted verbatim: SKILL_DIRS, codex_homes, instruction_targets, render, install_rule, points_to, link_skill.
Only module imports and HOME initialization are reduced to their dependencies. Left out: the
skill scan, which runs agent-hooks' skill_guard.py. This repo's skills are reviewed through
pull requests, the same exemption fanout.py gives agent-hooks' own skills.
install.py uses the installed agent-hooks fanout.py when present, and this file otherwise.
Do not edit these definitions; refresh from a reviewed upstream commit instead.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

HOME = Path.home()
SKILLS = HOME / ".agents/skills"
WINDOWS = os.name == "nt"
DEVIN_SKILLS = Path(os.environ["APPDATA"], "devin/skills") if WINDOWS else HOME / ".config/devin/skills"

# Harness skill dirs. Precedent: the 2026-09-17 bend fan-out.
SKILL_DIRS = [HOME / p for p in (
    ".claude/skills", ".codex/skills", ".grok/skills", ".kimi/skills", ".gemini/skills",
    ".copilot/skills", ".cursor/skills", ".kiro/skills", ".qoder/skills", ".omp/agent/skills",
    ".t3/skills", ".warp/skills", ".codeium/windsurf/skills",
    ".hermes/skills", ".openclaw/skills", ".pi/agent/skills",
)] + [DEVIN_SKILLS]


def codex_homes() -> list[Path]:
    """~/.codex, then every other Codex home in use (CODEX_HOME=~/.codex-school)."""
    return [HOME / ".codex"] + sorted(p for p in HOME.glob(".codex?*") if p.is_dir()
                                      and ((p / "config.toml").exists() or (p / "auth.json").exists()))


def instruction_targets(tag: str, title: str) -> list[tuple[str, Path, str | None]]:
    """(harness, file, head). head None: edit only if the file exists. Else create with head."""
    return [
        ("canonical", HOME / "FABLE/AGENTS.md", None),
        ("claude-code", HOME / ".claude/CLAUDE.md", None),
        *[("codex", home / "AGENTS.md", None) for home in codex_homes()],
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


def points_to(dest: Path, src: Path) -> bool:
    """dest is a link to src. Falls back to reading the link when it cannot be followed:
    Windows OpenSSH sessions refuse to traverse junctions made without admin rights
    (WinError 448, "untrusted mount point"), and this tool's links point straight at src."""
    try:
        return dest.resolve() == src.resolve()
    except OSError:
        try:
            target = os.readlink(dest)
        except OSError:
            return False
        for prefix in ("\\\\?\\", "\\??\\"):
            target = target.removeprefix(prefix)
        return os.path.normcase(os.path.normpath(target)) == os.path.normcase(os.path.normpath(src))


def link_skill(name: str, dirs: list[Path], check: bool, source_root: Path = SKILLS) -> int:
    src = source_root / name
    if not (src / "SKILL.md").is_file():
        raise SystemExit(f"fanout: {src}/SKILL.md is missing; write the canonical skill first")
    drift = 0
    for d in dirs:
        dest = d / name
        if not d.is_dir():
            print(f"skip     absent: {d}")
        elif points_to(dest, src):
            print(f"ok       {dest}")
        elif os.path.lexists(dest):
            drift += 1
            print(f"CONFLICT {dest} is not a link to {src}; left as is")
        elif check:
            drift += 1
            print(f"MISSING  {dest}")
        elif WINDOWS:
            import _winapi  # a junction needs no admin or Developer Mode, unlike a symlink

            _winapi.CreateJunction(str(src), str(dest))
            print(f"linked   {dest} (junction)")
        else:
            dest.symlink_to(src)
            print(f"linked   {dest}")
    return drift
