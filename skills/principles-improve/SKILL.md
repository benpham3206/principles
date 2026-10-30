---
name: principles-improve
description: Improve a working thing while preserving what matters. Use when reducing cost, delay, complexity, or failures, or before optimizing or automating.
---

# Improve

In one line: Measure the gain on the goal's own metric, and keep every requirement intact while you pursue it.

An **improvement** moves a working thing toward its goal on a measured metric while preserving its requirements. Extra activity or polish alone proves no gain.

Use `principles-refine` for revisions to expression, coherence, or fit judged through comparison and use. A refinement can include measured improvement; match the evidence to the claim.

```
MEASURE ----> BOTTLENECK ----> QUESTION ----> DELETE ----> SIMPLIFY ----> SPEED UP ----> AUTOMATE
baseline,     the one thing    is this        remove       fewer parts,   shorten the     only what is
the metric    that limits      needed at      what need    fewer states,  loop that       understood,
that counts   the goal now     all?           not exist    fewer paths    is left         stable, repeated
```

Check whether a step is needed before spending effort making it faster.

## Laws

- Find what limits the metric. For throughput, improve the limiting stage or what makes it wait. For totals such as latency or cost, compare each possible reduction with its cost. The largest term is a place to look, not an automatic choice.
- The best part is no part; the best step is no step.
- Make it work, then make it simple, then make it fast, in that order.
- Keep a change when measurements show a gain and the requirements still hold. Otherwise, return to the prior version.
- Stop when the next improvement costs more than it returns.

## Defaults to replace

Optimizing first, a speedup with no baseline, automation of an unclear process, several changes shipped together, tuning a part that is not the bottleneck, a cache or layer added before a deletion was tried, an improvement with no revert path, an unrecorded limit, and progress measured in lines, files, or hours instead of the metric.

## Steps

1. Use `principles-measure` to establish the baseline on the goal metric and the guardrails: the other measures that must not get worse. Correctness checks are always guardrails. Without a baseline, no change can be shown to help.
2. Find what limits the goal now, including how parts interact. For throughput, that is the limiting step and whatever makes it wait or blocks it. For a metric that adds up, compare the reduction each part can give for its cost.
3. Question the requirement behind it. Ask who needs it and what breaks without it. A requirement with no owner is a candidate for deletion.
4. Delete what does not need to exist. Stop when the next deletion would break the goal or a guardrail.
5. Simplify what remains with `principles-simplify`. Reduce parts, states, branches, and dependencies while preserving requirements.
6. Speed up the loop that is left: the time from a change to knowing whether it worked.
7. Automate only work that is understood, stable, and repeated, or a one-time job whose manual cost or risk exceeds the cost of building and checking the automation. Automating a broken process makes it fail faster.
8. Optimize performance only when a measured metric breaks a stated limit at the bottleneck, or measurements show it will before a fix could be ready, and the code or part is verified and not about to be deleted. Otherwise ship the simple version and write down its known limit and how to raise it.
9. Run each change as an experiment. First record its hypothesis, expected metric change, and acceptable guardrail ranges. Keep it only if the gain exceeds noise and every guardrail holds; otherwise revert it. Record the measurements and decision, including rejected changes, in the work's history. Then find the limit again. Six Sigma's define, measure, analyze, improve, control cycle (DMAIC) is one form of this loop. Control checks that the gain holds.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Measure before and after | A change kept because it felt better | Is there a baseline and an after, on the same metric, under the same conditions? |
| Work the bottleneck | Effort spent where it is easy, not where it limits | Would the goal metric move if this part became perfect? If not, look elsewhere |
| The bottleneck moves | Old wins defended after the limit has shifted | After each improvement, is the bottleneck found again? |
| Delete before improving | Optimizing a step that should not exist | Was deletion tried first, and does the step have an owner who needs it? |
| A place for everything, at the point of use | A tool, part, or file hunted for each time it is needed | Does each thing have one marked place where it is used, so a missing one shows at a glance? |
| Clean to inspect | A leak, crack, or drift hidden under dirt or clutter, or a real alert hidden among stale ones | Does each cleaning include a look for what changed since the last one? |
| Standardize the best known way | Each person does the job their own way, so no gain can be measured or kept | Is the current best method written where the work happens, and is it the baseline for the next change? |
| Simplify before speeding up | A fast, tangled thing nobody can change | Could fewer parts do the same job? |
| Automate last | A script that encodes a process nobody understands | Can a person do it by hand, correctly, from a written list? Then automate |
| One change at a time, unless a designed experiment separates the effects | Several changes together, so the cause of any gain or loss is unknown | Can each effect be traced to one change, or to a factor in a planned design (see `principles-synthesize`)? |
| Keep it working throughout | A broken system during a long improvement | Is the thing usable after every step? |
| Prefer reversible steps | An improvement that cannot be undone when it turns out wrong | Can this change be reverted in minutes? |
| Optimize to a stated limit | Endless tuning with no target | What threshold makes this good enough? Stop at it |
| Write down known limits | A hidden ceiling found by the next person in an outage | Is the limit and its upgrade path recorded where the code or part lives? |
| Improvements decay | A gain lost as the system drifts back | Is there a check that fails if the gain is undone? |
| Find who pays: a gain can move its cost to someone the metric does not see, such as the user's attention, their battery, or a later maintainer | A faster path that drains the battery or someone's time | Who pays for this gain, and is that payer one of the guardrails? |
| Stop at the bar where value is passing a threshold; where value is rank among comparable work, the last increments can matter most | Stopping at adequate on work judged against the best | Is this work judged by a threshold or by rank? If by rank, compare it with the best comparable work |

## Where to look

- The largest flow, the longest wait, the most frequent failure, and the step everyone works around.
- Handoffs and queues. Work often waits far longer than it is worked on.
- Parts and steps added to fix a problem that a simpler design would not have had.
- Anything done by hand every time that is understood and stable.
- Anything automated that nobody can explain.
- The workspace itself, bench or repository. Sort out what is not needed, set the rest in order, clean to inspect, standardize, and sustain: the 5S practice of the Toyota Production System. Clutter hides the bottleneck.

Pairs with: before `principles-simplify`, `principles-verify`, `principles-distribute`, `principles-ground`; after `principles-lessons`, `principles-compound`.
