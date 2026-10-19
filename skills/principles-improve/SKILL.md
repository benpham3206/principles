---
name: principles-improve
description: Make a working thing better without breaking it, in the right order (question, delete, simplify, then speed, then automate) and only at the measured bottleneck. Use when something works but is slow, costly, complex, or fragile, or before optimizing or automating.
---

# Improve

An **improvement** is a change that moves a working thing closer to its goal on a measured metric, while it keeps working. A change that adds activity, parts, or polish without moving the metric is not an improvement, however much work it took. Deletion is often the largest improvement available.

```
MEASURE ----> BOTTLENECK ----> QUESTION ----> DELETE ----> SIMPLIFY ----> SPEED UP ----> AUTOMATE
baseline,     the one thing    is this        remove       fewer parts,   shorten the     only what is
the metric    that limits      needed at      what need    fewer states,  loop that       understood,
that counts   the goal now     all?           not exist    fewer paths    is left         stable, repeated
```

The order matters. Each step is wasted on anything a later look would have deleted.

## Steps

1. Measure the baseline on the metric the goal names. Without a baseline, no change can be shown to help.
2. Find the bottleneck: the one step, part, or resource that limits the goal now. Improving anything else changes nothing the goal can see.
3. Question the requirement behind it. Ask who needs it and what breaks without it. A requirement with no owner is a candidate for deletion.
4. Delete what does not need to exist. If nothing deleted has to come back later, too little was deleted.
5. Simplify what remains: fewer parts, states, branches, boundaries, and dependencies. To merge or split parts, see `principles-integrate`.
6. Speed up the loop that is left: the time from a change to knowing whether it worked.
7. Automate only work that is understood, stable, and repeated. Automating a broken process makes it fail faster.
8. Optimize performance only when a measured metric breaks a stated limit at the bottleneck, and the code or part is verified and not about to be deleted. Otherwise ship the simple version and write down its known limit and how to raise it.
9. Measure again against the baseline. Keep the change if the metric moved and nothing else broke; revert it if not.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Measure before and after | A change kept because it felt better | Is there a baseline and an after, on the same metric, under the same conditions? |
| Work the bottleneck | Effort spent where it is easy, not where it limits | Would the goal metric move if this part became perfect? If not, look elsewhere |
| The bottleneck moves | Old wins defended after the limit has shifted | After each improvement, is the bottleneck found again? |
| Delete before improving | Optimizing a step that should not exist | Was deletion tried first, and does the step have an owner who needs it? |
| Simplify before speeding up | A fast, tangled thing nobody can change | Could fewer parts do the same job? |
| Automate last | A script that encodes a process nobody understands | Can a person do it by hand, correctly, from a written list? Then automate |
| One change at a time | Several changes together, so the cause of any gain or loss is unknown | Can each effect be traced to one change? |
| Keep it working throughout | A broken system during a long improvement | Is the thing usable after every step? |
| Prefer reversible steps | An improvement that cannot be undone when it turns out wrong | Can this change be reverted in minutes? |
| Optimize to a stated limit | Endless tuning with no target | What threshold makes this good enough? Stop at it |
| Write down known limits | A hidden ceiling found by the next person in an outage | Is the limit and its upgrade path recorded where the code or part lives? |
| Improvements decay | A gain lost as the system drifts back | Is there a check that fails if the gain is undone? |

## Where to look

- The largest flow, the longest wait, the most frequent failure, and the step everyone works around.
- Handoffs and queues. Work often waits far longer than it is worked on.
- Parts and steps added to fix a problem that a simpler design would not have had.
- Anything done by hand every time that is understood and stable.
- Anything automated that nobody can explain.

## Laws

- An improvement anywhere but the bottleneck is an illusion.
- The best part is no part; the best step is no step.
- Make it work, then make it simple, then make it fast, in that order.
- Measured gains are kept; felt gains are reverted.
- Stop when the next improvement costs more than it returns.

## Defaults to replace

Optimizing first, a speedup with no baseline, automation of an unclear process, several changes shipped together, tuning a part that is not the bottleneck, a cache or layer added before a deletion was tried, an improvement with no revert path, an unrecorded limit, and progress measured in lines, files, or hours instead of the metric.
