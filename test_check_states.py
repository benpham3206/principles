#!/usr/bin/env python3
"""The state checker in principles-verify, run the way an agent runs it.

Each test guards a promise that skill makes about check_states.py: the shortest path to
each broken rule, deadlock unless an end state is declared, a bound that never reports a
rule as proven, a model failure that never passes, and a chart that Mermaid can parse.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

CHECKER = Path(__file__).resolve().parent / "skills" / "principles-verify" / "check_states.py"

CHECKOUT = """
init = {"phase": "idle", "charged": 0}
def steps(s):
    if s["phase"] == "idle":
        yield "you press pay", {**s, "phase": "paying"}
    if s["phase"] == "paying":
        yield "the card clears", {**s, "phase": "paid", "charged": s["charged"] + 1}
        yield "the card times out", {**s, "phase": "idle"}
    if s["phase"] == "paid" and s["charged"] < 2 and GUARD:
        yield "you press pay again", {**s, "phase": "paying"}
rules = {"You are charged at most once": lambda s: s["charged"] <= 1}
end = lambda s: s["phase"] == "paid" and s["charged"] == 1
label = lambda s: s["phase"].title()
"""


def check(model: str, *args: str) -> tuple[int, str, str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "model.py"
        path.write_text(textwrap.dedent(model), encoding="utf-8")
        out = Path(tmp) / "out"
        done = subprocess.run([sys.executable, str(CHECKER), str(path), "--out", str(out), *args],
                              capture_output=True, text=True, timeout=60)
        chart = (out / "chart.mmd").read_text(encoding="utf-8") if (out / "chart.mmd").exists() else ""
        return done.returncode, done.stdout, done.stderr, chart


class TestStateCheck(unittest.TestCase):
    def test_broken_rule_reports_the_shortest_path_and_exits_1(self) -> None:
        code, out, _, chart = check("GUARD = True\n" + CHECKOUT)
        self.assertEqual(code, 1, out)
        self.assertIn("- Breaks: You are charged at most once", out)
        path = out.split("## Shortest path to break: You are charged at most once")[1].split("##")[0]
        steps = [l for l in path.splitlines() if l[:1].isdigit()]
        self.assertEqual(len(steps), 5, path)
        self.assertTrue(steps[-1].startswith("5. the card clears: Paid"), steps[-1])
        self.assertIn("class s2 mayBreak", chart)

    def test_fixed_model_holds_and_exits_0(self) -> None:
        code, out, _, chart = check("GUARD = False\n" + CHECKOUT)
        self.assertEqual(code, 0, out)
        self.assertIn("- Holds: You are charged at most once", out)
        self.assertIn("- Holds: No deadlock", out)
        self.assertIn("s2 --> [*]", chart)

    def test_state_with_no_step_out_is_a_deadlock_unless_declared_an_end(self) -> None:
        model = 'init = {"n": 0}\ndef steps(s):\n    if s["n"] < 2:\n        yield "count", {"n": s["n"] + 1}\n'
        code, out, _, _ = check(model)
        self.assertEqual(code, 1, out)
        self.assertIn("- Breaks: No deadlock", out)
        code, out, _, _ = check(model + 'end = lambda s: s["n"] == 2\n')
        self.assertEqual(code, 0, out)

    def test_search_stopped_at_the_bound_proves_nothing_and_exits_2(self) -> None:
        model = 'init = {"n": 0}\ndef steps(s):\n    yield "count", {"n": s["n"] + 1}\nrules = {"Small": lambda s: s["n"] >= 0}\n'
        code, out, _, _ = check(model, "--max-states", "50")
        self.assertEqual(code, 2, out)
        self.assertIn("- Not proven: Small", out)
        self.assertNotIn("Holds", out)

    def test_model_failure_exits_2_and_names_the_state(self) -> None:
        code, _, err, _ = check('init = {"n": 0}\ndef steps(s):\n    yield "oops"\n')
        self.assertEqual(code, 2)
        self.assertIn("{'n': 0}", err)

    def test_path_is_the_shortest_when_a_longer_route_reaches_a_break_first_in_depth(self) -> None:
        model = ('init = {"n": 0}\ndef steps(s):\n    if s["n"] < 9:\n'
                 '        yield "you jump", {"n": s["n"] + 5}\n        yield "you step", {"n": s["n"] + 1}\n'
                 'rules = {"Below five": lambda s: s["n"] < 5}\nend = lambda s: s["n"] >= 9\n')
        code, out, _, _ = check(model)
        self.assertEqual(code, 1, out)
        path = out.split("## Shortest path to break: Below five")[1].split("##")[0]
        self.assertEqual([l.split(":")[0] for l in path.splitlines() if l[:1].isdigit()],
                         ["1. start", "2. you jump"], path)

    def test_a_model_that_edits_and_reuses_one_state_loses_no_successor(self) -> None:
        model = ('init = {"n": [0]}\ndef steps(s):\n    if s["n"][0] == 0:\n'
                 '        s["n"][0] = 1\n        yield "left", s\n        s["n"][0] = 2\n        yield "right", s\n'
                 'end = lambda s: s["n"][0] > 0\n')
        code, out, _, _ = check(model)
        self.assertEqual(code, 0, out)
        self.assertIn("Explored 3 states", out)

    def test_chart_labels_escape_the_characters_mermaid_reads_as_syntax(self) -> None:
        model = ('init = {"a": 0}\ndef steps(s):\n    if s["a"] == 0:\n        yield \'you type "x: y"; then #1\', {"a": 1}\n'
                 'end = lambda s: s["a"] == 1\nlabel = lambda s: \'Step: "one"\' if s["a"] else "Start"\n')
        code, out, _, chart = check(model)
        self.assertEqual(code, 0, out)
        self.assertIn('state "Step#58; #quot;one#quot;" as s1', chart)
        self.assertIn("s0 --> s1 : you type #quot;x#58; y#quot;#59; then #35;1", chart)


if __name__ == "__main__":
    unittest.main()
