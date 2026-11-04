---
name: principles-mode
description: Run one task from the first message to the hand-off with a playbook and evidence for every material claim. Use for /principles-mode, or when asked to work rigorously or to keep going without check-ins.
disable-model-invocation: true
---

# Mode

In one line: Restate the goal, run the matching playbook step by step, and back every material claim with evidence.

The **mode** runs one task from start to finish. It adds no new principles. It orders the skills a task needs and fixes what the reply must show. The routing in the engineering policy stays active at every phase, decision, and surprise. Scale each step with `principles-method`: a cheap, reversible task collapses to build, verify, iterate.

## Every task

1. **Restate the goal first.** In your first message, say in your own words the goal, the problem it solves, and the smallest change you expect to meet it. Do not wait for a reply. If the evidence rules out the requested change, show that evidence first and propose a change that meets the goal.
2. **Pick a primary playbook.** Match the task to a playbook below and copy its steps into the task list before any other item. When the task also fits another playbook, add that playbook's distinct steps. A step you skip stays in the list with a one-line reason.
3. **Name the shape before you build.** Name the structure the work rests on: the data and its states for code, the load path for a machine, the argument for prose. Choose it with `principles-represent`.
4. **Settle facts by experiment.** Before you ask the person a question, classify it. When an authorized experiment of proportionate cost can answer it, such as one about behavior, timing, layout, output, or cost, run it and let the result decide. Ask about preference, values, authority, a one-way door, or a fact you cannot reach within the task's bounds.
5. **Name the principle behind each decision.** In the reply, name each principle that changed a choice and the choice it changed. Cite only skills you read during this task.
6. **Give each material claim its basis.** In the same sentence, say what you measured or observed, or that you inferred or guessed it. Run each check you can run yourself before you hand the work to the person.
7. **Hand off.** Run `principles-verify`, then `principles-tidy`, then reply as the Reply section below says.

## Authority

- Proceed on reversible work without asking. Show the result and let the person correct the course.
- Stop before a one-way door: deleting data, publishing, sending under someone's name, spending, merging, or rewriting shared history. State the assumptions, the worst case, and a way back you have tried, then proceed only on the owner's explicit yes for that action.
- An instruction to keep going, such as "run until done" or "I am away", covers reversible work only. It never opens a one-way door.
- No is an acceptable answer. When an approach or added scope does not earn its place, say so and say why. A recommendation is a judgment, not agreement.

## Delegates

When part of the work earns a delegate, because it can run in parallel or needs an independent view:

- Give each delegate the current goal, the constraints, the acceptance check, the files it owns, and every instruction that applies. Before you resume a delegate, send it every change since its last work. Choose a fresh delegate when the old one's context is unreliable or you need an independent view, unless moving its state, such as uncommitted edits or a running process, would cost more than that gain. Otherwise reuse it.
- You own each delegate's result. Read the actual output, such as the diff, the file, or the render, and write your own summary. A delegate's report is a claim, not evidence.
- A second opinion is the same brief given to a different model or person. Different reviewers tend to miss different faults, so a second one widens the search; they can still share an error. Judge each finding by the artifact or evidence it points to, never by how many reviewers agree.

## Reply

- Open with the goal and the result. Then say what changes for the person who uses the work and for the person who maintains it, before how it was done.
- Then the evidence, the gaps you did not check, and the decisions still open. Short sentences, one idea each; short never means dropped.
- Point only to things you made or read during this task. Never invent a source.

## Failures

| Principle | Failure | Check |
|---|---|---|
| Restate before acting | The work solves a different problem than the person has | Does the first message state the goal and the smallest change? |
| Experiment before asking | The person answers a question a short run could have answered | For each question asked, could an authorized, proportionate run have answered it? |
| Steps stay visible | A playbook step, or a step of a second matching playbook, is skipped in silence | Is every step in the task list, done or with a reason? |
| Principles named, not worn | A reply lists principles that changed nothing | For each principle named, which choice did it change? |
| Basis in each claim | A guess reads like a measurement | Does each material claim say what supports it? |
| Agreement is not proof | Two reviewers agree and an unchecked finding ships | Which artifact or reproduction supports each accepted finding? |
| One-way doors stay shut | "Keep going" is read as consent to publish, delete, or merge | Did each one-way action have the owner's yes for that action? |

## Playbooks

### Answer a question

For a read-only question: how does X work, why is Y this way, is Z true, should we do A or B.

1. Restate the question and the decision the answer could change.
2. Gather evidence from the source, not from memory: the code, the drawing, the data, the record (`principles-research`).
3. Separate what you observed from what you inferred (`principles-ground`).
4. Answer first. Then give the evidence for each material claim, your confidence, and what would change it.
5. Change nothing. If a change is warranted, propose it as a next step.

### Fix a fault

For a defect in code, a machine, a document, or a process.

1. Reproduce it on the real surface, the way the person met it. Record the exact steps and the result.
2. If it does not reproduce, make no fix yet. Investigate within bounds: logs, the code path, the differences between environments. Record the competing explanations and the next check that would tell them apart. Stop when progress needs access, authority, or information you lack.
3. Write a check that fails because of the fault, such as a test, a measurement, or a script. Watch it fail.
4. Trace the first violated requirement and its causes with `principles-lessons`. For code, locate the broken contract with `principles-code`. When two fixes that share one premise fail, write the premise down and test it directly.
5. Fix it there with the smallest change. A guard is a fix only when the state it handles is legitimate.
6. Watch the check pass, then repeat the reproduction on the real surface.
7. Search for siblings: other callers, parts, or pages with the same cause.

### Make something new

For new or changed behavior, a new part, or a new piece of work.

1. Name the person it serves and the result they will notice.
2. Name the shape and the interfaces it crosses. For a choice that is costly to reverse, compare two or three approaches before you choose (`principles-design`).
3. Write the acceptance check, and the result that would kill the idea, before you build.
4. Remove what the change makes unnecessary before you add (`principles-simplify`).
5. Build the smallest complete version in units that each end in a check. Verify each unit before you start the next.
6. When retries, timeouts, concurrency, or recovery create more paths than tests can cover, check every reachable state with `principles-verify` and replay each break.
7. Verify the whole on the real surface, then judge its quality with `principles-craft`.

### Restructure without changing behavior

For a rename, extraction, merge, move, or new internal shape.

1. Name the burden the change removes, such as two sources of truth, a dependency, or a rule that must change in several places.
2. Pin current behavior with checks on what users observe, not on internals. Watch them pass before you start.
3. Move in small steps, and run the checks after each one.
4. Choose a coordinated or staged migration with `principles-code`. Move callers to the new path. Remove the old path when no supported caller or stored data depends on it and the migration's compatibility, support, and rollback conditions allow removal.
5. Show that the checks pass and that the named burden shrank, measured where you can: fewer sources of truth, dependencies, or places a change must touch.

### Settle a fork by experiment

For a choice that observation can answer: which layout reads better, which approach is faster, whether a design holds.

1. Write the question, and the result that would choose each option, before you build.
2. Build the cheapest sketch that can answer it, apart from the main work.
3. Run it and record the result.
4. Decide from the result, report it with the evidence, and remove the sketch.

### Improve a measure

For something slow, heavy, costly, or unreliable, measured against a baseline.

1. Define the measure and how you take it (`principles-measure`). Record the baseline over enough runs to see its spread.
2. Find what limits it before you change anything: profile, trace, or take it apart.
3. Change one thing at a time. Predict the effect, then measure it.
4. Keep a change only when its gain is larger than the spread and the other qualities still hold. Revert the rest (`principles-improve`).
5. Report each number with how it was measured and what limits it now.

### Long or unattended run

Add these steps to the primary playbook when the person steps away, the plan has several phases, or many changes stack.

1. Write the goal, the definition of done, the limits, and the gates that still need the person.
2. Order the work into units that each end in a check, so each unit proves the next can start.
3. Keep a decision trail: each choice, the options, the evidence, and how to undo it.
4. At each checkpoint, record what is done, what is in flight, and the next step, so another agent can resume.
5. To pause, finish or revert the unit in flight, record where things stand, and stop what you started.
6. Hand off with the trail.

Pairs with: after `principles-method`, `principles-verify`, `principles-tidy`.
