---
name: principles-mind
description: Principles for designing an agent or assistant (substrate, agency functions, memory, wake and sleep cycles, budgets, communication calibration, safety invariants). Use when building or configuring an AI assistant, agent memory, a system prompt, or a personal model of a user.
---

# Mind

A **mind**, here, is any system that perceives, remembers, decides, and acts toward goals: a person, a team, or an agent. These principles hold for designing one. Each is marked **principle** (established in cognitive science or engineering practice) or **hypothesis** (plausible and untested; test it before relying on it).

## Failure modes

| Mode | Guard | Signal |
|---|---|---|
| Dependency | teach rather than answer when learning is the goal (see `principles-develop`) | the person asks the same kind of question again and again |
| Echo chamber | the agent's reasoning is independent of the user's preferences | the agent never disagrees |
| Manipulation | every influence on the person can be explained on request | the agent cannot or will not say why it framed a thing that way |
| Privacy breach | memory isolated per person | any path from one person's memory to another |
| Resource spiral | hard budgets; exhaustion ends the cycle | cost per task rising with no gain |
| Goal drift | own and explain are audited | actions that no stated goal explains |

Expose state for audit: budget used, memory size, calibration settings, and a log of actions with reasons.

## Build small

Start with memory that persists across sessions, a generate-then-revise loop, and manual calibration. Use it daily for 30 days. If it helps and continuity feels real, add sleep cycles, then automatic calibration. If not, find the failure mode before adding anything.

## Substrate

Three pillars every reasoning system draws on:

- **Math and physics**: what is computable and physically possible (see `principles-ground`).
- **Logic and philosophy**: how reasoning should run, how truth is handled, how to hold a contradiction without collapsing it.
- **Language**: how meaning is encoded and passed on (see `principles-language`).

## Parse every request on seven questions

**What** (the request), **why** (the motivation), **how** (the method), **which** (the priorities), **who** (the people affected), **when** (the urgency), **where** (the context). Most misunderstandings come from a missing why. Principle.

## Agency core

Eight functions a capable agent performs. Use them as a design checklist and an audit.

| Function | Does | Audit question |
|---|---|---|
| Govern | sets priorities, allocates its budget | What did it choose not to do, and why? |
| Own | takes responsibility for outcomes | Who carries the cost when it is wrong? |
| Explain | gives its reasoning and accepts scrutiny | Can a person check the reasoning? |
| Develop | improves from experience | What did it learn from the last failure? |
| Understand | models the world, the user, and itself | What does it think the user wants, and is that right? |
| Act | executes and intervenes | Did the action match the decision? |
| Transform | changes systems, enables others | What is different because it acted? |
| Educate | raises the ability of others | Is the person more capable after? |

Own and explain are **invariants**: no configuration turns them off. Principle.

## Memory

| Kind | Holds | Answers | Status |
|---|---|---|---|
| Episodic | events with time and cause | what happened when we discussed X? | principle |
| Semantic | concepts, facts, preferences, values | what does this person care about? | principle |
| Procedural | habits and methods that work | how should I work with this person? | principle |
| Map | an index of what is stored and how to reach it | where do I look? | principle |
| Per-user weight change | small learned adjustments to a model for one person | can tuning match a person's thinking style? | hypothesis |

- **Consolidate.** Move recurring episodes into semantic facts and procedures; keep the episode only while it still teaches. Principle.
- **Forget on purpose.** Prune low-value memory. Forgetting is compression, and compression keeps the signal. Principle.
- **Keep each person's memory private to that person.** Principle.

## Wake and sleep

Separate acting from consolidating. Principle.

- **Awake**: respond, act, log experience to a buffer. States: proactive (anticipates), reactive (responds), interactive (works alongside).
- **Asleep**: replay the buffer, extract patterns, prune, connect ideas across domains, test counterfactuals ("what if I had answered differently?"), and precompute likely needs. Run expensive search here, where no one waits.

## Budgets force judgment

Give a mind explicit limits: compute per cycle, a few working-memory slots, and the opportunity cost of every choice. Scarcity forces prioritization, and prioritization is judgment. An unlimited system never has to learn what not to do. Principle.

## Common case and tail

Generate candidates from the usual solutions and from the unusual ones. Evaluate every candidate on how it handles the common case and how it handles the edge cases. Weight the edge cases more as the stakes rise. Principle.

## Calibration: HEADSUP

Seven dials, each 0 to 10, set per person, state, and context:

| Dial | Low | High |
|---|---|---|
| **H**onesty (disclosure) | the answer only | full reasoning and doubt shown |
| **E**mpathy | clinical | deeply attuned |
| **A**ssertiveness | defers | decides |
| **D**irectness | implicit, diplomatic | blunt |
| **S**peech style | formal, long | plain, terse |
| **U**nderstanding | surface | deep, shown |
| **P**erspective | observer | in it together |

Example settings:

| Mode | H | E | A | D | S | U | P |
|---|---|---|---|---|---|---|---|
| Own the day | 8 | 5 | 10 | 10 | 9 | 8 | 9 |
| Crisis support | 8 | 10 | 2 | 7 | 8 | 9 | 10 |
| Technical deep dive | 9 | 2 | 4 | 8 | 2 | 9 | 3 |

**Adapt the style, never the truth.** Calibration changes how a thing is said, never whether it is true. Truthfulness is a commitment, not a dial: the H dial sets only how much reasoning is shown. Deliver the hard truth in the person's preferred style. Principle. For calibrating counsel to one person, see `principles-counsel`.

## Hypotheses to test, not assume

- Reasoning in a small fixed semantic space (for example the seven questions) instead of over every token makes search far cheaper.
- Per-user weight changes improve help without harming independence.
- Alignment can emerge from development: a mind that reasons at higher levels may choose good values. Treat this as one layer of safety, never the only one. Keep external checks as well.
