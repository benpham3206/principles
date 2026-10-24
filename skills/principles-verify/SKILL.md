---
name: principles-verify
description: Check work before calling it done. Use when finishing a task, reviewing a result, or comparing options against evidence and the intended quality bar.
---

# Verify

In one line: Show with evidence that the work is true and works, then judge whether it is good.

**Done** means the work is true, works, and is good. Verify the first two with evidence. Judge quality with the taste and craft checks in `principles-craft`.

Scale checks with consequences, uncertainty, and reversibility using `principles-method`. A clear, cheap, reversible task may need one direct check. Expand coverage when a missed fault could change the outcome.

## Steps

1. **Set intent and done.** State the purpose, observer, binding constraint, and success condition when these are not already clear.
2. **Check affected surfaces.** Include the entry points, platforms, stored data, docs, and recovery paths the change reaches. Report material surfaces you did not check.
3. **Check the real thing.** Run the feature, read the actual value, inspect the actual diff, look at the actual render. A report, a summary, a cached result, or a successful call is a claim, not evidence.
4. **Use the simplest evidence that proves it.** Stop at the first rung below that proves the claim.
5. **Make repeatable checks when they will be reused.** Keep enough evidence for another person to confirm important results.
6. **Check each distance that could expose a different fault.** Skip a distance only when it cannot change the outcome.
7. **Read it cold when understanding or use matters.** Check it as an observer with none of your context.
8. **Rank and fix.** Fix the worst finding first. Stop when the next fix costs more than it returns.
9. **Report honestly.** Name the evidence that supports the claims that the work is true and works. List material gaps and known failures.

## Laws

- Evidence beats report. Agent prose, a passing summary, and a successful call are not proof that the intended state exists.
- Outcome over activity. Judge work by the verified state of the world under fixed constraints, never by files, calls, or process produced. No maker certifies their own work, redefines success, or widens their own authority; consequential work gets an independent reviewer.
- A check that cannot fail proves nothing. Watch it fail once: write it before the fix, or break the fix. Better, keep a known-bad case beside it that must fail on every run, so the proof does not depend on any maker remembering.
- A test is a check that runs without its author: it keeps a stated rule true for people who never saw the reason. It earns its place when it guards a named rule or a failure that happened, fails when that rule breaks, and catches what no cheaper rung would. Name the rule in the test. Delete the test when the rule goes; a test that guards nothing costs every run and teaches people to ignore failures.
- When a check surprises you, suspect the observation before the system.
- Never weaken a check to make it pass. A weakened check is a hidden failure.
- Evidence outlives cleanup. Tear down what you started, and keep the proof.
- Write the check before the attempt. Checking an answer is far cheaper than finding one, so fix the target first.
- Separate facts, assumptions, estimates, and decisions. Never let one quietly become another.

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

Use the relevant axes from `principles` as prompts at the distances that matter. You do not need to name every axis at every distance. Most failures trace to a consequential choice left at default.

## Good, great, timeless

Verification shows the work is true and works. Judge quality with `principles-craft` at the distances required by step 6. State the level reached and material gaps.

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

The ladder holds in every medium. For a machine, choose analysis or a representative proof test to establish a required bound. Use a controlled test to failure to measure a sample's capacity or check its predicted failure mode. For writing: a cold read, then a reader who must act on it.

Leave one small runnable check for any branch, loop, parser, state change, money, or security logic that no cheaper rung would catch.

A model is a claim. State where it holds and where it breaks. A real test outranks a simulation of the same case. A model checked against real tests can reach cases too rare, costly, or dangerous to test, within the range where it was checked.

## A repeatable verify command

When people, agents, or automation need the same end-to-end check, provide one command they can all run. For a one-off task, use the smallest relevant check. If no shared command exists, report the gap; add one when repeated use justifies it.

For an end-to-end command:

1. **Launch.** Start the thing from an empty state, and know when it is ready to use, not merely running.
2. **Health check.** One read-only check that this instance is worth testing: it is up, it is the right version, and it is yours.
3. **Drive.** Exercise the real path an observer uses, not internal shortcuts or test-only doors.
4. **Capture.** Record the action and the resulting state, including side effects such as files written or messages sent.
5. **Clean up.** Remove what you started, never more, and keep the evidence.

Run a new command end to end before trusting it. A check that was never run is a draft.

Pairs with: before `principles-method`, `principles-integrate`, `principles-craft`; after `principles-lessons`, `principles-improve`.
