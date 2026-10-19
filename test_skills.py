#!/usr/bin/env python3
"""Skill file checks, run the way a harness would trip over them.

    python3 -m unittest            # discovers this file next to test_install.py

frontmatter_errors parses the `---` block the way a strict YAML reader does: a
second `: ` inside an unquoted scalar is an error, because harnesses that parse
frontmatter as YAML then fail and the skill silently never registers.
"""

from __future__ import annotations

import re
import subprocess
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
    """Non-ASCII outside fenced code blocks."""
    errors = []
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

    def test_plain_ascii_has_no_errors(self) -> None:
        self.assertEqual(ascii_errors("all plain\n"), [])


class TestRepo(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
