---
name: principles-compound
description: Make gains feed later gains and protect them from loss. Use when choosing what to learn, build, record, or invest in, or when growth, decay, or debt accumulates over cycles.
---

# Compound

In one line: Keep each gain and feed it into the next cycle, and protect the series from any loss that resets it.

A gain **compounds** when it becomes input to the next gain. The thing that grows is a **stock**: knowledge, skill, tools, records, trust, capital, or a body of work. Each **cycle** adds to it or takes from it. The same arithmetic applies to a person, a team, a codebase, an organization, or a field.

Compounding is momentum: what each cycle carries into the next. `principles-loop` shapes the cycle itself, and the two are used together.

```
gain -> retained in the stock -> reinvested as input -> next gain
  ^                                                      |
  +------------------------------------------------------+
Each cycle can also lose part of the stock to decay or a single large loss.
```

## Laws

- Rate and cycle count both multiply. A stock that grows at rate $r$ per cycle for $n$ cycles grows by $(1 + r)^n$. This holds while the rate stays constant, the gain is reinvested, and nothing limits growth. Doubling takes about $70 / p$ cycles at $p$ percent per cycle, an approximation that is close for small rates.
- A gain compounds only when it is retained and reinvested. A gain that is lost, or kept and never used, adds once and stops.
- Losses compound by the same arithmetic. A stock that loses fraction $d$ per cycle keeps $(1 - d)^n$ of itself. Neglect, debt, forgetting, and distrust grow this way.
- Swings lower the compound rate. Up 50 percent and then down 50 percent leaves 75 percent of the start, though the average change is zero. The rate that compounds is the geometric mean, not the arithmetic mean.
- Every compounding stock meets a limit: a balancing loop, a resource that runs out, or a boundary outside the system (`principles-loop`). Name the limit before planning on the curve.
- A loss that resets the stock ends the series. The root skill's no ruin principle governs it (`principles`).

## Defaults to replace

Growth planned as a straight line, or as a curve with no ceiling. Activity counted as gain. A fix, insight, or decision kept in one head or never written down. Work restarted from nothing each cycle. A high rate bought with a chance of total loss. Gross growth reported while the stock decays. Effort spent accumulating what is becoming abundant.

## Steps

1. Name the stock that should grow and the cycle that adds to it.
2. For each cycle, name where its gain is retained and what in the next cycle starts from it. A gain with no home resets.
3. Estimate the rate and the cycle length. Shorten the cycle before raising the rate, when quality holds.
4. Name what the stock loses each cycle and what will limit its growth.
5. Name the one loss that would reset the stock. Bound it before raising the rate.
6. Measure the stock, not the activity, at intervals longer than its noise (`principles-measure`). Move effort from cycles that reset to cycles that compound.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Retain the gain | Work is redone because its result was never kept | Where does this cycle's gain live, and can the next cycle find it? |
| Reinvest | Gains are stored and never used as input | What in the next cycle starts from this gain? |
| Many short cycles | Few long cycles, so feedback and gains arrive late | How long from action to usable result? Can it shrink without losing quality? |
| Bound the worst loss | A high rate carries a chance of losing everything | Which single event resets the stock, and what bounds it? |
| Reduce swings | The average looks good while the compound rate is low | Compare the geometric rate with the average rate over the same cycles |
| Count decay | Growth is reported gross while the stock erodes | What is lost each cycle, and is net growth positive? |
| Expect the limit | A plan extends the curve past its ceiling | What limits growth, and when will it bind? |
| Compound what stays scarce | Effort accumulates something that is becoming cheap and plentiful | Will this stock still be scarce and valued when the series matures? This is a heuristic; scarcity can change |
| Stock over activity | Busy cycles leave the stock unchanged | Did the measured stock grow? |

## What compounds

| Stock | Compounds through | Decays when |
|---|---|---|
| **Knowledge** | Each concept makes the next easier to learn and connect | it is never used or never written down |
| **Skill** | Each attempt improves the prediction for the next | the same attempt is repeated without review |
| **Taste** | Better judgment picks better inputs, which train better judgment | only one's own work is seen |
| **Finished work and tools** | Each finished piece becomes an asset, a reference, or a tool for the next | work is started and not finished |
| **Records** | Retained context removes rework | records are scattered or never consulted |
| **Trust** | Kept promises make the next agreement cheaper and larger | one broken promise outweighs many kept ones |
| **Lineage** | Knowledge passed to others keeps compounding after its maker | it lives in one head |

Pairs with: before `principles-lessons`, `principles-counsel`, `principles-loop`; after `principles-improve`, `principles-measure`.
