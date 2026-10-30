#!/usr/bin/env python3
"""Skill file checks, run the way a harness would trip over them.

    python3 -m unittest            # discovers this file next to test_install.py

frontmatter_errors parses the `---` block the way a strict YAML reader does: a
second `: ` inside an unquoted scalar is an error, because harnesses that parse
frontmatter as YAML then fail and the skill silently never registers.
"""

from __future__ import annotations

import inspect
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BAD_START = set("-?:,[]{}#&*!|>'\"%@`")
FIELD = re.compile(r"^([A-Za-z_][\w-]*):(?: (.*))?$")


def frontmatter_errors(text: str) -> list[str]:
    """Structural and scalar errors in a SKILL.md frontmatter block."""
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return ["file does not start with ---"]
    close = next((i for i in range(1, len(lines)) if lines[i] == "---"), None)
    if close is None:
        return ["no closing ---"]
    errors: list[str] = []
    fields: dict[str, str] = {}
    for i in range(1, close):
        line = lines[i]
        m = FIELD.match(line)
        if not m:
            errors.append(f"line {i + 1} is not 'key: value': {line!r}")
            continue
        key, value = m.group(1), m.group(2) or ""
        fields[key] = value
        if value.startswith(("'", '"')):
            if len(value) < 2 or not value.endswith(value[0]):
                errors.append(f"{key}: quoted value does not close on the line")
            continue
        if value and value[0] in BAD_START:
            errors.append(f"{key}: value starts with {value[0]!r}")
            continue
        if ": " in value:
            errors.append(f"{key}: unquoted value contains ': '")
        if " #" in value:
            errors.append(f"{key}: unquoted value contains ' #'")
    for required in ("name", "description"):
        if required not in fields:
            errors.append(f"missing {required}")
    return errors


def _fields(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}
    fields = {}
    for line in lines[1:]:
        if line == "---":
            break
        m = FIELD.match(line)
        if m:
            fields[m.group(1)] = m.group(2) or ""
    return fields


def meta_errors(name: str, description: str, folder: str) -> list[str]:
    """name must equal the folder name; description must be under 45 words."""
    errors = []
    if name != folder:
        errors.append(f"name {name!r} does not equal folder {folder!r}")
    if len(description.split()) >= 45:
        errors.append(f"description has {len(description.split())} words (limit 45)")
    return errors


REF = re.compile(r"principles-[a-z-]+")


def ref_errors(text: str, names: set[str]) -> list[str]:
    """Every principles-<name> token must be an existing skill folder."""
    return [f"dangling reference {t!r}" for t in
            sorted({m.rstrip("-") for m in REF.findall(text)} - names)]


def ascii_errors(text: str) -> list[str]:
    """Non-ASCII outside fenced code blocks, and NUL anywhere (a file saved as UTF-16)."""
    errors = ["NUL bytes: the file is not UTF-8 (UTF-16?)"] if "\x00" in text else []
    fenced = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced:
            for ch in line:
                if ord(ch) > 127:
                    errors.append(f"line {i}: non-ASCII {ch!r}")
                    break
    return errors


LINK = re.compile(r"https?://|\]\((?!#)")


def link_errors(text: str) -> list[str]:
    """A link out of the family, outside fenced code blocks; in-page anchors are allowed."""
    errors = []
    fenced = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and LINK.search(line):
            errors.append(f"line {i}: link out of the family")
    return errors


AXES = ("Form", "Material", "Energy", "Observer", "Composition", "Time")
MEDIA = ("visual", "sound", "touch", "language", "interaction", "information", "code", "machine")
SHAPE = ("Laws of the medium", "Defaults to replace", "Tree") + AXES
LEAF_HEADER = "| Leaf | Principle | Failure | Check |"


def shape_errors(text: str) -> list[str]:
    """A medium skill has the AGENTS.md sections in order, and each axis section a Leaf table."""
    sections: list[tuple[str, list[str]]] = []
    for line in text.splitlines():
        if line.startswith("## "):
            sections.append((line[3:].strip(), []))
        elif sections:
            sections[-1][1].append(line)
    titles = [t for t, _ in sections]
    errors = []
    for want, got in zip(SHAPE, titles):
        if not got.startswith(want):
            errors.append(f"section {got!r} where {want!r} belongs")
            return errors
    if len(titles) < len(SHAPE):
        return [f"missing sections {list(SHAPE[len(titles):])}"]
    for title, body in sections[3:3 + len(AXES)]:
        if LEAF_HEADER not in body:
            errors.append(f"## {title} has no {LEAF_HEADER} table")
    return errors


STOCK = re.compile(r"\b(crucial|delve|robust|comprehensive|seamless(ly)?|utili[sz]e|ensure|landscape)\b", re.I)


def stock_errors(text: str) -> list[str]:
    """Stock vocabulary AGENTS.md bans, outside fenced code blocks."""
    errors = []
    fenced = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and (m := STOCK.search(line)):
            errors.append(f"line {i}: stock word {m.group(0)!r}")
    return errors


AXES_ROW = re.compile(r"^\| \*\*Form\*\* \|", re.M)
ONE_LINE = "In one line: "
ONE_LINE_WORDS = 20


def one_line_errors(text: str) -> list[str]:
    """The first line after the title states the skill's rule in one sentence."""
    lines = text.splitlines()
    title = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if title is None:
        return ["no '# ' title"]
    first = next((l for l in lines[title + 1:] if l.strip()), "")
    if not first.startswith(ONE_LINE):
        return [f"first line after the title must start with {ONE_LINE!r}"]
    body = first[len(ONE_LINE):]
    errors = []
    if len(body.split()) > ONE_LINE_WORDS:
        errors.append(f"one line has {len(body.split())} words; keep it to {ONE_LINE_WORDS}")
    if not body.endswith(".") or ". " in body:
        errors.append("one line must be a single sentence ending in a period")
    return errors


def tracked_markdown() -> list[Path]:
    out = subprocess.check_output(["git", "ls-files", "*.md"], cwd=ROOT)
    return [ROOT / f for f in out.decode().splitlines()]


def skill_dirs() -> list[Path]:
    return sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())


class TestFrontmatter(unittest.TestCase):
    GOOD = "---\nname: x\ndescription: Verify work before it is done.\n---\n\n# X\n"

    def test_second_colon_in_unquoted_value_is_an_error(self) -> None:
        text = "---\nname: x\ndescription: Verify any work before calling it done: true, works, and good.\n---\n"
        self.assertTrue(frontmatter_errors(text))

    def test_hash_comment_in_unquoted_value_is_an_error(self) -> None:
        text = "---\nname: x\ndescription: done # not a comment\n---\n"
        self.assertTrue(frontmatter_errors(text))

    def test_missing_description_is_an_error(self) -> None:
        self.assertTrue(frontmatter_errors("---\nname: x\n---\n"))

    def test_unclosed_quote_is_an_error(self) -> None:
        text = '---\nname: x\ndescription: "never closed\n---\n'
        self.assertTrue(frontmatter_errors(text))

    def test_valid_frontmatter_has_no_errors(self) -> None:
        self.assertEqual(frontmatter_errors(self.GOOD), [])


class TestMeta(unittest.TestCase):
    def test_name_folder_mismatch_is_an_error(self) -> None:
        self.assertTrue(meta_errors("visual", "d", "sound"))

    def test_45_word_description_is_an_error(self) -> None:
        self.assertTrue(meta_errors("x", " ".join(["word"] * 45), "x"))

    def test_valid_meta_has_no_errors(self) -> None:
        self.assertEqual(meta_errors("x", "short description", "x"), [])


class TestRefs(unittest.TestCase):
    def test_dangling_reference_is_an_error(self) -> None:
        self.assertTrue(ref_errors("see `principles-nope`", {"principles-verify"}))

    def test_resolving_reference_has_no_errors(self) -> None:
        self.assertEqual(ref_errors("see `principles-verify`", {"principles-verify"}), [])


class TestAscii(unittest.TestCase):
    def test_non_ascii_outside_fence_is_an_error(self) -> None:
        self.assertTrue(ascii_errors("plain text with a — dash"))

    def test_non_ascii_inside_a_fence_passes(self) -> None:
        self.assertEqual(ascii_errors("```\n├── tree\n```\nplain\n"), [])

    def test_utf16_text_is_an_error(self) -> None:
        self.assertTrue(ascii_errors("# Title\n".encode("utf-16-le").decode("utf-8")))

    def test_plain_ascii_has_no_errors(self) -> None:
        self.assertEqual(ascii_errors("all plain\n"), [])


class TestLinks(unittest.TestCase):
    def test_outside_link_is_an_error(self) -> None:
        self.assertTrue(link_errors("See [a guide](https://example.com)."))

    def test_relative_link_is_an_error(self) -> None:
        self.assertTrue(link_errors("See [notes](../notes.md)."))

    def test_in_page_anchor_passes(self) -> None:
        self.assertEqual(link_errors("Go to [Control](#control)."), [])


class TestShape(unittest.TestCase):
    GOOD = "\n".join(
        [f"## {s}\n" for s in SHAPE[:3]]
        + [f"## {a}\n{LEAF_HEADER}\n" for a in AXES]
        + ["## Extra branch\n"])

    def test_valid_shape_has_no_errors(self) -> None:
        self.assertEqual(shape_errors(self.GOOD), [])

    def test_axis_section_out_of_order_is_an_error(self) -> None:
        self.assertTrue(shape_errors(self.GOOD.replace("## Form", "## Formx").replace("## Material", "## Form")))

    def test_missing_axis_section_is_an_error(self) -> None:
        self.assertTrue(shape_errors(self.GOOD.split("## Time")[0]))

    def test_axis_section_without_leaf_table_is_an_error(self) -> None:
        self.assertTrue(shape_errors(self.GOOD.replace(f"## Energy\n{LEAF_HEADER}", "## Energy\nprose")))


class TestStock(unittest.TestCase):
    def test_stock_word_is_an_error(self) -> None:
        self.assertTrue(stock_errors("This is a robust design."))

    def test_stock_word_inside_a_fence_passes(self) -> None:
        self.assertEqual(stock_errors("```\nrobust\n```\n"), [])

    def test_plain_words_pass(self) -> None:
        self.assertEqual(stock_errors("Name a mechanism or a number."), [])


class TestOneLine(unittest.TestCase):
    GOOD = "---\nname: x\n---\n\n# X\n\nIn one line: Check the work against evidence before calling it done.\n\nBody.\n"

    def test_valid_one_line_has_no_errors(self) -> None:
        self.assertEqual(one_line_errors(self.GOOD), [])

    def test_missing_one_line_is_an_error(self) -> None:
        self.assertTrue(one_line_errors("# X\n\nA **term** is defined here.\n"))

    def test_long_one_line_is_an_error(self) -> None:
        self.assertTrue(one_line_errors("# X\n\nIn one line: " + " ".join(["word"] * 21) + ".\n"))

    def test_two_sentences_are_an_error(self) -> None:
        self.assertTrue(one_line_errors("# X\n\nIn one line: Do this. Then that.\n"))


def unproven_checkers(namespace: dict, source: str) -> list[str]:
    """Checkers with no known-bad case: no test asserts that they return errors."""
    return sorted(n for n, f in namespace.items()
                  if n.endswith("_errors") and callable(f) and f"assertTrue({n}(" not in source)


class TestKnownBad(unittest.TestCase):
    def test_checker_without_a_known_bad_case_is_reported(self) -> None:
        self.assertEqual(unproven_checkers({"x_errors": len}, "assertEqual(x_errors(''), [])"), ["x_errors"])

    def test_checker_with_a_known_bad_case_passes(self) -> None:
        self.assertEqual(unproven_checkers({"x_errors": len}, "assertTrue(x_errors('bad'))"), [])


class TestRepo(unittest.TestCase):
    def test_every_checker_is_seen_to_fail(self) -> None:
        # principles-verify: a check that cannot fail proves nothing; each checker keeps a known-bad case.
        module = sys.modules[__name__]
        self.assertEqual(unproven_checkers(vars(module), inspect.getsource(module)), [])

    def test_every_skill_states_its_rule_in_one_line(self) -> None:
        errors = [f"{d.name}: {e}" for d in skill_dirs()
                  for e in one_line_errors((d / "SKILL.md").read_text(encoding="utf-8"))]
        self.assertEqual(errors, [])

    def test_all_tracked_markdown_passes(self) -> None:
        errors = []
        names = {p.name for p in skill_dirs()}
        for d in skill_dirs():
            skill = d / "SKILL.md"
            text = skill.read_text(encoding="utf-8")
            errors += [f"{skill}: {e}" for e in frontmatter_errors(text)]
            fields = _fields(text)
            errors += [f"{skill}: {e}" for e in
                       meta_errors(fields.get("name", ""), fields.get("description", ""), d.name)]
        for md in tracked_markdown():
            text = md.read_text(encoding="utf-8")
            errors += [f"{md}: {e}" for e in ref_errors(text, names)]
            errors += [f"{md}: {e}" for e in ascii_errors(text)]
        for e in errors:
            print(e)
        self.assertEqual(errors, [])

    def test_every_skill_pairs_with_another_and_is_reachable(self) -> None:
        pairs = {}
        for d in skill_dirs():
            lines = [l for l in (d / "SKILL.md").read_text(encoding="utf-8").splitlines()
                     if l.startswith("Pairs with:")]
            if d.name != "principles":
                self.assertEqual(len(lines), 1, f"{d.name}: needs exactly one 'Pairs with:' line")
            pairs[d.name] = {m.rstrip("-") for l in lines for m in REF.findall(l)} - {d.name}
        reached = set().union(*pairs.values())
        orphans = {n for n in pairs if n != "principles"} - reached
        self.assertEqual(orphans, set(), "no other skill pairs with these")

    def test_medium_skills_follow_the_shape(self) -> None:
        names = {p.name for p in skill_dirs()}
        self.assertLessEqual({f"principles-{m}" for m in MEDIA}, names, "a medium skill folder is missing")
        errors = [f"principles-{m}: {e}" for m in MEDIA for e in
                  shape_errors((ROOT / "skills" / f"principles-{m}" / "SKILL.md").read_text(encoding="utf-8"))]
        self.assertEqual(errors, [])

    def test_no_stock_vocabulary(self) -> None:
        # AGENTS.md and principles-language name the banned words in order to ban them.
        exempt = {ROOT / "AGENTS.md", ROOT / "skills" / "principles-language" / "SKILL.md"}
        errors = [f"{md}: {e}" for md in tracked_markdown() if md not in exempt
                  for e in stock_errors(md.read_text(encoding="utf-8"))]
        self.assertEqual(errors, [])

    def test_skills_and_policy_are_self_contained(self) -> None:
        # AGENTS.md, Self-contained: skills and policy.md link to nothing outside the family.
        files = [d / "SKILL.md" for d in skill_dirs()] + [ROOT / "policy.md"]
        errors = [f"{f}: {e}" for f in files for e in link_errors(f.read_text(encoding="utf-8"))]
        self.assertEqual(errors, [])

    def test_six_axes_are_defined_in_one_place(self) -> None:
        owners = [d.name for d in skill_dirs()
                  if AXES_ROW.search((d / "SKILL.md").read_text(encoding="utf-8"))]
        self.assertEqual(owners, ["principles"])

    def test_every_skill_is_listed_in_the_readme_and_the_map(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        mapping = (ROOT / "skills" / "principles" / "SKILL.md").read_text(encoding="utf-8")
        missing = [f"README: {d.name}" for d in skill_dirs() if f"`{d.name}`" not in readme]
        missing += [f"map: {d.name}" for d in skill_dirs()
                    if d.name != "principles" and f"`{d.name}`" not in mapping]
        self.assertEqual(missing, [])

    def test_policy_stays_short(self) -> None:
        text = (ROOT / "policy.md").read_text(encoding="utf-8")
        lines = text.splitlines()
        self.assertLessEqual(len(lines), 50, "policy.md loads in every session; keep it to 50 lines or fewer")
        self.assertLessEqual(len(text.split()), 550, "policy.md loads in every session; keep it to 550 words or fewer")


if __name__ == "__main__":
    unittest.main()
