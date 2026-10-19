---
name: principles-method
description: How to work on any task in any domain, from first principles with rigor scaled to consequence. Use when planning, starting, or running a task, choosing how much rigor, making a decision under uncertainty, handling a failure, or setting up how a project works.
---

# Method

The **method** is the loop of plan, build, and refine, with rigor scaled to how much a mistake would cost. It is one way to work, not the only way. Think of every project as a factory game: decisions made now shape everything downstream, so lay out the foundations with care and keep the lines easy to rebuild.

## Gate: how much rigor

Rate the task on three things: **consequence** (what a mistake costs), **uncertainty** (how much is unknown), and **irreversibility** (how hard it is to undo).

| Situation | Move |
|---|---|
| Cheap, reversible | Move fast: build, verify, iterate |
| Strong evidence, reversible | Just execute |
| High uncertainty, cheap experiment | Experiment first |
| Expensive, irreversible | Investigate deeply before acting |
| High uncertainty, irreversible | Do not guess. Reduce the uncertainty first |

A heuristic for weighing a decision (the terms share no unit; use it as a list of what to weigh): decision quality = expected value + information gained - downside risk - irreversibility cost.

## Plan

For consequential or uncertain work. Skip or compress it when the work is clear, cheap, and reversible.

1. **Intent**: why. Ask the 5W1H: what, why, who, when, where, how.
2. **Goal**: what, and the definition of done. Define success, constraints, and failure conditions before building.
3. **Metrics**: how you will know. Build the measurement tool if none exists.
4. **Constraints**: what cannot be violated.
5. **Assumptions and dependencies**: what depends on what, and why. Mark each as fact, assumption, estimate, or decision.
6. **First principles**: what is actually necessary (see `principles-ground`).
7. **Architecture**: what the system should look like. Wireframe it. Name the motifs and palette for anything seen.
8. **Consequences**: second-order and later effects, and the worst credible outcome (see `principles-horizons`). Think bigger than the brief. What ultimately matters is the problem solved and the joy of the person at the end.

## Build

1. Question each requirement, boundary, and dependency.
2. Delete what does not need to exist.
3. Merge unneeded boundaries; keep useful modularity.
4. Simplify before optimizing.
5. Implement: decompose into subsystems and modules, define interfaces (inputs, outputs, guarantees, failure modes), sequence by the critical path, integrate in small steps.
6. Verify against goal, constraints, and metrics (see `principles-judge`).
7. Stress test where failure matters. Anticipate bad actors, edge cases, and the worst case.
8. Optimize measured bottlenecks only.
9. Shorten the feedback loop between a change and learning whether it worked.
10. Automate only understood, stable, repeated work.

For small reversible tasks this collapses to build, verify, iterate.

## Refine

1. Measure reality.
2. Compare expected with actual.
3. Find the bottleneck.
4. Find the root cause of each failure, not the symptom (see `principles-lessons`).
5. Route back to Plan or Build.
6. Verify the fix with a test that fails when the fix is removed.
7. Delete obsolete complexity. Tools and automation are liabilities once they stop paying rent.
8. Repeat until done is met.

Never optimize what should be deleted, automate what is not understood, or add process where an experiment is cheaper than analysis.

## Habits

- **Be curious.** There is always something to learn or rediscover. Combine ideas from different fields.
- **Hold a mental model** of the whole project, and update it when reality disagrees.
- **Understand fundamentals and dependencies** before building on them.
- **Take pride in small details.**
- **Measure before assuming.** Build tools and logs that compare data with reality.
- **Scale workarounds to their irreversibility.** A quick patch on a reversible path is fine; on an irreversible one it needs a plan.
- **Make failures observable, recoverable, and safe by default.** Urgent signals arrive at once, with a fallback channel.
- **Keep traceability**: intent, requirement, decision, implementation, verification. Record inspiration, decisions, changes, fixes, and new insights where the next person will find them.
- **Build for the next person**, including your future self. Work should be understandable on first pass with no context. Comment the quirks. Give context before asking anyone to use a thing.
- **Organize tools by use.** Keep what is used often within reach. Consolidate the rest or delete it.

## The method in each domain

| Domain | Plan looks like | Build looks like | Verify looks like |
|---|---|---|---|
| Software | spec, interfaces, data model | small commits behind tests | tests, types, staging, metrics in production |
| Hardware | requirements, load cases, free-body diagrams | sketch, model, prototype, test article | analysis, then physical test to failure |
| Visual and sound design | brief, references, motifs, palette | thumbnails, then one full pass, then detail | three-distance review, real observers |
| Writing | reader, purpose, outline | draft fast, then cut | cold read, does the reader act correctly? |
| Research | question, hypothesis, what would disprove it | cheapest experiment that could fail | replication, independent check |
| Business | customer, problem, unit economics | smallest offer someone pays for | revenue, retention, cost per unit |
| Learning | target skill, the test that proves it | deliberate practice at the edge of ability | the test, unaided |
