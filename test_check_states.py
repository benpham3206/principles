#!/usr/bin/env python3
"""The state checker in principles-verify, run the way an agent runs it.

Each test guards a promise that skill makes about check_states.py: the shortest path to
each broken rule, no reachable state skipped, deadlock unless an end state is declared,
a bound that never reports a rule as proven, a model failure that never passes, and a
chart whose marks and text match the search.
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

# A long chain is yielded first and last; the direct route to the bad state is yielded in
# the middle, so a depth-first search in either order reports a longer path.
THREE_ROUTES = """
init = "start"
NEXT = {"start": [("go long", "a1"), ("go direct", "bad1"), ("go round", "b1")],
        "a1": [("on", "a2")], "a2": [("on", "bad2")], "b1": [("on", "b2")], "b2": [("on", "bad3")]}
def steps(s):
    yield from NEXT.get(s, [])
rules = {"Never bad": lambda s: not s.startswith("bad")}
end = lambda s: s.startswith("bad")
label = lambda s: "Bad" if s.startswith("bad") else ("Chain" if s[0] in "ab" else "Start")
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


def path_steps(out: str, rule: str) -> list[str]:
    section = out.split(f"## Shortest path to break: {rule}")[1].split("##")[0]
    return [l for l in section.splitlines() if l[:1].isdigit()]


class TestSearch(unittest.TestCase):
    def test_broken_rule_reports_the_shortest_path_and_exits_1(self) -> None:
        code, out, _, _ = check("GUARD = True\n" + CHECKOUT)
        self.assertEqual(code, 1, out)
        steps = path_steps(out, "You are charged at most once")
        self.assertEqual(len(steps), 5, steps)
        self.assertTrue(steps[-1].startswith("5. the card clears: Paid"), steps[-1])

    def test_path_is_the_shortest_whatever_order_the_steps_are_yielded_in(self) -> None:
        code, out, _, _ = check(THREE_ROUTES)
        self.assertEqual(code, 1, out)
        self.assertEqual([l.split(":")[0] for l in path_steps(out, "Never bad")], ["1. start", "2. go direct"])

    def test_fixed_model_holds_and_exits_0(self) -> None:
        code, out, _, chart = check("GUARD = False\n" + CHECKOUT)
        self.assertEqual(code, 0, out)
        self.assertIn("- Holds: You are charged at most once", out)
        self.assertIn("- Holds: No deadlock", out)
        self.assertIn("s2 --> [*]", chart)

    def test_values_a_rule_can_tell_apart_are_different_states(self) -> None:
        # Each pair compares equal in Python; merging them would hide the second state's break.
        pairs = [('{"x": []}', '{"x": ()}', 'type(s["x"]) is list'),
                 ('{"x": 1}', '{"x": True}', 'type(s["x"]) is int'),
                 ('{"x": 0.0}', '{"x": -0.0}', 'str(s["x"]) == "0.0"'),
                 ('{"a": 0, "b": 0}', '{"b": 0, "a": 0}', 'next(iter(s)) == "a"'),
                 ('float("nan")', '-float("nan")', 'math.copysign(1.0, s) > 0'),
                 ('set([0, 8])', 'set([8, 0])', 'next(iter(s)) == 0')]
        self.assertNotEqual(list(set([0, 8])), list(set([8, 0])))   # the last pair iterates differently here
        for a, b, rule in pairs:
            model = (f'import math\ninit = [{a}, {b}]\ndef steps(s):\n    return []\n'
                     f'end = lambda s: True\nrules = {{"First kind": lambda s: {rule}}}\n')
            code, out, _, _ = check(model)
            self.assertEqual(code, 1, (a, b, out))
            self.assertIn("Explored 2 states", out)

    def test_every_rule_is_checked_and_gets_its_own_shortest_path(self) -> None:
        model = ('init = {"n": 0}\ndef steps(s):\n    if s["n"] < 5:\n        yield "count", {"n": s["n"] + 1}\n'
                 'end = lambda s: s["n"] == 5\n'
                 'rules = {"Holds always": lambda s: s["n"] >= 0, "Under 2": lambda s: s["n"] < 2,\n'
                 '         "Under 4": lambda s: s["n"] < 4}\n')
        code, out, _, _ = check(model)
        self.assertEqual(code, 1, out)
        self.assertIn("- Holds: Holds always", out)
        self.assertEqual(len(path_steps(out, "Under 2")), 3)
        self.assertEqual(len(path_steps(out, "Under 4")), 5)

    def test_enum_members_are_states(self) -> None:
        model = ('import enum\nclass Phase(enum.Enum):\n    IDLE = 1\n    DONE = 2\ninit = Phase.IDLE\n'
                 'def steps(s):\n    if s is Phase.IDLE:\n        yield "finish", Phase.DONE\n'
                 'end = lambda s: s is Phase.DONE\n')
        code, out, _, _ = check(model)
        self.assertEqual(code, 0, out)
        self.assertIn("Explored 2 states", out)

    def test_a_model_that_edits_and_reuses_one_state_loses_no_successor(self) -> None:
        model = ('init = {"n": [0]}\ndef steps(s):\n    if s["n"][0] == 0:\n'
                 '        s["n"][0] = 1\n        yield "left", s\n        s["n"][0] = 2\n        yield "right", s\n'
                 'end = lambda s: s["n"][0] > 0\nrules = {"Never two": lambda s: s["n"][0] != 2}\n'
                 'label = lambda s: str(s["n"][0])\n')
        code, out, _, chart = check(model)
        self.assertEqual(code, 1, out)
        self.assertIn("Explored 3 states", out)
        self.assertEqual([l.split(" `")[0] for l in path_steps(out, "Never two")], ["1. start: 0", "2. right: 2"])
        self.assertIn("s0 --> s1 : left", chart)
        self.assertIn("s0 --> s2 : right", chart)

    def test_state_with_no_step_out_is_a_deadlock_unless_declared_an_end(self) -> None:
        model = 'init = {"n": 0}\ndef steps(s):\n    if s["n"] < 2:\n        yield "count", {"n": s["n"] + 1}\n'
        code, out, _, _ = check(model)
        self.assertEqual(code, 1, out)
        self.assertIn("- Breaks: No deadlock", out)
        code, out, _, _ = check(model + 'end = lambda s: s["n"] == 2\n')
        self.assertEqual(code, 0, out)


class TestBound(unittest.TestCase):
    GROWS = 'init = {"n": 0}\ndef steps(s):\n    yield "count", {"n": s["n"] + 1}\n'

    def test_search_stopped_at_the_bound_proves_nothing_and_exits_2(self) -> None:
        code, out, _, _ = check(self.GROWS + 'rules = {"Small": lambda s: s["n"] >= 0}\n', "--max-states", "50")
        self.assertEqual(code, 2, out)
        self.assertIn("Explored 50 states", out)
        self.assertIn("- Not proven: Small", out)
        self.assertNotIn("Holds", out)

    def test_a_break_found_before_the_bound_still_exits_1(self) -> None:
        code, out, _, _ = check(self.GROWS + 'rules = {"Under 3": lambda s: s["n"] < 3}\n', "--max-states", "50")
        self.assertEqual(code, 1, out)
        self.assertEqual(len(path_steps(out, "Under 3")), 4)

    def test_start_states_count_against_the_bound(self) -> None:
        code, out, _, _ = check('init = [{"n": 0}, {"n": 1}]\ndef steps(s):\n    return []\nend = lambda s: True\n',
                                "--max-states", "1")
        self.assertEqual(code, 2, out)
        self.assertIn("Explored 1 states", out)

    def test_a_bound_below_1_is_refused(self) -> None:
        code, _, err, _ = check(self.GROWS, "--max-states", "0")
        self.assertEqual(code, 2)
        self.assertIn("must be 1 or more", err)


class TestModelFailure(unittest.TestCase):
    def test_every_model_failure_exits_2_with_a_reason(self) -> None:
        cases = {
            'init = {"n": 0}\ndef steps(s):\n    yield "oops"\n': "{'n': 0}",
            "def steps(s) return []\n": "SyntaxError",
            'raise RuntimeError("top level")\n': "top level",
            "import no_such_module_for_check_states\n": "ModuleNotFoundError",
            'def steps(s):\n    return []\n': "does not define init",
            'init = {"n": 0}\ndef steps(s):\n    return []\nend = lambda s: True\nrules = {"No deadlock": lambda s: True}\n':
                "built-in deadlock check",
            'init = {"f": bytearray(b"x")}\ndef steps(s):\n    return []\n': "a state holds",
            "raise SystemExit(0)\n": "SystemExit",
            "raise SystemExit(1)\n": "SystemExit",
            'import sys\ninit = 0\ndef steps(s):\n    sys.exit(0)\n    yield\n': "SystemExit",
            # Outside the state contract: an object with its own equality, one list in two places, a cycle.
            'class Thing:\n    pass\ninit = {"t": Thing()}\ndef steps(s):\n    return []\n': "a state holds a Thing",
            'shared = [0]\ninit = {"a": shared, "b": shared}\ndef steps(s):\n    return []\n': "in two places",
            'init = {}\ninit["me"] = init\ndef steps(s):\n    return []\n': "in two places",
            # A crash in the checker must not exit 1, which means a rule breaks.
            'init = 0\nfor _ in range(5000):\n    init = (init,)\ndef steps(s):\n    return []\n': "RecursionError",
        }
        for model, reason in cases.items():
            code, _, err, _ = check(model)
            self.assertEqual(code, 2, model)
            self.assertIn(reason, err, model)


class TestChart(unittest.TestCase):
    def test_marks_tell_a_state_that_always_breaks_from_one_that_sometimes_does(self) -> None:
        _, out, _, chart = check(THREE_ROUTES)
        self.assertIn('state "Bad" as s2', chart)
        self.assertIn("class s2 breaks", chart)      # every state labeled Bad breaks the rule
        self.assertNotIn("class s0 ", chart)         # Start never breaks it
        self.assertNotIn("class s1 ", chart)         # nor does Chain
        _, out, _, chart = check("GUARD = True\n" + CHECKOUT)
        self.assertIn("class s2 mayBreak", chart)
        self.assertIn("(1 of 2 states behind it)", out)

    def test_a_label_of_any_type_becomes_text(self) -> None:
        code, out, _, chart = check('init = 0\ndef steps(s):\n    yield ["wait"], s\n')
        self.assertEqual(code, 0, out)
        self.assertIn("s0 --> s0 : ['wait']", chart)

    def test_a_step_that_stays_in_one_box_is_drawn(self) -> None:
        _, out, _, chart = check('init = {"n": 0}\ndef steps(s):\n    yield "wait", s\n')
        self.assertIn("s0 --> s0 : wait", chart)
        self.assertIn("- Holds: No deadlock", out)

    def test_text_that_cannot_be_encoded_is_escaped_not_fatal(self) -> None:
        code, out, err, _ = check('title = "\\ud800"\ninit = 0\ndef steps(s):\n    return []\nend = lambda s: True\n')
        self.assertEqual(code, 0, err)
        self.assertIn("# State check: \\ud800", out)

    def test_chart_text_cannot_change_the_chart_syntax(self) -> None:
        model = ('title = "[#1: \\"x\\"]"\ninit = {"a": 0}\ndef steps(s):\n    if s["a"] == 0:\n'
                 '        yield \'you type "x: y"; #1\\ns0 --> s0 : invented\', {"a": 1}\n'
                 'end = lambda s: s["a"] == 1\nlabel = lambda s: \'Step: "one"\' if s["a"] else "Start"\n')
        code, out, _, chart = check(model)
        self.assertEqual(code, 0, out)
        self.assertIn('title: "[#1: \\"x\\"]"', chart)
        self.assertIn('state "Step#58; #quot;one#quot;" as s1', chart)
        self.assertIn("s0 --> s1 : you type #quot;x#58; y#quot;#59; #35;1 s0 --> s0 #58; invented", chart)
        self.assertNotIn("s0 --> s0 : invented", chart)


if __name__ == "__main__":
    unittest.main()
