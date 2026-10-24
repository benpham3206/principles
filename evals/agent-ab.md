# Agent A/B eval: lessons for a rerun

Question: does a coding agent do better work on real repositories with the principles skills and policy installed than without, and at what cost in time and tokens? A first attempt with gpt-6-luna (Codex CLI) built the harness and ran 30 tasks, then stopped before grading. This file keeps what a rerun needs.

## Design that held

- Two arms, same model, effort, prompt, snapshot, and sandbox. The with arm installs principles into a blank home with `install.py`, which doubles as a fresh-machine install test.
- Tasks come from real commits so the ground truth is real: a coding task with hidden tests from the upstream fix, code reviews of a real change with seeded defects, a pull request description for a real branch, and a new strict lesson checked by the repository's verifier.
- Snapshots are a fresh repository built from `git archive`, so the agent cannot read the answer in the history.
- Blind grading: arm names, skill names, and the policy heading are redacted before a grader sees the output.
- A probe before any task run: ask each arm what it sees. This caught the isolation failure below before it cost a full run.

## What broke, and the check that now catches it

| Cause | Check |
|---|---|
| Codex on Windows reads skills from the real user profile even when HOME, USERPROFILE, and CODEX_HOME point to a temp home, so the control arm saw principles | Before every run, render what the model will see with `codex debug prompt-input hi` and refuse to start unless the without arm shows no principles skill and no policy, and the with arm shows both. A temp HOME isolates on macOS; on Windows use WSL or another machine |
| `git archive` on Windows applies `core.autocrlf`, so a snapshot used on macOS showed every file modified and a review diff of 12,000 lines | Run git with `core.autocrlf=false`, record `git status --short` for each snapshot, and refuse to start a run whose tree differs |
| A file-writing tool on Windows saved prompts and briefs as UTF-16, and one reached a model as the single letter R | Check the bytes of every file a tool creates before a program reads it; `test_skills.py` rejects NUL bytes in tracked markdown |
| A sandboxed delegate could not reach the network, so it could not launch the agent runs it was asked to run | Delegates write and test code; the parent runs anything that calls a model or the network |
| A delegate reported isolation fixed from evidence that did not hold | Verify each delegate result yourself before using it |
| Building a snapshot into an existing folder silently reverted its files | Build into a new folder only |

## Ground truth to fix before grading

- A seeded defect must be a real defect. One seed removed an identity check that the code made redundant: the cache held the image strongly, so its address could not be reused. Read the surrounding code before choosing a seed.
- Validate each grader against the reference answer. The upstream fix for the coding task also updated two test fixtures, so a grader that restores the original fixtures fails the reference itself.
- Choose tasks that reproduce on the machine that runs them. A Windows-only decode error does not reproduce on macOS or Linux.

## Observed before stopping (not graded)

All 30 runs (5 tasks, 2 arms, 3 repeats) completed. The with arm opened 4 to 10 principles skills in all but one run, and used about 1.0 to 2.6 times the input tokens of the without arm. In the pilot, both arms found the same two real defects in one review. Quality was never graded, so these runs say nothing yet about whether principles helps.
