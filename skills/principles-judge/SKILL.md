---
name: principles-judge
description: Taste and verification for any work, in any medium. Use when reviewing, critiquing, or verifying work, deciding whether it is done, comparing options, or before claiming a result, including your own output.
---

# Judge

**Taste** is a trained prediction of how a thing will land with its observer, together with the will to reject work that misses. **Verification** is evidence that a thing is true or works. Taste without verification ships beautiful errors. Verification without taste ships correct work nobody wants. Run both.

This is the recognitive layer: it compares the made thing against something outside it.

## Steps

1. **Restate the intent** in one sentence: purpose, observer, binding constraint. Without intent, judging is only preference; stop and get the intent.
2. **Look at three distances.** Each scale hides different faults.

   | Medium | Far (the whole, in one second) | Middle (structure) | Close (detail) |
   |---|---|---|---|
   | Visual | squint or blur; thumbnail size | grid, groups, alignment | edges, type, color values |
   | Sound | low volume, cheap speaker, next room | sections, mix balance | transients, noise, edits |
   | Language | headings and first sentences only | paragraph order, argument | word choice, rhythm |
   | Interaction | can a newcomer finish the main task? | flow and states | timing, feedback, copy |
   | Code | module names and boundaries | signatures and data flow | names, edge cases, errors |
   | Machine | free-body diagram, exploded view | load paths, interfaces | fits, finishes, fasteners |

3. **Walk the six axes** from `principles`. For each, name the choice made and whether it serves the intent. Most failures trace to an axis set by default.
4. **Verify against reality.** Compare with something the work cannot argue with: a measurement, a test, a simulation with stated limits, a reference, a real observer. Done when each claim of the work has its evidence named.
5. **Rank findings by consequence.** Fix the worst first. Stop when the next fix costs more than it returns.

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

To build taste: study the best work in the medium until you can say why it is best in terms of the six axes, make many versions, and compare side by side. Side-by-side comparison beats judging one thing alone.

## Verification: check before you generate

Finding an answer can be far harder than checking one. This asymmetry is the practical face of the open P versus NP question, and every engineer meets it. Use it.

- Write the check before the attempt: the test, the acceptance criterion, the reference render, the target number.
- Narrow the search with axioms (see `principles-ground`) so fewer candidates need checking.
- Make candidates cheap and checks fast, then generate many and keep the ones that pass.
- A model is a claim. State where it holds and where it breaks. One test in the real world outranks many simulations.
- Separate facts, assumptions, estimates, and decisions. Never let one quietly become another.

## Judging your own output

Your own work is the hardest to judge, because you read your intent into it.

- Read it cold, as the observer who has none of your context.
- Ask what a master of this medium would reject first, and fix that.
- Compare it against the best known example of its kind, not against your last draft.
- Name the evidence for each claim of done. A claim with no evidence is a guess.
