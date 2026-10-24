---
name: principles-ground
description: Reason from evidence and first principles. Use when checking claims, comparing explanations, choosing experiments, or deciding whether more information would change a decision.
---

# Ground

**Grounding** checks a claim or design against evidence and the limits of physics, logic, mathematics, and perception.

## Map and territory

A description is a **map**; the thing described is the **territory**. Language compresses the world, and compression loses detail. An agent that works only in words can build a consistent, fluent map that matches nothing. People do this too.

- Treat every statement, your own included, as a claim about the territory, not as the territory.
- Ground a claim by touching something outside language: a measurement, a test that can fail, a simulation with stated limits, a source you have read, a person who was there.
- When two maps disagree, go to the territory. Do not average the maps.
- Fluency is not evidence. A smooth explanation and a true one feel the same from inside.

## Kinds of claim

| Kind | Rests on | Holds within | Outside that, do this |
|---|---|---|---|
| Formal law: logic, mathematics | proof from axioms | situations that satisfy the axioms | Find the axiom that fails; the result says nothing there |
| Physical law | repeated measurement | the tested range of speed, size, temperature, and material | Use the more general law, or measure |
| Empirical regularity: perception, materials data, human behavior | observations of a known population | that population and setting | Treat it as a hypothesis and test it on the case |
| Heuristic | a default that usually pays | cases without its named exceptions | Look for the exceptions; if none are named, find them before relying on it |
| Hypothesis | it would explain what is seen | nothing yet; it waits for a test that could refute it | Run the test; revise or drop it |
| Convention | agreement | the people who agree | Follow the current agreement, or change it openly |
| Value or taste | the goals of the intended observers | those observers and goals | Name whose goals; judge with those people |

Most rules in these skills are empirical regularities or heuristics. Apply one where its conditions hold. Where they do not, say so and reason from what does hold.

## Label what you know

- **Observation**: seen or measured directly. Note how, and with what instrument.
- **Inference**: derived from observations by a step you can state. It is no stronger than its weakest step.
- **Hypothesis**: a proposed explanation, with the result that would show it false.
- **Assumption**: taken as true to proceed, unchecked. Name what breaks if it is wrong.
- **Estimate**: a quantity with its uncertainty and its basis.
- **Decision**: a choice, with who made it.

A **fact** is an observation, or an inference whose steps were checked. Never let one kind become another without saying so: a hypothesis that survived one test is still a hypothesis, and an assumption repeated is still an assumption.

Match confidence to evidence. Give a range and its basis, such as "4 to 7 days, from five similar jobs." Use a probability only with a base rate, model, or calibrated track record. Otherwise say likely, plausible, or speculative, and name what would change that judgment.

## Reasoning Methods

Choose and combine reasoning methods based on the problem, available evidence, and uncertainty. Check assumptions, consider alternative explanations, and revise conclusions when evidence changes.

| Method | Use and check |
|---|---|
| Deduction | Apply known rules to reach conclusions. Check premises and the rule's scope with [kinds of claim](#kinds-of-claim) |
| Induction | Find patterns in observations. Check their population and setting with [kinds of claim](#kinds-of-claim) |
| Abduction | Identify the most likely explanation by [comparing explanations](#compare-explanations) |
| First principles | Break problems into fundamental facts and rebuild solutions with "First principles, as a procedure" below |
| Analogy | Apply lessons from similar problems; [compare known to unknown](#compare-known-to-unknown) to check the differences |
| Causal reasoning | Determine what causes what. Use the intervention and confounder checks in `principles-loop` |
| Probabilistic reasoning | Make decisions with incomplete information. Use [confidence labels](#label-what-you-know), [explanation updates](#compare-explanations), and [stopping rules](#when-to-learn-more) |
| Counterfactual reasoning | Consider what would happen if something changed. State what changes and what stays fixed; trace consequences with `principles-horizons` |
| Systems reasoning | Understand how components interact. Trace feedback, stocks, and delays with `principles-loop` |
| Metacognition | Examine and correct your own reasoning; [label what you know](#label-what-you-know) and [reopen conclusions built on false assumptions](#compare-explanations) |

## Compare explanations

When something needs explaining, such as a failure, a result, or a surprise:

1. Write every explanation still in play: at least two, and "something not yet named". The familiar one is a candidate, not the answer.
2. For each, write what it predicts that the others do not.
3. Weigh evidence by how much more likely it is under one explanation than under the others. Evidence that every candidate predicts moves nothing, however much of it there is. When you hold a prior, state it, update it with the data, and check whether the decision changes under other plausible priors.
4. Choose a test that can distinguish explanations requiring different actions. Weigh that information against the test's cost and risk. One test that separates three such explanations can be more useful than three tests that each support only one.
5. Update. When a result contradicts an assumption, mark it false and reopen every inference and decision built on it.
6. Stop by the rule in the next section. A decision can be settled while several explanations remain plausible, when all of them call for the same action.

Failure: the familiar cause is investigated, found plausible, and fixed, while the real cause stays. Check: before acting, name the result that would have pointed to a different cause, and say whether you looked for it.

## When to learn more

Reduce an uncertainty when reducing it could change a consequential decision. Before gathering, name the decision, the result that would change it, how likely that result is, and what waiting costs.

- No plausible result would change the choice: decide now.
- A mistake is cheap and reversible: act, and treat the result as the test.
- Otherwise, gather the information whose likely results improve the decision by more than its cost, delay, and risk. A test that could flip the choice is worth little when that result is very unlikely or the test is often wrong.
- A safety or legal limit is not traded against cost: where the limit could be crossed, check before acting.

Failure: research that continues after the choice is settled, or an irreversible step taken on an assumption that a cheap check would have overturned. Check: what result would change the decision, how likely is it, and is learning it worth more than it costs?

## Measurements and predictions

- Use `principles-measure` to define quantities, choose and check instruments, collect readings, carry uncertainty, and compare results. Establish what the measurement supports before inferring a cause or generalizing beyond its conditions.
- A prediction is a model run forward. Its uncertainty grows with distance from the cases the model was checked against; state that distance.

## Axioms by domain

These are the limits nothing designed can beat. State the general form; give local values (Earth gravity, sea-level air) as one case, labelled.

- **Conservation.** Energy, mass, momentum, and charge are conserved. Every design is an accounting of where they go.
- **Entropy.** Every real process loses some useful energy as heat. No machine is perfectly efficient; no process runs backward for free.
- **Signal speed.** No signal travels faster than light, about $3.0 \times 10^8$ m/s in vacuum. Distance is delay.
- **Scale.** Area grows with the square of size and volume with the cube. Small things are dominated by surface effects, large things by weight.
- **Materials.** Every material has a strength, a stiffness, and a temperature limit. Structure is the art of staying under them.
- **Information.** Data cannot be losslessly compressed below its entropy, and noise caps how much a channel can carry.
- **Computation.** Some problems are easy to check but hard to solve. Some questions no program can answer for every input.
- **Perception.** These are empirical regularities. Over the middle of a sense's range, the smallest noticeable change grows in proportion to the size of the stimulus; near the threshold it does not. Working memory holds only a few chunks at once. Attention is finite.
- **Human systems.** People respond to incentives. Every choice has an opportunity cost. Trust is slow to build and fast to lose. These are durable regularities, not physical laws.

## First principles, as a procedure

1. State the problem as a physical or logical goal, stripped of how it is done today.
2. List what must be true: the axioms above that apply.
3. Derive the limit: the best result physics and logic allow (minimum energy, minimum mass, minimum time, raw material cost).
4. Compare the limit with current practice. The gap is the opportunity, and its size says how much invention is possible.
5. Ask what convention, not law, holds practice away from the limit. Conventions can change.

Done when the limit is a number with units and each step to it names the law it rests on.

## Compare known to unknown

To reason about something new, anchor it to the nearest thing that is known and measured, then reason only about the difference. State which known case you chose and why it is close. The size of the difference is the size of your uncertainty.

Pairs with: before `principles-measure`; after `principles-method`, `principles-research`, `principles-horizons`.
