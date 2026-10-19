"""Tests for install.py. Run: python -m unittest test_install"""

from __future__ import annotations

import os
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


class TestPrune(Fixture):
    def setUp(self) -> None:
        super().setUp()
        self.harness = self.home / "harness-skills"
        self.harness.mkdir()
        fanout = self.home / "fanout.py"
        fanout.write_text(f"SKILL_DIRS = [{str(self.harness)!r}]\n")
        patch = mock.patch.object(install, "FANOUT", fanout)
        patch.start()
        self.addCleanup(patch.stop)
        for name in ("judge", "visual"):
            install.link(name, check=False)
            install.make_link(self.harness / name, self.agent_skills / name)
        (self.harness / "own").mkdir()  # a real folder in the harness: never touched

    def remove_skill(self, name: str) -> None:
        skill = self.clone / "skills" / name
        (skill / "SKILL.md").unlink()
        skill.rmdir()

    def test_nothing_to_prune_when_all_skills_exist(self) -> None:
        self.assertEqual(install.prune(["judge", "visual"], check=False), [])

    def test_check_reports_without_removing(self) -> None:
        self.remove_skill("visual")
        found = install.prune(["judge"], check=True)
        self.assertEqual({p.name for p in found}, {"visual"})
        self.assertEqual(len(found), 2)
        self.assertTrue(install.is_link(self.harness / "visual"))

    def test_removes_both_links_and_keeps_everything_else(self) -> None:
        self.remove_skill("visual")
        install.prune(["judge"], check=False)
        self.assertFalse(os.path.lexists(self.harness / "visual"))
        self.assertFalse(os.path.lexists(self.agent_skills / "visual"))
        self.assertTrue((self.harness / "judge" / "SKILL.md").is_file())
        self.assertTrue((self.harness / "own").is_dir())


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


REAL_FANOUT = install.FANOUT


@unittest.skipUnless(REAL_FANOUT.is_file(), "agent-hooks fanout.py is not installed")
class TestPolicy(Fixture):
    def setUp(self) -> None:
        super().setUp()
        (self.clone / "policy.md").write_text("rule one\n")
        (self.home / ".codex").mkdir()
        self.codex = self.home / ".codex" / "AGENTS.md"
        self.codex.write_text("mine\n")
        with mock.patch.object(install, "FANOUT", REAL_FANOUT):
            fo = install.load_fanout()
        fo.HOME = self.home  # instruction_targets reads HOME at call time: keep every write in the temp home
        for patch in (mock.patch.object(install, "load_fanout", lambda: fo),
                      mock.patch.object(install, "HERMES", self.home / "no-hermes")):
            patch.start()
            self.addCleanup(patch.stop)

    def test_check_reports_drift_and_writes_nothing(self) -> None:
        self.assertGreater(install.policy(check=True), 0)
        self.assertEqual(self.codex.read_text(), "mine\n")

    def test_writes_block_keeps_own_text_then_check_is_clean(self) -> None:
        install.policy(check=False)
        text = self.codex.read_text()
        self.assertIn("mine", text)
        self.assertIn("rule one", text)
        self.assertEqual(install.policy(check=True), 0)

    def test_rerun_replaces_the_block_in_place(self) -> None:
        install.policy(check=False)
        (self.clone / "policy.md").write_text("rule two\n")
        install.policy(check=False)
        text = self.codex.read_text()
        self.assertEqual(text.count("BEGIN ben-engineering-policy"), 1)
        self.assertNotIn("rule one", text)
        self.assertIn("rule two", text)

    def test_missing_policy_is_skipped(self) -> None:
        (self.clone / "policy.md").unlink()
        self.assertEqual(install.policy(check=True), 0)


if __name__ == "__main__":
    unittest.main()
