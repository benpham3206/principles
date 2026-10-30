---
name: principles-tidy
description: Close agent work with safe cleanup, accurate dependency and architecture docs, and discoverable tools. Use at task close or handoff, including when no cleanup tool is installed.
---

# Tidy

In one line: Leave the next person a clean workspace, accurate docs, findable tools, and the evidence to continue.

Leave the next person a usable workspace, accurate documentation, discoverable tools, and the evidence needed to continue. Apply this to the work being closed. A dedicated cleanup tool is optional.

## Establish ownership

Read project instructions, the task record, current changes, and any recorded starting state. Identify the files, processes, branches, worktrees, dependencies, and documents the task reached. Use recorded commands or direct evidence to establish ownership. A name or recent timestamp alone is insufficient.

Keep deliverables, verification evidence, rollback material still needed, and work required to resume. Preserve other people's edits and resources. When ownership or retention is uncertain, leave the item in place and report the uncertainty. A clean version-control status is not a reason to discard work.

## Close the task

1. Inspect any existing cleanup workflow before using it. Prefer its inspection mode and check the exact targets and effects against this task's authority. Use the steps below directly when the tool is absent or its scope is broader than the task. No installation is required.
2. Account for every resource the task acquired, such as temporary files, generated output, downloads, logs, backups, accounts, reservations, and permissions, including those outside the repository. Keep each item that still serves a named purpose. Move obsolete files and folders to the platform's recoverable Trash; use the project-approved recoverable method when Trash is unavailable. If recovery is unavailable, retain the item and report it. Do not bypass a deletion guard.
3. Check each process the task started by its current identity and workspace. Stop only processes proven to belong to this task, using a graceful stop with a timeout. Recheck that it stopped. Retain a service needed for handoff and state who will stop it. Avoid broad process-name termination.
4. Inspect branches and worktrees the task created. Keep active checkouts and any uncommitted, untracked, or unpushed work. Retire a checkout or branch only with task authorization, proof its work is preserved, and a recoverable method. Leave a candidate for the owner when those conditions are absent.
5. Reconcile dependencies, architecture, and tool discovery as below. Fix discrepancies introduced by the task. Record unrelated gaps for later work. Keep the pass within the task's scope; a cleanup request supplies no authority to merge, publish, install a skill, or discard tracked edits.
6. Run the project's verify command and the checks needed for the cleanup or documentation changes. Inspect the remaining diff, resources, and references. Confirm retained evidence and recovery material still exist. If a check cannot run, report the gap and reason.
7. Leave a short record in the project's existing task or change record. Name what was removed, retained, or left unresolved, and link to the updated docs and verification evidence. Include the tool report below. Reuse an existing record rather than creating a second ledger. Report remaining owner actions.

## Dependencies

Reconcile every declared relationship with actual use. In code, compare changed dependency declarations and lockfiles with actual imports, build setup, runtime loading, and external services. Account for dependencies added, removed, or changed by the task, including optional and indirect uses. An absent text match alone does not prove a dependency is unused.

Use manifests and lockfiles as the authority for exact versions. Keep documentation focused on purpose, required setup, system prerequisites, and relevant limits. Correct stale setup commands and links. Change declarations only when the discrepancy is supported by evidence and within scope. Use the project's package manager to keep related files consistent; retain unrelated versions.

## Architecture

Trace the changed path from its entry point through module responsibilities, dependency direction, external boundaries, and stored state. Check failure and recovery paths where the change affects them. Compare those facts with the existing architecture notes, file map, and diagrams.

Update the nearest authoritative document when a responsibility, interface, dependency, or operational assumption changed. Include the reason for a non-obvious boundary. Link to code or declarations for details that would otherwise drift. Create a small architecture note only when a durable fact has no suitable home. Resolve a disagreement from the implementation and evidence; mark intended future structure as a proposal.

## Tool discovery

Identify useful tools created, found, or repeatedly used during the task. Check whether a fresh agent can find them from the project's normal entry point. A tool that exists only in the transcript or behind a path nobody reads is still hidden.

For each tool worth retaining, update the existing agent entry point or reachable tool index with a short pointer: when to use it, its canonical location, and a working invocation. Put prerequisites, inputs, outputs, side effects, and limits in the linked tool documentation or help. Use paths relative to the project when practical. Keep operational tool details with the project rather than embedding them in general Principles skills.

Keep the entry point brief and put each fact in one place. For example, a pointer might read: "Before changing a dependency, run `python3 tools/dependency_report.py --help`; usage and output are in `tools/README.md`." The example is a shape, not a required tool or command.

Check discovery from the same entry documents a fresh agent receives, without relying on the task transcript. Follow the pointer to the tool and perform a safe documented operation. Report when only the documentation path was checked or execution requires further authority. Preserve meaningful output as evidence and keep credentials out of the record.

Use `principles-create` to assess a repeated workflow that may deserve a Principles skill. Create or install one only within the authorized scope. Use `principles-measure` when a claim about tool speed, cost, reliability, or ease of use needs measurement. A tool being used often does not establish that it improves the result.

## Tool report

Briefly name the material tools actually used across the task and this cleanup, including tools the agent created. State each tool's purpose, observed result or limitation, and evidence location. Distinguish tools used from tools merely found or proposed. Group repeated calls by tool; a call transcript is unnecessary.

Say what became easier to find: name the tool, the entry point changed, and the working invocation or linked help. State whether fresh-context discovery was exercised or only inspected. Link any skill authoring work and measurement record when present. This report documents observed use; it supplies no authority for another action.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Ownership before removal | Cleanup destroys another task's work or an active recovery path | For each target, what proves ownership and that its purpose has ended? |
| Evidence outlives cleanup | The result remains but nobody can verify or resume it | Open the retained proof and resume record after the cleanup |
| Documentation follows reality | Dependencies or boundaries changed while instructions describe the old system | Trace the changed path and follow each affected setup instruction and reference |
| One source per fact | A second inventory or diagram starts to disagree with the first | Does each repeated detail belong as a link to its authority? |
| Useful tools remain reachable | The next agent rebuilds a tool because it cannot find the existing one | Starting with the normal entry documents alone, can a fresh agent find the tool and perform a safe documented operation? |
| Bounded completion | A closeout pass grows into a repository rewrite | Can every change be traced to the task being closed? |
| Record each resource's owner and expiry when it is acquired, so the claims of an actor that crashes lapse | Orphans pile up, and nobody can safely reclaim them | For each resource, who owns it, when does the claim lapse, and what reclaims it? |

## Completion

Every identified task artifact has a known disposition. Cleanup has preserved the work, its proof, and the needed recovery path. Dependency and architecture documentation match the changed system. Useful retained tools have a reachable entry point, and their actual use is reported. Report checks that passed and gaps that remain. Retained work can be the correct result.

Pairs with: before `principles-verify`, `principles-secure`; after `principles-create`, `principles-measure`, `principles-code`, `principles-integrate`, `principles-compound`.
