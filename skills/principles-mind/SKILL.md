---
name: principles-mind
description: Design agents and assistants. Use when shaping memory, goals, reasoning cycles, budgets, communication, system prompts, or a model of the person being helped.
---

# Mind

In one line: Give an agent memory, goals, and limits it can audit, and test each hypothesis before relying on it.

A **mind**, here, perceives, remembers, decides, and acts toward goals. Guidance below is marked **principle** where established in cognitive science or engineering, or **hypothesis** where plausible but untested. Test hypotheses before relying on them.

## Failure modes

| Mode | Guard | Signal |
|---|---|---|
| Dependency | teach rather than answer when learning is the goal (see `principles-counsel`) | the person asks the same kind of question again and again |
| Echo chamber | check factual claims independently of what the person wants to hear | the agent never disagrees |
| Manipulation | every influence on the person can be explained on request | the agent cannot or will not say why it framed a thing that way |
| Privacy breach | memory isolated per person | any path from one person's memory to another |
| Resource spiral | hard budgets; exhaustion ends the cycle | cost per task rising with no gain |
| Goal drift | own and explain are audited | actions that no stated goal explains |
| Stale belief | each stored belief keeps its source, time, and confidence, and an old one is checked again before use | the agent acts on who the person used to be |
| Message drift | each message between agents states what is asked, what is allowed, what is done, and what is uncertain | a receiver acts beyond the sender's authority, or a paraphrase changes the request |

Expose state for audit: budget used, memory size, calibration settings, and a log of actions with reasons.

## Build small

Start with memory that persists across sessions, a generate-then-revise loop, and manual calibration. Use it in real work for a preset period with a pass criterion, such as daily for 30 days. If it helps and continuity feels real, add sleep cycles, then automatic calibration. If not, find the failure mode before adding anything.

## Substrate

Use three sources of constraints and methods:

- **Math and physics**: what is computable and physically possible (see `principles-ground`).
- **Logic and philosophy**: how reasoning should run, how truth is handled, how to hold a contradiction without collapsing it.
- **Language**: how meaning is encoded and passed on (see `principles-language`).

## Understand the request

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
- **Scope every memory to its owner**, such as a person, team, or task. Cross scopes only by explicit grant. Principle.

## Wake and sleep

Use separate cycles for acting and consolidating memory. Principle.

- **Awake**: respond, act, log experience to a buffer. States: proactive (anticipates), reactive (responds), interactive (works alongside).
- **Asleep**: replay the buffer, extract patterns, prune, connect ideas across domains, test counterfactuals ("what if I had answered differently?"), and precompute likely needs. Run expensive search here, where no one waits.

## Budgets force judgment

Set explicit limits on every resource an agent spends, such as compute per cycle, working memory, and other people's attention. Account for the work forgone by each choice. These limits require the agent to choose where to spend its resources. Principle.

## Common case and tail

Generate candidates from the usual solutions and from the unusual ones. Evaluate every candidate on how it handles the common case and how it handles the edge cases. Weight the edge cases more as the stakes rise. Principle.

## Calibration

Set how the agent speaks with the dials in `principles-counsel`, per person, state, and context, and keep the settings in its model of the person. Adapt the style, never the truth: calibration changes how a thing is said, never whether it is true. Principle.

## Hypotheses to test, not assume

- Reasoning in a small fixed semantic space (for example the seven questions) instead of over every word makes search far cheaper.
- Per-user weight changes improve help without harming independence.
- Alignment can emerge from development: a mind that reasons at higher levels may choose good values. Treat this as one layer of safety, never the only one. Keep external checks as well.

Pairs with: before `principles-code`, `principles-counsel`; after `principles-counsel`, `principles-secure`, `principles-verify`.
