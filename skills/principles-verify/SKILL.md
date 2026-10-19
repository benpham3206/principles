---
name: principles-verify
description: Verify work before calling it done, so it is true, works, and good. Evidence against the real thing, taste at three distances, and a bar you would sign. Use when reviewing or critiquing work, comparing options, or before claiming any result, including your own.
---

# Verify

**Done** means three things: the work is true, it works, and it is good. **Verification** is evidence for the first two. **Taste** is a trained prediction of how the work will land with its observer, together with the will to reject work that misses. **Pride** joins them: hand over only what you would sign. Taste without evidence ships beautiful errors. Evidence without taste ships correct work nobody wants.

## Steps

Run these before calling anything done, your own work first of all.

1. **Restate intent and done.** One sentence: purpose, observer, binding constraint, and what done means. Without it, checking is only preference; stop and get it.
2. **Name every surface.** List each place the work reaches: entry points, platforms, clients, stored data, docs, and the way back out. Say which ones you checked. Working on the tested path and broken elsewhere is not done.
3. **Check the real thing.** Run the feature, read the actual value, inspect the actual diff, look at the actual render. A report, a summary, a cached result, or a successful call is a claim, not evidence.
4. **Use the simplest evidence that proves it.** Climb the evidence ladder below and stop at the first rung that proves the claim.
5. **Make the check repeatable.** Prefer a script or a command over an eyeball, and keep its output where someone else can rerun it.
6. **Look at three distances.** Far, middle, and close, from the table below. Each scale hides different faults.
7. **Read it cold.** Read it as the observer who has none of your context. Ask what a master of this medium would reject first, and fix that.
8. **Rank and fix.** Fix the worst finding first. Stop when the next fix costs more than it returns.
9. **Report honestly.** Name the evidence for each claim of done. List what you did not check and what is known to fail. A claim with no evidence is a guess.

## Laws

- Evidence beats report. Agent prose, a passing summary, and a successful call are not proof that the intended state exists.
- A check that cannot fail proves nothing. A regression check must fail when the fix is removed, so break the fix once and watch it fail.
- When a check surprises you, suspect the observation before the system.
- Never weaken a check to make it pass. A weakened check is a hidden failure.
- Evidence outlives cleanup. Tear down what you started, and keep the proof.
- Write the check before the attempt. Checking an answer is far cheaper than finding one, so fix the target first.
- Separate facts, assumptions, estimates, and decisions. Never let one quietly become another.

## Pride

Pride is the standard of work you would put your name on. Before handing it over, ask: would I show this to the best maker in this medium without apology? If the answer needs a caveat, fix the thing or state the caveat plainly, never hide it. Craft lives in the details nobody asked for, so check those too.

## Defaults to replace

"It compiles." "Tests pass" when the changed path never ran. A subagent's summary taken as proof. A screenshot from before the last change. Only the happy path tried. A check that was never seen to fail. Done declared with no evidence named. Polish on the details while the whole is wrong.

## Three distances

| Medium | Far (the whole, in one second) | Middle (structure) | Close (detail) |
|---|---|---|---|
| Visual | squint or blur; thumbnail size | grid, groups, alignment | edges, type, color values |
| Sound | low volume, cheap speaker, next room | sections, mix balance | transients, noise, edits |
| Language | headings and first sentences only | paragraph order, argument | word choice, rhythm |
| Interaction | can a newcomer finish the main task? | flow and states | timing, feedback, copy |
| Code | module names and boundaries | signatures and data flow | names, edge cases, errors |
| Machine | free-body diagram, exploded view | load paths, interfaces | fits, finishes, fasteners |

Walk the six axes from `principles` at each distance. For each axis, name the choice made and whether it serves the intent. Most failures trace to an axis set by default.

## Taste: what to look for

Faults:

- **Sameness.** Every element at the same weight, so nothing leads.
- **Decoration.** A part with no job.
- **Defaults.** Values nobody chose: the stock font, the stock gray, the stock padding, the stock tempo, the stock phrase.
- **Hedging.** Elements or words added to avoid being wrong rather than to be right.
- **Genericness.** It could have come from anyone. Specificity is the first mark of taste.
- **Noise.** Inconsistency that means nothing.
- **Effort on the wrong scale.** Polish on details while the whole is wrong.

Marks of good work:

- One clear idea the observer gets without help.
- Every part earns its place; removing any part loses something.
- Choices hold at all three distances.
- Materials are honest: each one does what it looks like it does.
- Consistent where it should be, surprising where it means to be.

To build taste: study the best work in the medium until you can say why it is best in terms of the six axes, make many versions, and compare them side by side. Side-by-side comparison beats judging one thing alone.

## Evidence ladder

Cheapest first. Stop at the first rung that proves the property. A higher rung is not more rigorous when a lower one already proves it.

1. Types, compilers, and designs that make the fault impossible.
2. Schemas, constraints, and static checks.
3. Running the changed behavior directly.
4. A check on the stable contract or public interface.
5. A regression check for a failure that actually happened.
6. An integration check where the risk lies between parts.
7. An end-to-end check when only the whole can show the behavior.
8. Observation of real use, when real use is the evidence that matters.
9. Load, failure, security, or adversarial tests, when those are the actual risks.

The ladder holds in every medium. For a machine: analysis, then a bench test, then a test to failure. For writing: a cold read, then a reader who must act on it.

Leave one small runnable check for any branch, loop, parser, state change, money, or security logic that no cheaper rung would catch.

A model is a claim. State where it holds and where it breaks. One test in the real world outranks many simulations.

## A verify command for every project

Each project needs one command that people, agents, and automation run the same way. When a project has none, say so and build it:

1. **Launch.** Start the thing from an empty state, and know when it is ready to use, not merely running.
2. **Health check.** One read-only check that this instance is worth testing: it is up, it is the right version, and it is yours.
3. **Drive.** Exercise the real path an observer uses, not internal shortcuts or test-only doors.
4. **Capture.** Record the action and the resulting state, including side effects such as files written or messages sent.
5. **Clean up.** Remove what you started, never more, and keep the evidence.

Run the command once end to end before trusting it. A check that was never run is a draft.
