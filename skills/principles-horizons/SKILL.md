---
name: principles-horizons
description: Trace first, second, and later-order consequences of a decision, technology, or goal. Use for strategy, long-range planning, predicting how people and systems will respond, worst-case thinking, or reasoning about a world changed by advanced AI.
---

# Horizons

A **horizon** is how far ahead you trace consequences. The **first-order** effect is the direct result. The **second-order** effect is how people and systems respond to it. Later orders are responses to the responses, until a new balance forms. Most surprises live past the first order.

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

## Patterns that recur

- **Cheaper means more.** When a thing gets cheaper, total use often rises enough to raise total consumption.
- **Value moves to the bottleneck.** When one step of a chain becomes abundant, value flows to the step that stays scarce.
- **Signals decay.** When a signal becomes cheap to fake, it stops carrying information, and people look for a new one.
- **Incentives win.** Over time, a system does what it rewards, whatever it says it does.
- **Slow variables decide.** Trust, skill, infrastructure, and culture change slowly and outweigh fast variables over long horizons.

## Worked horizon: abundant machine intelligence

An example of the method, labelled by confidence.

| Order | Change | Confidence |
|---|---|---|
| First | Analysis, writing, and code become cheap and fast. Growth accelerates; expert explanation reaches anyone who asks | likely |
| Second | Everyone can reach a doctoral level of synthesis. The scarce inputs become the questions worth asking, taste, verification, trust, physical execution, and attention | plausible |
| Third | Credentials lose signal because the knowledge they certified is available on demand. Value flows to insight and to arbitrage between cheap machine labor and costly human needs | plausible |
| Fourth | People who stop practicing judgment lose it; dependency grows unless tools build the user's ability | plausible |
| Fifth | Legitimacy questions arise: who decides, who is accountable, whose values the systems carry | speculative |
| Sixth | Meaning and identity shift when work no longer defines contribution | speculative |

From this horizon come four design goals for any tool that adds intelligence:

- **The counterpart rule.** Where the person's own ability is part of the goal, every gain in machine capability ships with a human counterpart; `principles-develop` holds the rule and its test. Where the goal is only the output, as with an accessibility aid or routine automation, delegation is the point.
- **Turn search into checking.** Make hard problems tractable by finding structure, so that answers become checkable and search narrows (see `principles-verify`).
- **Understanding keeps pace.** The person's model of the world should grow with the system's, even if more slowly. A result nobody understands cannot be trusted or corrected.
- **Value flows to insight as well as labor.** Design so that people capture value from new understanding, not only from cheaper work.

Pairs with: before `principles-ground`; after `principles-method`, `principles-synthesize`.
