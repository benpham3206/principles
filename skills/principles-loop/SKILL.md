---
name: principles-loop
description: Understand and shape feedback. Use when tuning control systems or designing return, retention, reciprocity, growth, or any system fed by its own results.
---

# Loop

A **loop** feeds a result back into what happens next. A **reinforcing loop** amplifies change in either direction. A **balancing loop** counteracts change; it can still be unstable or produce an unwanted result. A **stock** accumulates over time, such as users, trust, or knowledge.

Use `principles-represent` to draw the loops and delays. Use `principles-compound` to choose what to accumulate and `principles-improve` to choose what to change.

```
Action -> Result -> Return as an input
  ^                         |
  +-------------------------+
Each turn can include delay, decay, and loss.
```

## Laws

- A loop's behavior comes from its structure: which links exist, their direction, the stocks, and the delays. Change the structure to change the behavior.
- No reinforcing loop grows forever. Something limits it: a balancing loop, a stock running out, or a boundary outside the system.
- Each link in a loop claims that one change causes another. Test it by intervention where possible. Otherwise, rule out competing explanations and confounders: other factors that could produce the apparent link.
- People return by choice when the return is worth it to them. A loop that holds them by coercion or deception, such as hidden exits, false urgency, or manufactured guilt, is a trap, however well it retains. Obligations people take on freely, such as a commitment to a group, are not.

## Heuristics (test them on your system)

| Heuristic | Where it breaks | Check |
|---|---|---|
| Measure delays separately: action to effect, effect to observation, and time spent deciding or passing a signal on. Shorter observation delay can help you learn sooner | Acting on each new reading can chase noise. The longest delay may not be the one that limits learning | Which delay sits between action and learning, and did shortening it reduce swings or only add actions? |
| People come back for what renews: new value, being remembered, other people, visible progress | Some returns are habits that serve the person well with nothing new | Would they come back if nothing reminded them? |
| Giving with no condition starts trust that taking cannot | Some gifts are taken and never returned, and that is fine | Would the gift still be worth giving if nothing came back? |
| Value made by members for members lets a community outgrow its founders | Members can be exploited for unpaid work | Are contributors credited, heard in decisions, and free to leave with their work? |

## Defaults to replace

Growth planned as a straight line, a launch with no reason to return, rewards on a random schedule tuned for compulsion, streaks that punish a missed day, a gift with hidden strings, notifications that take attention without giving anything, memory of a person kept without their consent, a retention number read without asking whether people are better off, a push answered by a harder push before the first one shows, and a system that only checks itself.

## Steps

1. Draw the loops as causal claims: each link, its direction, the stocks it fills or drains, and its delay. Draw the boundary: what you treat as outside.
2. For each link, name the evidence for it: an intervention where you can make one, otherwise a prediction that could fail, with confounders and competing explanations ruled out. Look for reversed causes and missing stocks.
3. Name what limits each reinforcing loop.
4. Before intervening, predict what each candidate change does to the whole loop, including side effects on people and parts outside the boundary. Pick by predicted effect for its cost; `principles-improve` has the method.
5. Design the return: what renews for the person each time, and what they would miss.
6. Give first, then make giving back small and obvious: a reply, a contribution, a referral, a payment.
7. Let members make value for each other, with credit and a voice.
8. Remember people only with consent, keep the least you need, and let them see and delete it.
9. Check the health of the loop over months, not visits: do people take part willingly, are they better off, can they leave easily, and does it harm anyone outside it?

## Principles

| Principle | Failure | Check |
|---|---|---|
| Structure over effort | Pushing harder on a loop whose shape produces the problem | Which link, stock, or delay produces this behavior? |
| Causal evidence | A loop drawn from a story, with a reversed, confounded, or imagined link | Was each link tested by intervention, or its rivals ruled out? |
| Stocks and flows | Watching a rate while the stock behind it drains | What accumulates here, and what fills and drains it? |
| Named limits | Growth planned with no ceiling | What limits this reinforcing loop, and when will it bind? |
| Leaks and decay | A loop that seems to grow while its stock drains | What is lost each cycle: churn, forgetting, trust? |
| Return worth making | People come once and never again | What is new, remembered, or alive the next time they come? |
| Consent to be remembered | Memory that surprises or exposes people | Did they agree, is it the least needed, and can they delete it? |
| Gifts without strings | A gift that is really a trap, so trust breaks | Would the gift stand if they never gave back? |
| Fair communities | Members' work captured without credit or voice | Who gets credit, who decides, and can members leave with their work? |
| Willing participation | Retention bought with coercion or deception | Over months, do people choose to return, are they better off, and is leaving easy? |
| Effects outside the loop | A loop that works for its members and harms others | Who outside the boundary bears a cost? |
| Grounded self-reference | A system that only checks itself and drifts from reality | What outside check does each turn meet? |

## Control

A **controller** compares a measurement with a target and acts to close the gap. The **state** determines what the system does next, such as temperature or queue length. **Inputs** are what the controller changes; **outputs** are what it measures. **Disturbances** change the state from outside.

**Feedback** corrects measured error after it appears, including errors nobody predicted. **Feedforward** acts on a plan or measured disturbance before the error appears. Pair it with feedback to catch model errors. A state is **observable** when it can be inferred from output history and known inputs, and **controllable** when inputs can move it to the target. Check both before tuning.

### Delay and gain

A late reading can lead to a correction that is too large for the current state. Consider a model with a fixed target and no saturation. The controller's **gain** $g > 0$ sets the fraction of error it removes at each step. It acts on the error seen $d$ steps ago. Let $e_k$ be the error at step $k$:

$e_{k+1} = e_k - g\, e_{k-d}$.

| Delay | Behavior in this model |
|---|---|
| None | Settles without overshoot for $0 < g \le 1$; settles with swings for $1 < g < 2$ |
| One step | Swings for $g > 0.25$; the swings stop decaying at $g = 1$ |
| Two steps | The swings stop decaying at about $g = 0.62$ |

In this model, more delay narrows the range of gain that settles. Shortening the delay allows a more aggressive response. Lowering the gain can restore stability; whether it slows convergence depends on the starting gain and delay.

When the swings grow, this model has nothing to bound them. Saturation or other limits in a real system may bound them; check that separately. To choose gain or timing for a real loop, use the domain's method: gain and phase margin for servos, queueing models for services, or simulation for organizations and markets.

| Principle | Failure | Check |
|---|---|---|
| Name state, inputs, outputs, disturbances | A controller tuned on what it sees, blind to the state that drives it and the pushes from outside | What does the system hold, what can you change, what can you see, and what moves it unasked? |
| Stable before fast | A loop made more responsive that now swings: hiring and layoffs, autoscaler flapping, an agent that over-corrects each review | After a step change, does it settle, and in how many swings? Is each correction sized and spaced for the delay? |
| Feedback for the unpredicted, feedforward for the known | Waiting for a scheduled load to cause an error, or running a plan open loop with no check | Which disturbances are known ahead? Is each met early, with feedback behind it? |
| Observe the state, not a proxy | The measured number improves while the thing it stood for gets worse, because the loop drove the number | If this metric were gamed or drifted, what other measurement would reveal the real state, and how late? |
| Act through a path that reaches the state | Pushing harder on an input that does not move the state: more servers for a queue held by a lock | Trace the path from input to state. Did a past change in this input move it? |
| Plan for saturation | At an input's limit the loop is open; error that piles up meanwhile, such as a backlog, queued retries, or an integrator winding up, lurches out when the limit lifts | What happens at full input? What accumulates there, and what bounds it? |
| Gain amplifies noise | A controller that chases measurement noise; a filter added to calm it that adds delay | Does the action change when the state did not? What delay did the filter add? |
| Disturbances faster than the loop need other defenses | Feedback expected to catch a spike it cannot see in time | Is each fast disturbance met by a buffer, feedforward, or margin? |

## Strange loops

A **strange loop** moves through a hierarchy of levels and arrives back where it began. Examples include hands drawing each other, a canon whose repeats rise in pitch and return to the start, and a statement within a formal system about that system. Self-reference, recursion, and feedback can be parts of a strange loop; each can also exist without one. One hypothesis holds that a self arises from a pattern that represents itself this way.

A library of principles can contain this structure. Its principles govern how work is made. They also govern how the principles themselves may change. A lesson from the work can revise those rules and then change how the next work is made: work, rules, rules about rules, and back to work.

Such loops can give a thing identity and a way to improve itself. They can also produce paradox, endless chains of justification, and echo chambers. Name the levels to make these risks visible. Check each turn against evidence outside the loop.

## Where to look

- The return path: what brings a person, a payment, or knowledge back, and how long it takes.
- The stocks that drain quietly: trust, attention, the list, the best contributors.
- The point where growth flattens, and the limit behind it.
- The boundary: who and what you left outside the drawing, and what the loop does to them.
- Any place a system judges itself.

Pairs with: before `principles-represent`, `principles-compound`, `principles-improve`; after `principles-distribute`, `principles-world`.
