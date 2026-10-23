---
name: principles-invert
description: Find paths and limits by reversing a question. Use when working backward from an outcome, testing a rule against its opposite, or designing a failure to find its guard.
---

# Invert

**Inversion** reverses a question to find hidden paths or limits. The reverse is a candidate, not proof. Keep evidence for both directions separate. Evidence tests factual claims; the rightful decision maker chooses between values.

```
FORWARD     steps -------> outcome        principle ----> good result
INVERTED    outcome -----> what must be   opposite -----> where it wins
                           true before    failure ------> its guard
```

## Five moves

| Move | Ask | Failure it prevents | Check |
|---|---|---|---|
| **Backward from the outcome** | Describe the finished outcome as a state someone can observe, with a number. What must be true just before it? And before that, back to today? | A plan made of activities, none of them needed or enough for the outcome | Does each step name the precondition it makes true, and do the preconditions together give the outcome? |
| **Invert the principle** | State its opposite. In what realistic case is the opposite right? | A heuristic applied as a law, past its limit | Name a case where following the principle makes the outcome worse. Is that limit written beside the principle? |
| **Invert the intent** | What does following it optimize, what does it cost, and who pays? What would someone with the opposite value build? | A value pursued with its costs unseen: simplicity that deletes needed margin, speed that skips the check | Whose loss does the rule accept, and did someone choose that? |
| **Design the failure** | How would you make the feared outcome happen reliably? | Guards chosen by habit that miss the actual path to failure | For each path found, which guard blocks it, and has that guard been seen to work? |
| **Reverse a relation** | Swap cause and effect, input and output, maker and observer, or the order of two steps | A sequence kept because it is the usual one | What would you build, measure, or decide differently in the reversed order? |

Examples of a reversed relation:

| Usual | Reversed | Different action |
|---|---|---|
| Knowledge guides creation | Creation produces knowledge | Build an instrumented prototype to learn what analysis cannot tell you |
| Requirements, then implementation | Implementation exposes requirements | Put a crude working version in front of a real observer to find the missing need |
| Design for the process | Change the process for the design | Change the fixture or tool so a better geometry becomes possible, within cost, tolerance, and yield |
| Features produce an experience | The experience picks the features | Specify what the observer should feel or achieve, then keep only the features that cause it |

## Limits

- An inversion must still satisfy the laws that apply and their assumptions; conventions and habits are what it may overturn. Use the kinds of claim in `principles-ground` to tell them apart.
- An outcome rarely fixes one cause, so working backward gives candidate paths, not the path.
- A reversed arrow is a hypothesis about cause. Test it before building on it.
- A failure you design runs only on paper or in a bounded test. Safety, consent, and irreversible limits stay in force.

## Steps

1. State the original: the plan, relation, or principle, the outcome it is for, and its kind of claim.
2. Pick one move. Inverting several things at once leaves no way to tell which one helped.
3. Derive a different action: what you would build, measure, remove, or decide. When nothing different follows, the inversion adds nothing; stop.
4. Check it against the limits above.
5. Test it the way its kind needs. Competing factual claims: a separating test, as in `principles-ground`. A proposed action or order: does it improve the outcome within the constraints? A value trade-off: show the consequences, and name who decides.
6. Keep, combine, or discard it by the result. When an inverted principle revealed a limit, write the limit where the principle lives.

Stop when the best inversion has a mechanism and a test, when the original wins under the measured constraints, or when no inversion changes the next decision.

Pairs with: before `principles-ground`, `principles-method`; after `principles-synthesize`, `principles-lessons`.
