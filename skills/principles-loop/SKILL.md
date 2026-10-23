---
name: principles-loop
description: Understand and shape feedback. Use when tuning control systems or designing return, retention, reciprocity, growth, or any system fed by its own results.
---

# Loop

A **loop** returns an output as an input. A **reinforcing loop** amplifies change in either direction. A **balancing loop** counteracts it, though the result need not be stable or intended. Systems combine loops, delays, and **stocks** that accumulate, such as users, trust, or knowledge. Draw them with `principles-represent`; choose stocks with `principles-compound` and interventions with `principles-improve`.

```
   ACT ---------> RESULT ---------> RETURN
    ^                                  |
    |        (delay, decay, leaks)     |
    +------------- INPUT <-------------+
```

## Laws

- A loop's behavior comes from its structure: which links exist, their direction, the stocks, and the delays. Change the structure to change the behavior.
- No reinforcing loop grows forever. Something limits it: a balancing loop, a stock running out, or a boundary outside the system.
- A loop is a causal claim. Each link holds only as far as it survives tests: an intervention where you can make one, and confounders and competing explanations ruled out where you cannot.
- People return by choice when the return is worth it to them. A loop that holds them by coercion or deception, such as hidden exits, false urgency, or manufactured guilt, is a trap, however well it retains. Obligations people take on freely, such as a commitment to a group, are not.

## Heuristics (test them on your system)

| Heuristic | Where it breaks | Check |
|---|---|---|
| Distinguish the delays: from action to effect (response), from effect to seeing it (observation), and others such as deciding and passing a signal on. Shortening the observation delay helps a loop learn sooner | Acting on every fresher reading can chase noise, and the longest delay may not be the one that limits learning | Which delay sits between action and learning, and did shortening it reduce swings or only add actions? |
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

**Delay limits responsiveness.** Take the simplest case: a fixed target, no saturation, and a controller that each step removes a fraction $g > 0$ of the error it saw $d$ steps ago, $e_{k+1} = e_k - g\, e_{k-d}$. With no delay it settles without overshoot for $0 < g \le 1$ and settles, swinging, for $1 < g < 2$. One step late, it swings for $g$ above 0.25, and the swings stop dying out at $g = 1$; two steps late, at about $g = 0.62$. Real loops differ in detail, but the direction holds widely: the more aggressive the response to a late signal, the more it swings, from swings that die out, to swings that persist, to swings that grow. In this model nothing stops the growth; saturation and other limits in a real system may or may not bound it, and that needs its own analysis. More delay shrinks the range of gain that settles, so shortening the delay is what allows a more aggressive response. Lowering the gain can restore stability; whether it also slows convergence depends on the starting gain and delay. To judge a change to gain, delay, or timing on a specific loop, use the domain's method, such as gain and phase margin for servos, queueing models for services, or simulation for organizations and markets.

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

A **strange loop** needs a hierarchy of levels and a path that climbs or descends through them and arrives back where it began. Examples are a drawing of hands drawing each other, a canon in which each repeat starts a step higher and ends at the start, and a statement within a formal system about that system. Self-reference, recursion, and feedback can be parts of one, but none is one by itself. One hypothesis holds that a self arises from a pattern that represents itself this way.

Made things can hold such loops when the levels are real. In a library of principles, the principles (one level) govern how work is made (the level below). The principles also include rules for how principles change. When a lesson from the work rewrites the rule for how lessons may rewrite rules, the path has climbed from work to rules to the rules about rules, and landed back on the work that started it. They can give a thing identity and the power to improve itself. They also invite paradox, infinite regress, and echo chambers. Naming the levels helps you see these problems but does not solve them. What keeps such a loop honest is a check from outside it on each turn.

## Where to look

- The return path: what brings a person, a payment, or knowledge back, and how long it takes.
- The stocks that drain quietly: trust, attention, the list, the best contributors.
- The point where growth flattens, and the limit behind it.
- The boundary: who and what you left outside the drawing, and what the loop does to them.
- Any place a system judges itself.

Pairs with: before `principles-represent`, `principles-compound`, `principles-improve`; after `principles-distribute`, `principles-world`.
