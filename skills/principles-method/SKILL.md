---
name: principles-method
description: Scale the work to its consequences. Use when planning a task, making a decision, choosing rigor, managing long-running or delegated work, or setting up how a project works.
---

# Method

In one line: Match effort to the cost of a mistake, and delete needless work before you optimize or automate it.

The **method** is a cycle: plan the work, build a version, check it, and refine it. Match the effort to the cost of a mistake. Keep earlier choices easy to change.

## Gate: how much rigor

Rate the task on three things: **consequence** (what a mistake costs), **uncertainty** (how much is unknown), and **irreversibility** (how hard it is to undo).

| Situation | Move |
|---|---|
| Cheap, reversible | Move fast: build, verify, iterate |
| Strong evidence, reversible | Just execute |
| High uncertainty, cheap experiment | Experiment first |
| Expensive, irreversible | Investigate deeply before acting |
| High uncertainty, irreversible | Do not guess. Reduce the uncertainty first |

Investigate an uncertainty when the answer could change an important decision. Use `principles-ground` to choose what to learn and when to stop. Use the same risk assessment to choose how much to spend on preventing, detecting, and recovering from failure (`principles-reliability`).

Weigh expected benefit, information gained, downside, and reversibility. These are considerations, not quantities to add without a common scale.

## Plan

For consequential or uncertain work. Skip or compress it when the work is clear, cheap, and reversible.

1. **Intent**: why. Ask the 5W1H: what, why, who, when, where, how.
2. **Goal**: what, and the definition of done. Define success, constraints, and failure conditions before building.
3. **Metrics**: how you will know. Use `principles-measure` to define quantities and check the measurement method before building a tool.
4. **Constraints**: what cannot be violated. Name them before choosing tools. Language, framework, storage, and infrastructure are downstream choices; revisit them only when evidence shows a constraint or bottleneck changed.
5. **Assumptions and dependencies**: what depends on what, and why. Mark each as fact, assumption, estimate, or decision.
6. **First principles**: what is actually necessary (see `principles-ground`).
7. **Design**: choose a coherent approach with `principles-design`. Make the form, behavior, and construction concrete enough to check the consequential choices.
8. **Consequences**: second-order and later effects, and the worst credible outcome (see `principles-horizons`). To find what the plan hides, work backward from the finished outcome and design its failure (see `principles-invert`). Think bigger than the brief. What ultimately matters is the problem solved and the joy of the person at the end.

## Build

1. Question each requirement, boundary, and dependency.
2. Delete what does not need to exist.
3. Merge unneeded boundaries; keep useful modularity (see `principles-integrate`).
4. Simplify before optimizing (see `principles-simplify`).
5. Split the work into subsystems and modules. Define each interface's inputs, outputs, guarantees, and failure modes. Order the work by its dependencies and critical path, then join the parts in small steps (`principles-integrate`).
6. Verify against goal, constraints, and metrics (see `principles-verify`).
7. Stress test where failure matters. Anticipate bad actors, edge cases, and the worst case.
8. Optimize measured bottlenecks only.
9. Shorten the feedback loop between a change and learning whether it worked.
10. Automate only understood, stable, repeated work.

Steps 2, 4, and 8 to 10 are the improvement order; `principles-improve` covers it in depth.

For small reversible tasks this collapses to build, verify, iterate.

## Execution limits

For work that can block, stall, or run in the background:

| Principle | Failure | Check |
|---|---|---|
| Bound each wait | A network call, remote machine, model call, server start, or health check hangs the task | Give it a timeout and name the response when it expires |
| Judge progress within limits | Useful work is stopped too soon, or stalled work consumes resources without end | Set limits for time to start, time between meaningful progress signals, and total duration. Keep work running while progress stays within all three |
| Resolve state before retrying | A retry duplicates work or side effects from an unfinished attempt | On expiry, check completion and liveness. Stop what remains and confirm it stopped. Before retrying, check for completed effects. Retry at most once, only when safe; otherwise escalate |
| Delegate parallel work and verify it | Work that could run in parallel runs in sequence, concurrent writers corrupt shared state, or a delegate's report is trusted unchecked | Delegate each part that can run alongside others, whether or not the parts are independent or check themselves. Give each delegate a bounded brief and exclusive file ownership, coordinate shared state, and keep dependencies ordered. Verify each result and the joined whole yourself; a delegate's own check is not verification |

## Refine

Use `principles-refine` to compare the actual result with the intent, revise at the scale of the gap, and verify the whole again. Return to Plan or Build when the evidence calls for it.

Delete unnecessary work before optimizing it. Understand a process before automating it. Use a cheap experiment when it can answer the question sooner than more analysis.

## Working record

Keep the project model current; revise it when evidence changes. Record the links between intent, requirements, decisions, implementation, and verification where the next person will find them. State known limits where the work lives. Make failures visible and recoverable, with an immediate signal and fallback when needed.

### Optional scratchpad

Use a scratchpad when work spans sessions, involves delegates, or needs a recovery record. Skip it for small tasks that can be completed and checked in one pass. Reuse the project's existing record when it serves this purpose; adapt these headings instead of creating a second ledger.

Before task work, fill the intent, relevant 5W1H context, goal, binding constraints, and definition of done. Mark unknowns in Open. Keep Todo tied to the definition of done and State current with verified facts, pending work, and the next safe action. Link evidence rather than copying it. Keep secrets out of the record.

Append dated checkpoints with expected versus actual results and evidence. Preserve earlier entries; append corrections when evidence changes. Record decisions with their reasons and limits of authority. Update the record at meaningful changes and before a handoff, so another reader can resume without guessing what ran or what remains.

```markdown
## Constraints

- Must not break:

## Goal

## Todo

## State

## Checkpoint

_(append-only; dated expected vs actual, with evidence)_

## Definition of Done

## Open

## Decisions

## Notes

Intent:
5W1H: What / Why / Who / When / Where / How
```

Check the record at handoff: can a fresh reader identify the goal, next safe action, unresolved questions, and evidence for completed work? A scratchpad supports continuity; it does not replace verification or grant permission to act.

## The method in each domain

| Domain | Plan looks like | Build looks like | Verify looks like |
|---|---|---|---|
| Software | spec, interfaces, data model | small commits behind tests | tests, types, staging, metrics in production |
| Hardware | requirements, load cases, free-body diagrams | sketch, model, prototype, test article | analysis and representative tests chosen for the required margin or failure behavior |
| Visual and sound design | brief, references, motifs, palette | thumbnails, then one full pass, then detail | three-distance review, real observers |
| Writing | reader, purpose, outline | draft fast, then cut | cold read, does the reader act correctly? |
| Research | question, hypothesis, what would disprove it | cheapest experiment that could fail | replication, independent check |
| Business | customer, problem, unit economics | smallest offer someone pays for | revenue, retention, cost per unit |
| Learning | target skill, the test that proves it | deliberate practice at the edge of ability | the test, unaided |

Pairs with: before `principles-scope`, `principles-ground`, `principles-represent`; after `principles-design`, `principles-refine`, `principles-verify`, `principles-lessons`.
