"""Tests for install.py. Run: python -m unittest test_install"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import install


class Fixture(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.home = Path(tmp.name)
        self.clone = self.home / "clone"
        self.agent_skills = self.home / "agent-skills"
        for name in ("judge", "visual"):
            (self.clone / "skills" / name).mkdir(parents=True)
            (self.clone / "skills" / name / "SKILL.md").write_text("---\nname: x\n---\n")
        (self.clone / "skills" / "notes").mkdir()  # no SKILL.md: not a skill
        for patch in (mock.patch.object(install, "CLONE", self.clone),
                      mock.patch.object(install, "AGENT_SKILLS", self.agent_skills),
                      mock.patch.object(install, "HOME", self.home)):
            patch.start()
            self.addCleanup(patch.stop)


class TestSkills(Fixture):
    def test_lists_only_folders_with_skill_md(self) -> None:
        self.assertEqual(install.skills(self.clone), ["judge", "visual"])

    def test_missing_folder_is_empty(self) -> None:
        self.assertEqual(install.skills(self.home / "nowhere"), [])


class TestLink(Fixture):
    def test_check_reports_missing_and_writes_nothing(self) -> None:
        self.assertEqual(install.link("judge", check=True), "missing")
        self.assertFalse((self.agent_skills / "judge").exists())

    def test_links_then_rerun_is_ok(self) -> None:
        self.assertEqual(install.link("judge", check=False), "linked")
        self.assertTrue((self.agent_skills / "judge" / "SKILL.md").is_file())
        self.assertEqual(install.link("judge", check=False), "ok")

    def test_foreign_folder_is_a_conflict_and_kept(self) -> None:
        (self.agent_skills / "judge").mkdir(parents=True)
        (self.agent_skills / "judge" / "mine.txt").write_text("keep")
        self.assertEqual(install.link("judge", check=False), "conflict")
        self.assertTrue((self.agent_skills / "judge" / "mine.txt").is_file())


class TestStale(Fixture):
    def test_reports_link_to_removed_skill_only(self) -> None:
        install.link("judge", check=False)
        install.link("visual", check=False)
        (self.agent_skills / "other").mkdir()
        self.assertEqual(install.stale(["judge"]), ["visual"])


class TestAliases(Fixture):
    def test_keeps_fleet_aliases_in_fleet_order(self) -> None:
        (self.home / ".ssh").mkdir()
        (self.home / ".ssh" / "config").write_text(
            "Host github-x\n  HostName github.com\nHost windows\nHost mbp13\n  User b\n")
        self.assertEqual(install.aliases(), ["mbp13", "windows"])

    def test_no_config_means_no_aliases(self) -> None:
        self.assertEqual(install.aliases(), [])


class TestInstall(Fixture):
    def test_check_on_fresh_machine_is_drift(self) -> None:
        fanout = self.home / "fanout.py"
        fanout.write_text("")
        with mock.patch.object(install, "FANOUT", fanout):
            self.assertEqual(install.install(check=True), 1)
        self.assertFalse(self.agent_skills.exists())

    def test_missing_fanout_fails_before_linking(self) -> None:
        with mock.patch.object(install, "FANOUT", self.home / "absent.py"):
            self.assertEqual(install.install(check=False), 1)
        self.assertFalse(self.agent_skills.exists())


if __name__ == "__main__":
    unittest.main()
