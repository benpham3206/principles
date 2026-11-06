#!/usr/bin/env python3
"""The routing map and the policy, read as a model for check_states.py.

    python3 skills/principles-verify/check_states.py routing_model.py --out DIR

An agent picks a task from the Choose a skill table in skills/principles/SKILL.md or
from the Choose guidance list in policy.md, then loads a skill named for it. The search
checks that every task reaches a skill, every named skill has a folder, a skill claimed
by two map rows is a declared overlap, and every skill folder is reached on some path.
Axes are prompts inside a medium skill, not a load step, so they are not modeled.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HUB = "principles"
ALLOWED_OVERLAPS = {"principles-craft", "principles-ground", "principles-lessons", "principles-measure"}
MEDIUM = "the medium skill"
MEDIUM_ROW = "Work in a medium"
POLICY_ROUTE = re.compile(r"(.+): (principles-[a-z-]+|the medium skill)\.")


def map_tasks(text: str) -> list:
    """(task, [(qualifier, skill)]) for each row of the Choose a skill table."""
    section = text.split("## Choose a skill", 1)[1].split("\n## ", 1)[0]
    rows = [l for l in section.splitlines() if l.startswith("|")][2:]   # skip header and rule
    tasks = []
    for row in rows:
        cells = [c.strip() for c in row.strip("|").split("|")]
        if len(cells) != 2 or not cells[0]:
            raise ValueError(f"map row is not '| Task | Skills |': {row}")
        claims = []
        for segment in cells[1].split(";"):    # a segment that names no skill adds to the one before
            names = re.findall(r"`([^`]+)`", segment)
            if names:
                claims += [(segment.rsplit("`", 1)[1].strip(" ,"), n) for n in names]
        if not claims:
            raise ValueError(f"map row {cells[0]!r} names no skill: {cells[1]!r}")
        tasks.append((cells[0], claims))
    return tasks


def policy_tasks(text: str, mapped: list) -> list:
    """(task, [("", skill)]) for each route in the Choose guidance list of policy.md."""
    section = text.split("### Choose guidance", 1)[1].split("\n### ", 1)[0]
    medium = next(c for t, c in mapped if t == MEDIUM_ROW)
    tasks = []
    for bullet in (l[2:] for l in section.splitlines() if l.startswith("- ")):
        for sentence in re.split(r"(?<=\.)\s+", bullet.strip()):
            m = POLICY_ROUTE.fullmatch(sentence)
            if not m:
                raise ValueError(f"policy route is not 'Task: skill.': {sentence!r}")
            tasks.append((m[1], medium if m[2] == MEDIUM else [("", m[2])]))
    return tasks


def live() -> tuple:
    mapped = map_tasks((ROOT / "skills" / HUB / "SKILL.md").read_text(encoding="utf-8"))
    policy = policy_tasks((ROOT / "policy.md").read_text(encoding="utf-8"), mapped)
    tasks = [("map", t, c) for t, c in mapped] + [("policy", t, c) for t, c in policy]
    skills = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
    return tasks, skills


def model(tasks: list, skills: set) -> dict:
    """check_states.py names for tasks [(source, task, [(qualifier, skill)])] and skill folders."""
    rows: dict = {}             # skill -> positions of the map rows that claim it
    for i, (source, _, claims) in enumerate(tasks):
        for _, s in claims:
            if source == "map":
                rows.setdefault(s, set()).add(i)
    orphans = skills - {HUB} - {s for _, _, claims in tasks for _, s in claims}

    def steps(s):
        if s[0] == "start":
            for i, (source, task, _) in enumerate(tasks):    # a row is its position, so equal labels stay apart
                yield "pick a task", ("picked", source, i, task)
        elif s[0] == "picked":
            for qualifier, skill in tasks[s[2]][2]:
                yield "load a skill", ("loaded", *s[1:], qualifier, skill)
        elif s[0] == "loaded":
            yield "done", ("done", tuple(sorted(orphans)))    # the done state names any orphan

    def at(phase, ok):
        return lambda s: s[0] != phase or ok(s)

    return {
        "init": ("start",),
        "steps": steps,
        "rules": {
            "Every task reaches a skill": at("picked", lambda s: bool(tasks[s[2]][2])),
            "Named skill exists": at("loaded", lambda s: s[5] in skills),
            "No undeclared overlap": at("loaded", lambda s: s[1] != "map"
                                        or len(rows[s[5]]) == 1 or s[5] in ALLOWED_OVERLAPS),
            "Every skill folder is reachable": at("done", lambda s: not s[1]),
        },
        "end": lambda s: s[0] == "done",
        "label": lambda s: s[0].title() if len(s) < 3 else f"{s[0].title()} ({s[1]})",
        "title": "Principles routing",
    }


if __name__ == "<run_path>":    # check_states.py loads this file with runpy
    globals().update(model(*live()))
