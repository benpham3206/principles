#!/usr/bin/env python3
"""Install or update the principles skills on this machine, or on every machine.

    python3 install.py            # link every skill and fan it out to each harness present
    python3 install.py --check    # dry run: print what would change, exit 1 if anything would
    python3 install.py --pull     # fast-forward the installed clone from GitHub first
    python3 install.py --all      # --pull here, then on every other machine with an ssh alias
    python3 install.py --check --all   # dry run here and on every other machine; changes nothing

The installed copy is the clone at ~/.agents/skill-repos/benpham3206__principles, never a
working checkout, so unfinished edits never reach an agent. Each skill is linked once into
~/.agents/skills/<name> (a junction on Windows), then linked into every harness present:
by agent-hooks' fanout.py when installed, else by the built-in harness map in harnesses.py. A pull therefore updates every harness at once; only a
new skill needs a new link. Pulls are fast-forward only: a clone with local commits or edits
refuses and is reported, never overwritten. A link that points elsewhere is a conflict and
is never replaced. When a skill is renamed or removed, the links this installer made for it
are pruned (only links, never folders). policy.md is written as one managed block into every
harness instruction file present, replaced in place on each run. Same script
on Windows and macOS, Python 3.9 or later.
"""

from __future__ import annotations

import argparse
import io
import os
import signal
import subprocess
import sys
import tempfile
from pathlib import Path

ORIGIN = "https://github.com/benpham3206/principles"
BRANCH = "main"
HOME = Path.home()
CLONE = HOME / ".agents" / "skill-repos" / "benpham3206__principles"
AGENT_SKILLS = HOME / ".agents" / "skills"
FANOUT = AGENT_SKILLS / "propagate-across-harnesses" / "fanout.py"
BUILTIN = Path(__file__).resolve().parent / "harnesses.py"
REMOTE = HOME / ".agents" / "hooks" / "remote.py"
# The always-on policy. The local renderer migrates blocks from the previous installer.
POLICY = "policy.md"
POLICY_TAG = "engineering-policy"
POLICY_TITLE = "Engineering policy from principles"
HERMES = HOME / ".hermes" / "skills" / "software-development" / "hermes-execution-todo"
HERMES_POINTER = ("**Engineering policy:** load `references/engineering-policy.md`, the managed copy of "
                  "principles' `policy.md`. Fast path for cheap reversible work: build, verify, iterate.")
WIN = sys.platform.startswith("win")
CREATE_IF_MISSING = {"claude-code", "codex", "kimi", "gemini", "copilot"}
# ssh aliases this fleet uses. remote.py drives the two it knows (same guard, same logs);
# mbp13 has no remote.py target, so it gets plain ssh into a login shell. The remote command
# fast-forwards with git before running install.py, so a clone older than install.py updates too.
FLEET = ("mac", "mbp13", "windows")
REMOTE_PY_TARGETS = ("mac", "windows")

# Each remote script refuses before it pulls or runs the clone's installer unless the clone
# pulls from ORIGIN, has no local changes (untracked files included, whatever git config
# says) and no commits missing from origin/main, and every git call succeeded. The status
# call skips git's optional index refresh, so a dry run does not write .git. --check runs
# the installer's dry run only: no fetch, no pull, no writes, and its ahead test uses the
# origin/main last fetched.
# Known limits: files matched by .gitignore are not counted, because __pycache__/ appears in
# normal use. Anyone who can write the clone's .git (hooks, config, info/exclude) can run
# code through git itself; that is outside what these checks defend.
POSIX_ORIGIN = (
    f"R=~/.agents/skill-repos/benpham3206__principles; "
    f"if [ -d $R ]; then U=$(git -C $R remote get-url origin) || exit 1; [ \"${{U%.git}}\" = {ORIGIN} ] || {{ echo \"$R pulls from $U\"; exit 1; }}; "
)
POSIX_CLEAN = (
    "S=$(git --no-optional-locks -C $R status --porcelain --untracked-files=all) || exit 1; "
    "[ -z \"$S\" ] || { echo \"$R has local changes\"; exit 1; }; "
)
POSIX_AHEAD = (
    "A=$(git -C $R rev-list origin/main..HEAD) || exit 1; "
    "[ -z \"$A\" ] || { echo \"$R has local commits\"; exit 1; }; "
)
POSIX_UPDATE = POSIX_ORIGIN + POSIX_CLEAN + "git -C $R fetch -q origin main || exit 1; " + POSIX_AHEAD + (
    f"git -C $R merge -q --ff-only origin/main || exit 1; else git clone -q {ORIGIN} $R || exit 1; fi; "
    "P=/opt/homebrew/bin/python3; [ -x $P ] || P=python3; "
    "$P $R/install.py --pull"
)
POSIX_CHECK = POSIX_ORIGIN + POSIX_CLEAN + POSIX_AHEAD + "else echo \"no clone at $R\"; exit 1; fi; " + (
    "P=/opt/homebrew/bin/python3; [ -x $P ] || P=python3; "
    "$P $R/install.py --check"
)
WINDOWS_ORIGIN = (
    "$R = \"$HOME\\.agents\\skill-repos\\benpham3206__principles\"; "
    "if (Test-Path $R) { "
    "$U = git -C $R remote get-url origin; if ($LASTEXITCODE) { exit 1 }; "
    f"$U = $U -replace '\\.git$',''; if ($U -ne '{ORIGIN}') {{ Write-Output \"$R pulls from $U\"; exit 1 }}; "
)
WINDOWS_CLEAN = (
    "$S = git --no-optional-locks -C $R status --porcelain --untracked-files=all; if ($LASTEXITCODE) { exit 1 }; "
    "if ($S) { Write-Output \"$R has local changes\"; exit 1 }; "
)
WINDOWS_AHEAD = (
    "$A = git -C $R rev-list origin/main..HEAD; if ($LASTEXITCODE) { exit 1 }; "
    "if ($A) { Write-Output \"$R has local commits\"; exit 1 }; "
)
WINDOWS_UPDATE = WINDOWS_ORIGIN + WINDOWS_CLEAN + (
    "git -C $R fetch -q origin main; if ($LASTEXITCODE) { exit 1 }; "
) + WINDOWS_AHEAD + (
    "git -C $R merge -q --ff-only origin/main; if ($LASTEXITCODE) { exit 1 } } "
    f"else {{ git clone -q {ORIGIN} $R; if ($LASTEXITCODE) {{ exit 1 }} }}; "
    "python \"$R\\install.py\" --pull"
)
WINDOWS_CHECK = WINDOWS_ORIGIN + WINDOWS_CLEAN + WINDOWS_AHEAD + (
    "} else { Write-Output \"no clone at $R\"; exit 1 }; "
    "python \"$R\\install.py\" --check"
)
# Every child process gets a deadline (seconds), so one stalled machine cannot block the rest.
GIT_TIMEOUT = 120
STEP_TIMEOUT = 600


def run(cmd: list[str], timeout: int, *, input: str | bytes | None = None,
        capture_output: bool = False, text: bool = False) -> subprocess.CompletedProcess:
    """Run cmd with a deadline. Returns a CompletedProcess like subprocess.run.

    Guarantee: run returns within about timeout + 15 s. Captured output and input go through
    temporary files, never pipes, so a grandchild holding an inherited handle cannot keep it
    waiting (git-remote-https did exactly that to subprocess.run on Windows). The child runs
    in its own process group (a new session on POSIX); on timeout or interrupt the whole
    group is ended (SIGTERM, then SIGKILL; taskkill /T /F on Windows), and a timeout returns
    code 124 with whatever was captured plus a stderr line naming the timeout. Captured
    text is decoded as subprocess.run decodes it, except that undecodable bytes are replaced.

    Known limits: a process that leaves the group (setsid, a detached git gc) survives, and
    so does one left behind by a child that exited on time. On Windows, taskkill /T finds
    descendants through living parents only, so one whose parent already exited survives (a
    Job Object would close that gap). A survivor still writing to the output files can
    garble the captured text; the read stops at the size the file had when reading began.
    Work started elsewhere, such as a command already running on a remote machine over SSH,
    may keep going; check before retrying. The child has no controlling terminal on POSIX,
    so it cannot prompt there.
    """
    with tempfile.TemporaryFile("w+" if text else "w+b") as inp, tempfile.TemporaryFile() as out, \
            tempfile.TemporaryFile() as err:
        if input is not None:
            inp.write(input)
            inp.flush()
            inp.seek(0)
        sinks = {"stdout": out, "stderr": err} if capture_output else {}
        group = {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP} if WIN else {"start_new_session": True}
        proc = subprocess.Popen(cmd, stdin=inp if input is not None else None, **sinks, **group)
        try:
            code = proc.wait(timeout)
        except subprocess.TimeoutExpired:
            end_tree(proc)
            code = None
        except BaseException:
            end_tree(proc)
            raise
        stdout, stderr = (decoded(out, text), decoded(err, text)) if capture_output else (None, None)
    if code is not None:
        return subprocess.CompletedProcess(cmd, code, stdout, stderr)
    line = f"timed out after {timeout} s: {' '.join(cmd[:3])}"
    if not capture_output:
        return subprocess.CompletedProcess(cmd, 124, "", line)
    if stderr and not stderr.endswith("\n" if text else b"\n"):
        line = "\n" + line
    return subprocess.CompletedProcess(cmd, 124, stdout, stderr + (line if text else line.encode()))


def decoded(f, text: bool) -> str | bytes:
    """Everything written to f. As text: locale encoding and newlines, as subprocess.run decodes,
    except that undecodable bytes (half a character from a killed writer) become U+FFFD."""
    size = os.fstat(f.fileno()).st_size  # a snapshot: a survivor still writing cannot extend the read
    f.seek(0)
    data = f.read(size)
    return io.TextIOWrapper(io.BytesIO(data), errors="replace").read() if text else data


def end_tree(proc: subprocess.Popen) -> None:
    """End proc and every process in its group. Bounded: returns within about 15 s."""
    if WIN:
        try:
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)], timeout=10,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except (OSError, subprocess.TimeoutExpired):
            pass
        proc.kill()
    else:
        for sig, grace in ((signal.SIGTERM, 2), (signal.SIGKILL, 3)):
            try:
                os.killpg(proc.pid, sig)
            except (ProcessLookupError, PermissionError):
                pass
            try:
                proc.wait(grace)
            except subprocess.TimeoutExpired:
                pass
    try:
        proc.wait(3)
    except subprocess.TimeoutExpired:
        pass


def git(*args: str) -> subprocess.CompletedProcess:
    return run(["git", "-C", str(CLONE), *args], GIT_TIMEOUT, capture_output=True, text=True)


def skills(root: Path) -> list[str]:
    """Skill folder names under root/skills: every folder holding a SKILL.md."""
    base = root / "skills"
    return sorted(p.name for p in base.iterdir() if (p / "SKILL.md").is_file()) if base.is_dir() else []


def same_path(a: Path, b: Path) -> bool:
    return os.path.normcase(os.path.realpath(a)) == os.path.normcase(os.path.realpath(b))


def make_link(target: Path, source: Path) -> None:
    if WIN:
        import _winapi  # junctions need no admin rights or developer mode
        _winapi.CreateJunction(str(source), str(target))
    else:
        target.symlink_to(source, target_is_directory=True)


def link(name: str, check: bool) -> str:
    """Link ~/.agents/skills/<name> to the clone. Returns ok, linked, missing, or conflict."""
    target, source = AGENT_SKILLS / name, CLONE / "skills" / name
    if os.path.lexists(target):
        return "ok" if same_path(target, source) else "conflict"
    if check:
        return "missing"
    AGENT_SKILLS.mkdir(parents=True, exist_ok=True)
    make_link(target, source)
    return "linked"


def stale(names: list[str]) -> list[str]:
    """Links in ~/.agents/skills that point into the clone at a skill that no longer exists."""
    if not AGENT_SKILLS.is_dir():
        return []
    root = os.path.normcase(os.path.realpath(CLONE / "skills"))
    out = []
    for entry in sorted(AGENT_SKILLS.iterdir()):
        real = os.path.normcase(os.path.realpath(entry))
        if os.path.dirname(real) == root and entry.name not in names:
            out.append(entry.name)
    return out


def is_link(path: Path) -> bool:
    """True for a symlink or a Windows junction (os.readlink reads both)."""
    try:
        os.readlink(path)
        return True
    except (OSError, ValueError):
        return False


def remove_link(path: Path) -> None:
    """Remove the link itself, never what it points at."""
    if WIN:
        os.rmdir(path)  # removes a junction or directory symlink, not its target's contents
    else:
        os.unlink(path)


def load_fanout():
    """agent-hooks' fanout.py when installed, else the built-in copy of its harness map."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("fanout", FANOUT if FANOUT.is_file() else BUILTIN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def harness_folders(folders: list[Path], check: bool) -> int:
    """Create each missing folder whose harness is installed. Returns how many were (or would be) made.

    A harness counts as installed when its own folder exists: the first folder under HOME, or the
    first two under ~/.config, which most machines have whatever harnesses they run. A fresh install
    often lacks the skills or rules folder the harness reads; without this it would get nothing.
    """
    missing = []
    for d in folders:
        try:
            parts = d.relative_to(HOME).parts
        except ValueError:
            continue
        root = HOME.joinpath(*parts[:2 if parts[0] == ".config" else 1])
        if root.is_dir() and root != d and not d.is_dir():
            missing.append(d)
    for d in missing:
        print(f"{'missing' if check else 'created':<8} {d}")
        if not check:
            d.mkdir(parents=True, exist_ok=True)
    return len(missing)


def policy(check: bool) -> int:
    """Write policy.md as one managed block into every harness instruction file. Returns drift."""
    src = CLONE / POLICY
    if not src.is_file():
        print(f"skip     no {POLICY} in {CLONE}")
        return 0
    fo = load_fanout()
    body = src.read_text(encoding="utf-8").strip()
    source = f"~/.agents/skill-repos/benpham3206__principles/{POLICY}"
    # An installed harness gets its instruction file even when it has none yet. Grok is left out: it
    # reads the policy from ~/.grok/rules, and a second copy in ~/.grok/AGENTS.md would double it.
    targets = [(h, p, "" if head is None and h in CREATE_IF_MISSING else head)
               for h, p, head in fo.instruction_targets(POLICY_TAG, POLICY_TITLE)]
    # Installed agent-hooks may still supply legacy names and Cursor frontmatter.
    targets = [(h, p.with_name(f"managed-{POLICY_TAG}.mdc") if h == "cursor" else p,
                f"---\ndescription: {POLICY_TITLE}\nalwaysApply: true\n---\n\n" if h == "cursor" else head)
               for h, p, head in targets]
    targets.append(("grok-rules", HOME / ".grok" / "rules" / f"managed-{POLICY_TAG}.md", ""))
    targets.append(("hermes", HERMES / "references" / "engineering-policy.md", ""))
    made = harness_folders([p.parent for h, p, _ in targets if h not in ("canonical", "hermes")], check)
    from harnesses import install_rule
    drift = (made if check else 0) + install_rule(POLICY_TAG, body, source, targets, check)
    return drift + install_rule(POLICY_TAG, HERMES_POINTER, source, [("hermes", HERMES / "SKILL.md", None)], check)


def harness_dirs() -> list[Path]:
    """The harness skill folders fanout.py links into, read from fanout.py itself."""
    return [Path(d) for d in getattr(load_fanout(), "SKILL_DIRS", [])]


def prune(names: list[str], check: bool) -> list[Path]:
    """Links this installer made for skills the clone no longer has (after a rename or removal).

    Removes only links: the harness link to ~/.agents/skills/<name>, then that link into the
    clone. A real folder is never touched. Returns what was (or, with check, would be) removed.
    """
    gone = stale(names)
    if not gone:
        return []
    out = []
    dirs = harness_dirs()
    for name in gone:
        ours = AGENT_SKILLS / name
        for d in dirs:
            entry = d / name
            if os.path.lexists(entry) and is_link(entry) and same_path(entry, ours):
                out.append(entry)
        if is_link(ours):
            out.append(ours)
    if not check:
        for path in out:
            remove_link(path)
    return out


def fanout(name: str, check: bool) -> tuple[int, list[str]]:
    """Link one skill into every present harness. Returns an exit code and the lines worth showing.

    With agent-hooks installed, its fanout.py runs, including its skill scan. Without it, the
    built-in harness map links the skill directly.
    """
    if FANOUT.is_file():
        cmd = [sys.executable, str(FANOUT), "skill", name] + (["--check"] if check else [])
        done = run(cmd, STEP_TIMEOUT, capture_output=True, text=True)
        code, out = done.returncode, (done.stdout or "") + (done.stderr or "")
    else:
        import contextlib
        fo, buf = load_fanout(), io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = 1 if fo.link_skill(name, fo.SKILL_DIRS, check, AGENT_SKILLS) else 0
        out = buf.getvalue()
    lines = [ln for ln in out.splitlines() if ln.split() and ln.split()[0] not in ("ok", "skip")]
    return code, lines


def pull() -> int:
    """Clone if absent, else fast-forward from ORIGIN. Refuses a clone pointing anywhere else."""
    if not CLONE.exists():
        CLONE.parent.mkdir(parents=True, exist_ok=True)
        done = run(["git", "clone", "-q", ORIGIN, str(CLONE)], GIT_TIMEOUT, capture_output=True, text=True)
        if done.returncode:
            print(f"install.py: clone failed: {done.stderr.strip()}", file=sys.stderr)
            return 1
        print(f"cloned   {ORIGIN} at {git('rev-parse', '--short', 'HEAD').stdout.strip()}")
        return 0
    url = git("remote", "get-url", "origin").stdout.strip().rstrip("/")
    if url.removesuffix(".git") != ORIGIN:
        print(f"install.py: {CLONE} pulls from {url}, not {ORIGIN}; refusing", file=sys.stderr)
        return 1
    before = git("rev-parse", "--short", "HEAD").stdout.strip()
    # Untracked files count, whatever git config says: an untracked skill folder would be
    # installed like a real one. Ignored files do not (see the known limits above).
    status = git("status", "--porcelain", "--untracked-files=all")
    if status.returncode or status.stdout.strip():
        print(f"install.py: {CLONE} has local changes or git failed; refusing", file=sys.stderr)
        return 1
    fetched = git("fetch", "-q", "origin", BRANCH)
    if fetched.returncode:
        print(f"install.py: fetch failed: {fetched.stderr.strip()}", file=sys.stderr)
        return 1
    ahead = git("rev-list", f"origin/{BRANCH}..HEAD")
    if ahead.returncode or ahead.stdout.strip():
        print(f"install.py: {CLONE} has local commits not on origin, or git failed; refusing", file=sys.stderr)
        return 1
    done = git("merge", "-q", "--ff-only", f"origin/{BRANCH}")
    if done.returncode or git("rev-parse", "HEAD").stdout != git("rev-parse", f"origin/{BRANCH}").stdout:
        print(f"install.py: could not fast-forward to origin: {done.stderr.strip()}", file=sys.stderr)
        return 1
    after = git("rev-parse", "--short", "HEAD").stdout.strip()
    print(f"updated  {before} -> {after}" if before != after else f"current  {after}")
    return 0


def install(check: bool) -> int:
    if not CLONE.is_dir():
        print(f"install.py: no clone at {CLONE}; run with --pull", file=sys.stderr)
        return 1
    print(f"harnesses {FANOUT if FANOUT.is_file() else BUILTIN}")
    names = skills(CLONE)
    worst = 1 if harness_folders(harness_dirs(), check) and check else 0
    for name in names:
        state = link(name, check)
        if state == "conflict":
            print(f"CONFLICT {AGENT_SKILLS / name} is not a link to this clone; left as is")
            worst = 1
            continue
        if state != "ok":
            print(f"{state:<8} {AGENT_SKILLS / name}")
            worst = worst or (1 if check else 0)
        if state == "missing":
            continue
        code, lines = fanout(name, check)
        for ln in lines:
            print(f"[{name}] {ln}")
        worst = worst or code
    for path in prune(names, check):
        print(f"{'stale' if check else 'pruned':<8} {path} (link to a skill the repo no longer has)")
        worst = worst or (1 if check else 0)
    if policy(check):
        worst = 1
    print(f"{'checked' if check else 'installed'} {len(names)} skills and {POLICY}: {'drift' if worst else 'ok'}")
    return worst


def aliases() -> list[str]:
    """FLEET aliases present in this machine's ~/.ssh/config."""
    try:
        cfg = (HOME / ".ssh" / "config").read_text(encoding="utf-8", errors="replace").lower()
    except OSError:
        return []
    hosts = {w for ln in cfg.splitlines() if ln.strip().startswith("host ") for w in ln.split()[1:]}
    return [a for a in FLEET if a in hosts]


def update_remote(alias: str, check: bool = False) -> int:
    windows = alias == "windows"
    script = (WINDOWS_CHECK if check else WINDOWS_UPDATE) if windows else (POSIX_CHECK if check else POSIX_UPDATE)
    if alias in REMOTE_PY_TARGETS and REMOTE.is_file():
        cmd = [sys.executable, str(REMOTE), alias, "--timeout", str(STEP_TIMEOUT)]
    else:
        shell = "powershell -NoProfile -Command -" if windows else "zsh -l"
        cmd = ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=10", alias, shell]
    print(f"# {alias}", flush=True)
    done = run(cmd, STEP_TIMEOUT + 60, input=script, text=True)
    if done.returncode == 124 and done.stderr:
        print(f"install.py: {alias}: {done.stderr}", file=sys.stderr)
    return done.returncode


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true", help="dry run; exit 1 on drift")
    ap.add_argument("--pull", action="store_true", help="fast-forward the clone first")
    ap.add_argument("--all", action="store_true", help="update this machine, then every other one")
    args = ap.parse_args(argv)
    if (args.pull or args.all) and not args.check:
        if pull():
            return 1
        # Run the freshly pulled installer, not this one, so a new install.py takes effect now.
        code = run([sys.executable, str(CLONE / "install.py")], STEP_TIMEOUT).returncode
    else:
        # --check is a dry run everywhere: no pull, no writes, here or on the other machines.
        code = install(args.check)
    if args.all:
        for alias in aliases():
            code = update_remote(alias, args.check) or code
    return code


if __name__ == "__main__":
    raise SystemExit(main())
