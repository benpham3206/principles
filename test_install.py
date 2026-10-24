"""Tests for install.py. Run: python -m unittest test_install"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import threading
import time
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
POLICY_FANOUT = Path(__file__).parent / "tests" / "fixtures" / "policy_fanout.py"


class TestPolicy(Fixture):
    """Run policy through the installer and pinned upstream file I/O, in a temp home."""

    fanout = POLICY_FANOUT

    def setUp(self) -> None:
        super().setUp()
        (self.clone / "policy.md").write_text("rule one\n")
        (self.home / ".codex").mkdir()
        self.codex = self.home / ".codex" / "AGENTS.md"
        self.own_text = ("# My rules\nKeep caf\u00e9 text.\n\n"
                         "<!-- BEGIN ben-other -->\nkeep this block\n<!-- END ben-other -->\n")
        self.codex.write_text(self.own_text, encoding="utf-8")
        self.hermes = self.home / ".hermes" / "skills" / "software-development" / "hermes-execution-todo"
        for folder in (".claude", ".grok/rules", ".cursor/rules", ".kiro/steering"):
            (self.home / folder).mkdir(parents=True)
        (self.hermes / "references").mkdir(parents=True)
        (self.hermes / "SKILL.md").write_text("# My Hermes skill\n")
        with mock.patch.object(install, "FANOUT", self.fanout):
            fo = install.load_fanout()
        fo.HOME = self.home  # instruction_targets reads HOME at call time: keep every write in the temp home
        for patch in (mock.patch.object(install, "load_fanout", return_value=fo),
                      mock.patch.object(install, "HERMES", self.hermes)):
            patch.start()
            self.addCleanup(patch.stop)

    def test_check_reports_drift_and_writes_nothing(self) -> None:
        before = {p.relative_to(self.home): p.read_bytes() if p.is_file() else None
                  for p in self.home.rglob("*")}
        self.assertGreater(install.policy(check=True), 0)
        self.assertEqual({p.relative_to(self.home): p.read_bytes() if p.is_file() else None
                          for p in self.home.rglob("*")}, before)

    def test_writes_block_keeps_own_text_then_check_is_clean(self) -> None:
        install.policy(check=False)
        block = ("<!-- BEGIN ben-engineering-policy (managed by propagate-across-harnesses; edit "
                 "~/.agents/skill-repos/benpham3206__principles/policy.md, then rerun) -->\n"
                 "rule one\n<!-- END ben-engineering-policy -->\n")
        self.assertEqual(self.codex.read_text(encoding="utf-8"), self.own_text + "\n" + block)
        before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.home.rglob("*") if p.is_file()}
        self.assertEqual(install.policy(check=True), 0)
        install.policy(check=False)
        self.assertEqual({p: (p.read_bytes(), p.stat().st_mtime_ns)
                          for p in self.home.rglob("*") if p.is_file()}, before)

    def test_rerun_replaces_the_block_in_place(self) -> None:
        install.policy(check=False)
        original = self.codex.read_text(encoding="utf-8") + "\n# My footer\nKeep this too.\n"
        self.codex.write_text(original, encoding="utf-8")
        body = "rule two: literal \\1 and \\path\nnext line"
        (self.clone / "policy.md").write_text(body + "\n")
        self.assertGreater(install.policy(check=True), 0)
        self.assertEqual(self.codex.read_text(encoding="utf-8"), original)
        install.policy(check=False)
        text = self.codex.read_text(encoding="utf-8")
        self.assertEqual(text.count("BEGIN ben-engineering-policy"), 1)
        self.assertEqual(text, original.replace("rule one", body))
        self.assertEqual(install.policy(check=True), 0)

    def test_grok_rules_folder_gets_its_own_file(self) -> None:
        install.policy(check=False)
        self.assertIn("rule one", (self.home / ".grok" / "rules" / "ben-engineering-policy.md").read_text())

    def test_present_harnesses_get_headers_and_hermes_pointer(self) -> None:
        install.policy(check=False)
        cursor = (self.home / ".cursor/rules/ben-engineering-policy.mdc").read_text()
        self.assertTrue(cursor.startswith("---\ndescription: Engineering policy from principles (Ben fleet)\nalwaysApply: true\n---\n"))
        kiro = (self.home / ".kiro/steering/engineering-policy.md").read_text()
        self.assertTrue(kiro.startswith("---\ntitle: Engineering policy from principles\ninclusion: always\n---\n"))
        for text in (cursor, kiro, (self.hermes / "references/engineering-policy.md").read_text()):
            self.assertIn("rule one", text)
        pointer = (self.hermes / "SKILL.md").read_text()
        self.assertTrue(pointer.startswith("# My Hermes skill\n"))
        self.assertIn(install.HERMES_POINTER, pointer)

    def test_absent_harnesses_and_missing_instruction_files_stay_absent(self) -> None:
        install.policy(check=False)
        for path in (".claude/CLAUDE.md", ".grok/AGENTS.md", ".config", "FABLE", ".kimi", ".gemini", ".copilot"):
            with self.subTest(path=path):
                self.assertFalse((self.home / path).exists())

    def test_duplicate_blocks_refuse_without_changing_the_file(self) -> None:
        install.policy(check=False)
        duplicate = self.codex.read_text(encoding="utf-8") * 2
        self.codex.write_text(duplicate, encoding="utf-8")
        for check in (True, False):
            with self.subTest(check=check), self.assertRaises(ValueError):
                install.policy(check=check)
            self.assertEqual(self.codex.read_text(encoding="utf-8"), duplicate)

    def test_missing_policy_is_skipped(self) -> None:
        (self.clone / "policy.md").unlink()
        before = {p.relative_to(self.home): p.read_bytes() if p.is_file() else None
                  for p in self.home.rglob("*")}
        self.assertEqual(install.policy(check=True), 0)
        self.assertEqual(install.policy(check=False), 0)
        self.assertEqual({p.relative_to(self.home): p.read_bytes() if p.is_file() else None
                          for p in self.home.rglob("*")}, before)


@unittest.skipUnless(REAL_FANOUT.is_file(), "optional integration: agent-hooks fanout.py is not installed")
class TestPolicyRealFanout(TestPolicy):
    """Keep the same policy contract checked against installed agent-hooks when present."""

    fanout = REAL_FANOUT


def sh(cwd: Path, *args: str) -> str:
    return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-c", "commit.gpgsign=false", *args],
                          cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


class TestPull(unittest.TestCase):
    """pull() deploys exactly origin, from a clean clone, or refuses."""

    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        self.origin, self.work, self.clone = root / "origin", root / "work", root / "clone"
        sh(root, "init", "-q", "--bare", "-b", "main", str(self.origin))
        sh(root, "clone", "-q", str(self.origin), str(self.work))
        (self.work / "a").write_text("1")
        sh(self.work, "add", "a")
        sh(self.work, "commit", "-qm", "one")
        sh(self.work, "push", "-q", "origin", "HEAD:main")
        sh(root, "clone", "-q", str(self.origin), str(self.clone))
        for patch in (mock.patch.object(install, "CLONE", self.clone),
                      mock.patch.object(install, "ORIGIN", str(self.origin))):
            patch.start()
            self.addCleanup(patch.stop)

    def upstream(self) -> None:
        (self.work / "a").write_text("2")
        sh(self.work, "commit", "-qam", "two")
        sh(self.work, "push", "-q", "origin", "HEAD:main")

    def test_fast_forwards_to_exactly_origin(self) -> None:
        self.upstream()
        self.assertEqual(install.pull(), 0)
        self.assertEqual(sh(self.clone, "rev-parse", "HEAD"), sh(self.work, "rev-parse", "HEAD"))

    def test_local_commit_is_refused_even_with_nothing_new_upstream(self) -> None:
        (self.clone / "b").write_text("local")
        sh(self.clone, "add", "b")
        sh(self.clone, "commit", "-qm", "local")
        self.assertEqual(install.pull(), 1)

    def test_tracked_edit_is_refused_even_when_it_would_not_conflict(self) -> None:
        (self.work / "c").write_text("x")  # upstream touches only c, so git would merge
        sh(self.work, "add", "c")
        sh(self.work, "commit", "-qm", "three")
        sh(self.work, "push", "-q", "origin", "HEAD:main")
        (self.clone / "a").write_text("edited")
        self.assertEqual(install.pull(), 1)

    def test_untracked_file_is_refused(self) -> None:
        self.upstream()
        (self.clone / "skills").mkdir()
        (self.clone / "skills" / "planted").mkdir()
        (self.clone / "skills" / "planted" / "SKILL.md").write_text("x")
        self.assertEqual(install.pull(), 1)

    def test_clone_pointing_elsewhere_is_refused(self) -> None:
        with mock.patch.object(install, "ORIGIN", "https://example.invalid/other"):
            self.assertEqual(install.pull(), 1)

    def test_untracked_file_is_refused_even_when_git_config_hides_untracked(self) -> None:
        sh(self.clone, "config", "status.showUntrackedFiles", "no")
        (self.clone / "skills" / "planted").mkdir(parents=True)
        (self.clone / "skills" / "planted" / "SKILL.md").write_text("x")
        self.assertEqual(install.pull(), 1)


@unittest.skipUnless(Path("/bin/sh").exists(), "needs /bin/sh; CI runs these on Linux")
class TestPosixScripts(unittest.TestCase):
    """Run the POSIX remote scripts for real against a temporary HOME and origin.

    The clone's install.py is a stand-in that only records that it ran, so a script that
    reaches the installer when it should have refused leaves a mark.
    """

    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.home = Path(tmp.name)
        self.origin, work = self.home / "origin", self.home / "work"
        self.clone = self.home / ".agents" / "skill-repos" / "benpham3206__principles"
        self.mark = self.home / "ran"
        sh(self.home, "init", "-q", "--bare", "-b", "main", str(self.origin))
        sh(self.home, "clone", "-q", str(self.origin), str(work))
        (work / "install.py").write_text(f"open({str(self.mark)!r}, 'w').write('ran')\n")
        sh(work, "add", "install.py")
        sh(work, "commit", "-qm", "one")
        sh(work, "push", "-q", "origin", "HEAD:main")
        sh(self.home, "clone", "-q", str(self.origin), str(self.clone))

    def script(self, text: str) -> int:
        text = text.replace(install.ORIGIN, str(self.origin))
        env = {**os.environ, "HOME": str(self.home)}
        return subprocess.run(["/bin/sh", "-c", text], env=env, capture_output=True, text=True).returncode

    def assert_refused(self) -> None:
        for name in ("POSIX_CHECK", "POSIX_UPDATE"):
            with self.subTest(name):
                self.mark.unlink(missing_ok=True)
                self.assertNotEqual(self.script(getattr(install, name)), 0)
                self.assertFalse(self.mark.exists(), f"{name} ran the installer")

    def test_clean_clone_runs_the_installer(self) -> None:
        for name in ("POSIX_CHECK", "POSIX_UPDATE"):
            with self.subTest(name):
                self.assertEqual(self.script(getattr(install, name)), 0)
                self.assertTrue(self.mark.exists())
                self.mark.unlink()

    def test_modified_installer_is_never_run(self) -> None:
        (self.clone / "install.py").write_text(f"open({str(self.mark)!r}, 'w').write('evil')\n")
        self.assert_refused()

    def test_local_commit_is_never_run(self) -> None:
        sh(self.clone, "commit", "-qm", "local", "--allow-empty")
        self.assert_refused()

    def test_untracked_file_hidden_by_config_is_refused(self) -> None:
        sh(self.clone, "config", "status.showUntrackedFiles", "no")
        (self.clone / "planted").write_text("x")
        self.assert_refused()

    def test_dry_run_does_not_rewrite_the_index(self) -> None:
        index = self.clone / ".git" / "index"
        os.utime(self.clone / "install.py", ns=(1, 1))  # stale stat data: plain status rewrites the index
        before = index.stat().st_mtime_ns
        self.assertEqual(self.script(install.POSIX_CHECK), 0)
        self.assertEqual(index.stat().st_mtime_ns, before)

    def test_failing_git_status_is_refused(self) -> None:
        (self.clone / ".git" / "index").write_bytes(b"not an index")
        self.assert_refused()


class TestCheckNeverWrites(unittest.TestCase):
    def test_check_all_does_not_pull_and_sends_remotes_a_dry_run(self) -> None:
        with mock.patch.object(install, "pull") as pull, \
                mock.patch.object(install, "install", return_value=0) as local, \
                mock.patch.object(install, "aliases", return_value=["mac", "windows"]), \
                mock.patch.object(install, "update_remote", return_value=0) as remote:
            install.main(["--check", "--all"])
        pull.assert_not_called()
        local.assert_called_once_with(True)
        self.assertEqual([c.args for c in remote.call_args_list], [("mac", True), ("windows", True)])

    def test_dry_run_scripts_never_pull_and_update_scripts_check_origin_first(self) -> None:
        for check in (install.POSIX_CHECK, install.WINDOWS_CHECK):
            for command in ("git -C $R pull", "fetch", "merge", "git clone"):
                self.assertNotIn(command, check)
            self.assertIn("--check", check)
        for script in (install.POSIX_UPDATE, install.WINDOWS_UPDATE, install.POSIX_CHECK, install.WINDOWS_CHECK):
            self.assertLess(script.index("remote get-url"), script.index("install.py"))
        for update in (install.POSIX_UPDATE, install.WINDOWS_UPDATE):
            self.assertLess(update.index("status --porcelain"), update.index("merge"))
            self.assertLess(update.index("rev-list"), update.index("merge"))
            self.assertNotIn("pull -q", update)

    def test_windows_scripts_guard_before_running_the_installer(self) -> None:
        # No PowerShell here to run them, so check their shape: every git call's exit code is
        # checked, untracked files are always listed, and the guards come before the installer.
        for script in (install.WINDOWS_CHECK, install.WINDOWS_UPDATE):
            with self.subTest(script[-20:]):
                for guard in ("status --porcelain --untracked-files=all", "rev-list origin/main..HEAD"):
                    self.assertLess(script.index(guard), script.index("install.py"))
                calls = script.count("git -C $R") + script.count("git --no-optional-locks -C $R") + script.count("git clone")
                self.assertIn("git --no-optional-locks -C $R status", script)
                self.assertEqual(script.count("if ($LASTEXITCODE) { exit 1 }"), calls)


class TestRemoteShell(unittest.TestCase):
    def test_windows_fallback_runs_powershell_and_macs_run_zsh(self) -> None:
        sent = {}

        def fake_run(cmd, timeout, **kw):
            sent[cmd[-2]] = (cmd[-1], kw["input"])
            return subprocess.CompletedProcess(cmd, 0)
        with mock.patch.object(install, "REMOTE", Path("/nonexistent/remote.py")), \
                mock.patch.object(install, "run", side_effect=fake_run):
            install.update_remote("windows")
            install.update_remote("mbp13")
        self.assertTrue(sent["windows"][0].startswith("powershell"))
        self.assertEqual(sent["windows"][1], install.WINDOWS_UPDATE)
        self.assertEqual(sent["mbp13"][0], "zsh -l")


class TestDeadlines(unittest.TestCase):
    def test_a_stalled_child_comes_back_as_a_failure(self) -> None:
        done = install.run([sys.executable, "-c", "import time; time.sleep(5)"], 1)
        self.assertEqual(done.returncode, 124)
        self.assertIn("timed out", done.stderr)

    def test_an_orphan_holding_the_output_cannot_stall_the_timeout(self) -> None:
        # The PHAMPC hang: git was killed on timeout, but git-remote-https, which it had
        # started, still held the inherited stdout, so subprocess.run waited for it forever.
        # Here a child starts a 60 s grandchild that inherits stdout, then stalls itself.
        with tempfile.TemporaryDirectory() as tmp:
            pidfile = Path(tmp) / "grandchild.pid"
            child = ("import subprocess, sys, time; "
                     "p = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)']); "
                     "open(sys.argv[1], 'w').write(str(p.pid)); print('started', flush=True); time.sleep(60)")
            box: dict = {}
            worker = threading.Thread(daemon=True, target=lambda: box.update(done=install.run(
                [sys.executable, "-c", child, str(pidfile)], 2, capture_output=True, text=True)))
            start = time.monotonic()
            worker.start()
            worker.join(20)  # watchdog: without the fix run() waits the full 60 s
            elapsed = time.monotonic() - start
            pid = int(pidfile.read_text()) if pidfile.is_file() else None
            try:
                self.assertFalse(worker.is_alive(), "run() did not return within 20 s")
                self.assertLess(elapsed, 10)
                done = box["done"]
                self.assertEqual(done.returncode, 124)
                self.assertIn("timed out after 2 s", done.stderr)
                self.assertIsNotNone(pid)
                deadline = time.monotonic() + 5
                while alive(pid) and time.monotonic() < deadline:
                    time.sleep(0.1)
                self.assertFalse(alive(pid), f"grandchild {pid} outlived the timeout")
                self.assertEqual(done.stdout, "started\n")  # output captured before the timeout is kept
            finally:
                if pid is not None and alive(pid):
                    kill(pid)

    def test_a_timeout_mid_character_still_comes_back_as_a_failure(self) -> None:
        # A child killed while writing can leave half a UTF-8 character in the captured output.
        script = "import sys, time; sys.stdout.buffer.write(b'cost \\xe2\\x82'); sys.stdout.flush(); time.sleep(30)"
        done = install.run([sys.executable, "-c", script], 1, capture_output=True, text=True)
        self.assertEqual(done.returncode, 124)
        self.assertTrue(done.stdout.startswith("cost "))
        self.assertIn("timed out after 1 s", done.stderr)

    def test_output_and_input_come_back_on_a_normal_run(self) -> None:
        script = ("import sys; print(sys.stdin.read().upper(), end=''); "
                  "print('to stderr', file=sys.stderr); sys.exit(3)")
        done = install.run([sys.executable, "-c", script], 30, input="one\ntwo\n", capture_output=True, text=True)
        self.assertEqual((done.returncode, done.stdout, done.stderr), (3, "ONE\nTWO\n", "to stderr\n"))
        raw = install.run([sys.executable, "-c", "import sys; sys.stdout.write(sys.stdin.read())"], 30,
                          input=b"bytes", capture_output=True)
        self.assertEqual((raw.returncode, raw.stdout, raw.stderr), (0, b"bytes", b""))


def alive(pid: int) -> bool:
    if sys.platform.startswith("win"):
        # Never os.kill(pid, 0) on Windows: it terminates the process.
        out = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH", "/FO", "CSV"],
                             capture_output=True, text=True).stdout
        return f'"{pid}"' in out
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    # A zombie waiting for init to reap it runs nothing and holds no handles: not alive.
    state = subprocess.run(["ps", "-o", "stat=", "-p", str(pid)], capture_output=True, text=True).stdout
    return bool(state.strip()) and not state.strip().startswith("Z")


def kill(pid: int) -> None:
    if sys.platform.startswith("win"):
        subprocess.run(["taskkill", "/F", "/PID", str(pid)], capture_output=True)
    else:
        os.kill(pid, 9)


if __name__ == "__main__":
    unittest.main()
