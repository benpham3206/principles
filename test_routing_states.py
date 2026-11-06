#!/usr/bin/env python3
"""Every route in the Choose a skill map and the policy's Choose guidance reaches a real
skill folder, and every skill folder is reached (routing_model.py, run by check_states.py).

The live map and policy must pass; each known-bad routing must fail on the rule it breaks.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import routing_model as rm

ROOT = Path(__file__).resolve().parent
CHECKER = ROOT / "skills" / "principles-verify" / "check_states.py"
SKILLS = {"principles", "principles-a", "principles-b"}
GOOD = [("map", "Do a", [("", "principles-a")]), ("map", "Do b", [("", "principles-b")])]


def check(model: Path) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as tmp:
        done = subprocess.run([sys.executable, str(CHECKER), str(model), "--out", tmp],
                              capture_output=True, text=True, timeout=60)
        return done.returncode, done.stdout + done.stderr


def check_routes(tasks: list, skills: set) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "model.py"
        path.write_text(f"import sys\nsys.path.insert(0, {str(ROOT)!r})\nfrom routing_model import model\n"
                        f"globals().update(model({tasks!r}, {skills!r}))\n", encoding="utf-8")
        return check(path)


class TestLiveRouting(unittest.TestCase):
    def test_live_map_and_policy_hold(self) -> None:
        code, out = check(ROOT / "routing_model.py")
        self.assertEqual(code, 0, out)

    def test_map_alone_reaches_every_skill(self) -> None:
        # The map is the hub an agent reads; a skill reached only through policy.md is a map gap.
        tasks, skills = rm.live()
        code, out = check_routes([t for t in tasks if t[0] == "map"], skills)
        self.assertEqual(code, 0, out)


class TestBrokenRouting(unittest.TestCase):
    def assert_breaks(self, tasks: list, skills: set, rule: str) -> None:
        code, out = check_routes(tasks, skills)
        self.assertEqual(code, 1, out)
        self.assertIn(f"Breaks: {rule}", out)

    def test_known_good_fixture_holds(self) -> None:
        self.assertEqual(check_routes(GOOD, SKILLS)[0], 0)

    def test_missing_skill_folder_breaks(self) -> None:
        self.assert_breaks(GOOD + [("map", "Do c", [("", "principles-c")])], SKILLS, "Named skill exists")

    def test_task_with_no_skill_breaks(self) -> None:
        self.assert_breaks(GOOD + [("policy", "Do nothing", [])], SKILLS, "Every task reaches a skill")

    def test_undeclared_overlap_breaks(self) -> None:
        self.assert_breaks(GOOD + [("map", "Do a again", [("", "principles-a")])], SKILLS,
                           "No undeclared overlap")

    def test_overlap_under_a_repeated_task_label_breaks(self) -> None:
        self.assert_breaks(GOOD + [GOOD[0]], SKILLS, "No undeclared overlap")

    def test_odd_skill_name_beside_a_good_one_breaks(self) -> None:
        tasks = rm.map_tasks("## Choose a skill\n\n| Task | Skills |\n|---|---|\n"
                             "| Do a | `principles-a`; `principles-b`; `principles-c2` |\n")
        self.assert_breaks([("map", *t) for t in tasks], SKILLS, "Named skill exists")

    def test_declared_overlap_holds(self) -> None:
        skills = SKILLS | {"principles-craft"}
        tasks = GOOD + [("map", t, [("", "principles-craft")]) for t in ("Judge", "Check")]
        self.assertEqual(check_routes(tasks, skills)[0], 0)

    def test_orphan_skill_folder_breaks(self) -> None:
        self.assert_breaks(GOOD, SKILLS | {"principles-z"}, "Every skill folder is reachable")


class TestExtract(unittest.TestCase):
    def test_map_row_without_a_skill_is_an_error(self) -> None:
        with self.assertRaises(ValueError):
            rm.map_tasks("## Choose a skill\n\n| Task | Skills |\n|---|---|\n| Do a | nothing named |\n")

    def test_policy_route_without_a_skill_is_an_error(self) -> None:
        mapped = [(rm.MEDIUM_ROW, [("", "principles-a")])]
        with self.assertRaises(ValueError):
            rm.policy_tasks("### Choose guidance\n- Joining parts: ask someone.\n", mapped)


if __name__ == "__main__":
    unittest.main()
