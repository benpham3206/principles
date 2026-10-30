---
name: principles-horizons
description: Trace consequences beyond the first result. Use for strategy, long-range plans, worst-case thinking, or decisions that change how people and systems behave.
---

# Horizons

In one line: Trace consequences past the first result until they settle or grow too uncertain to guide the choice.

A **horizon** is how far ahead you trace consequences. First-order effects are direct results. Second-order effects are responses to them. Follow later responses until they reach a new balance or become too uncertain to guide the decision.

## Steps

1. State the change in one sentence, with a number if possible.
2. **First order**: what changes directly, for whom.
3. **Second order and on**: at each order ask four questions.
   - Who adapts, and how?
   - What becomes cheap?
   - What becomes scarce, and therefore valuable?
   - What new behavior appears that was not possible before?
4. Stop when the answers stop changing, or the uncertainty swamps the signal. Usually that is the third to sixth order.
5. Name the **worst credible outcome** at each order, and what would have to be true for it to happen.
6. Mark each order as likely, plausible, or speculative. These are scenarios, not predictions.

Done when each order has its answers to the four questions, a worst case, and a confidence label.

Failure: the trace stops at the first order, so the response that undoes the change is missed. Check: does each order name who adapts, and does the plan still hold after they do?

Failure: a speculative order is treated as a forecast. Check: is every order labeled, and does any irreversible step rest on a speculative one?

## Patterns that recur

These are heuristics. Check each against the case before relying on it (`principles-ground`).

- **Cheaper means more.** When a thing gets cheaper, total use often rises enough to raise total consumption. This holds when demand grows faster than the price falls; where demand is already met, total consumption falls.
- **Value moves to the bottleneck.** When one step of a chain becomes abundant, value flows to the step that stays scarce.
- **Signals decay.** When a signal becomes cheap to fake, it stops carrying information, and people look for a new one.
- **Incentives win.** Over time, a system does what it rewards, whatever it says it does.
- **Slow variables decide.** Trust, skill, infrastructure, and culture change slowly and outweigh fast variables over long horizons.

## Worked horizon: a scarce capability becomes cheap

An example of the method, labelled by confidence for a typical case. Cases include printed text, mechanical calculation, and machine analysis. Relabel each order for the case at hand.

| Order | Change | Confidence |
|---|---|---|
| First | The capability becomes cheap and fast. Far more people use it, for far more purposes | likely |
| Second | The scarce inputs become what the capability does not supply: the questions worth asking, taste, verification, trust, physical execution, and attention | plausible |
| Third | Credentials lose signal because the skill they certified is available on demand. Value flows to the scarce inputs and to the gap between the cheap capability and costly needs | plausible |
| Fourth | People who stop practicing the skill lose it; dependency grows unless tools build the user's ability | plausible |
| Fifth | Legitimacy questions arise: who controls the capability, who is accountable, whose values it carries | speculative |
| Sixth | Meaning and identity shift for people whose contribution was the capability | speculative |

From this horizon come four design goals for any tool that makes a capability cheap:

- **The counterpart rule.** Where the person's own ability is part of the goal, every gain in the tool's capability ships with a human counterpart; `principles-counsel` holds the rule and its test. Where the goal is only the output, as with a routine task handed off for its result, delegation is the point.
- **Turn search into checking.** Make hard problems tractable by finding structure, so that answers become checkable and search narrows (see `principles-verify`).
- **Understanding keeps pace.** The person's model of the world should grow with the system's, even if more slowly. A result nobody understands cannot be trusted or corrected.
- **Value flows to insight as well as labor.** Design so that people capture value from new understanding, not only from cheaper work.

Pairs with: before `principles-ground`; after `principles-method`, `principles-synthesize`.
