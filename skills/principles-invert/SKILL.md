---
name: principles-invert
description: Find paths and limits by reversing a question. Use when working backward from an outcome, testing a rule against its opposite, examining a value's costs, or designing a failure to find its guard.
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
| **Invert the intent or value** | What matters, to whom, and why? What would defeat it? What useful value might lead someone to choose differently? | A value pursued with its costs unseen, or a competing value treated as a threat | Which loss must be prevented, which trade-off is allowed, and who decides? |
| **Design the failure** | How would you make the feared outcome happen reliably? | Guards chosen by habit that miss the actual path to failure | For each path found, which guard blocks it, and has that guard been seen to work? |
| **Reverse a relation** | Swap cause and effect, input and output, maker and observer, or the order of two steps | A sequence kept because it is the usual one | What would you build, measure, or decide differently in the reversed order? |

Examples of a reversed relation:

| Usual | Reversed | Different action |
|---|---|---|
| Knowledge guides creation | Creation produces knowledge | Build an instrumented prototype to learn what analysis cannot tell you |
| Requirements, then implementation | Implementation exposes requirements | Put a crude working version in front of a real observer to find the missing need |
| Design for the process | Change the process for the design | Change the fixture or tool so a better geometry becomes possible, within cost, tolerance, and yield |
| Features produce an experience | The experience picks the features | Specify what the observer should feel or achieve, then keep only the features that cause it |

## Inverting a value

1. State value X, whose interests it serves, and why it matters here.
2. Describe its loss or violation as an outcome someone could observe. Ask what actions, incentives, constraints, or mistakes could cause it, then ask why those causes might arise.
3. Ask whether a different choice serves a competing value Y. X and Y need not be opposites. Compare what pursuing each value gains, what it costs, and who bears each cost. Ask whether both can be served. Use `principles-qualities` to rank the trade-off with the rightful decision maker.
4. For each unacceptable loss, choose what to avoid and a way to prevent, detect, or recover from it. Use `principles-secure` when misuse, compromised parts, or unauthorized action threaten what is protected. A difference in taste alone is not a threat.
5. Treat proposed causes and motives as hypotheses. Check factual claims with `principles-ground`. After observation or a bounded test, use `principles-lessons` to turn the evidence into a rule or check for the next decision. Record it where that decision is made.

Example: X is privacy, so people control who receives their information. Its violation is disclosure to an unintended recipient. A possible cause is a broad sharing default. Ask why that default exists: it may serve Y, easy collaboration. That motive remains a hypothesis. Restrict recipients and require an authorized sharing choice. In a bounded test with invented data, check that an unintended recipient is denied and an intended recipient can receive the shared item. Use the result to revise the rule.

## Limits

- An inversion must still satisfy the laws that apply and their assumptions; conventions and habits are what it may overturn. Use the kinds of claim in `principles-ground` to tell them apart.
- An outcome rarely fixes one cause, so working backward gives candidate paths, not the path.
- A reversed arrow is a hypothesis about cause. Test it before building on it.
- A failure you design runs only on paper or in a bounded test. Safety, consent, and irreversible limits stay in force. A value trade-off grants no new authority.

## Steps

1. State the original: the plan, relation, principle, or value, the outcome it is for, and its kind of claim.
2. Pick one move. Inverting several things at once leaves no way to tell which one helped.
3. Derive a different action: what you would build, measure, remove, or decide. When nothing different follows, the inversion adds nothing; stop.
4. Check it against the limits above.
5. Test it the way its kind needs. Competing factual claims: a separating test, as in `principles-ground`. A proposed action or order: does it improve the outcome within the constraints? A value trade-off: show the consequences, and name who decides.
6. Keep, combine, or discard it by the result. When an inverted principle revealed a limit, write the limit where the principle lives.

Stop when the best inversion has a mechanism and a test, when the original wins under the measured constraints, or when no inversion changes the next decision.

Pairs with: before `principles-ground`, `principles-method`; after `principles-synthesize`, `principles-lessons`.
