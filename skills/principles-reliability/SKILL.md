---
name: principles-reliability
description: Keep systems working when parts fail. Use when designing for uptime or safety, adding redundancy or failover, or planning detection, rollback, recovery, and restore.
---

# Reliability

In one line: Prevent, detect, contain, and recover in proportion to the harm, and run every fallback before you need it.

**Reliability** is the chance that a thing does its job under stated conditions for the required time. Prevent faults, detect failures, contain harm, and test recovery. Scale each measure to the harm. For deliberate attacks, use `principles-secure`.

```
PREVENT ---------> DETECT ----------> CONTAIN ----------> RECOVER
fewer faults       see it in time     limit what one     restore the working
start: margin,     to choose a safe   fault can reach    state by a path that
simplicity, test   response                              has been run
```

Prevention lowers how often failure starts. Detection, containment, and recovery decide what a failure costs once it starts. Spend on all four; none replaces another.

## Laws

- **Rigor follows consequence.** Size the layers to the credible harm, how many it reaches, and how hard it is to undo, with the gate in `principles-method`.
- **Shared causes limit redundancy.** Redundancy removes the failures that do not disable every copy. A cause the copies share disables them together, so it sets a floor that more copies cannot lower.
- **Parts in series multiply.** When every part must work and their failures are independent over the same period, multiply their chances of working: 100 parts at 99 percent each give about 37 percent. Each required part added can only hold or lower the total.
- **A failure nobody sees is still running.** Time to detect is part of the failure.
- **Treat an unexercised path as broken until it runs.** A standby, backup, fallback, or rollback that has not run recently is a hypothesis.
- **Protection is made of parts.** Monitors, failover, and redundancy add failure modes of their own. Count them.
- **Reliability is conditional.** A rate measured under one load, environment, age, and set of users does not transfer to others.

## Defaults to replace

Two of everything on one power feed, network, region, config, version, or supplier batch; a standby never switched to; backups never restored; an alert nobody owns; silence read as health; a fallback that fails open; retries that turn one fault into a storm; failover that needs the failed part to decide; one person who alone knows how to restart it; reliability set by habit instead of by harm; tests only on the bench, at room temperature, under light load; and a failure rate quoted with no conditions.

## Steps

1. Rate the harm. For each function, what happens to whom when it stops, slows, gives a wrong answer, or acts when it should not? Set the rigor from the harm and its reversibility, using the table below.
2. List how each part can fail, its effect on the whole, and how soon the failure would be seen. Include people, power, networks, suppliers, config, and procedures. Use `principles-invert` to find failure paths that a parts list misses.
3. Find the single points: any part, person, credential, or file whose failure alone stops a critical function. Remove each one, back it up independently, or accept it in writing with its cost.
4. Test independence. For each redundant set, list what its members share: power, cooling, place, design, software version, config, supplier, operator, the deploy that changed them, and the assumption they were built on. Each shared item is a **common cause**. Separate those whose failure matters.
5. Design detection and isolation. For each critical failure mode, find the time from its start to unacceptable harm. Where a signal can fire and be acted on within that time, give it an owner and enough detail to choose the safe response. Where it cannot, the mode needs prevention or a protection that acts on its own. Then ask who notices when the monitor fails.
6. Contain. Bound what one failure reaches: separate pools, limits, timeouts, circuit breakers, bulkheads, fuses.
7. Choose the degraded state for each loss in advance: serve less, serve stale data marked stale, stop safely, or hand to a person. The safe state depends on the hazard: a brake sets, an exit opens, a write is refused.
8. Plan recovery: how to roll back, restore, or replace; how much data or work is lost; how long it takes; and what must be true before restart. Run it end to end.
9. Exercise on a schedule, under real conditions: fail over, restore from backup, cut the power. Re-run steps 1 to 4 when load, environment, users, or dependencies change.

## How much

Protections to consider at each level. Choose among them by the credible harm, how likely it is, how many it reaches, and how recoverable it is. A hazard analysis can justify less as well as more; a binding safety standard governs where one applies.

| Consequence | Protections to consider |
|---|---|
| Reversible and cheap, affects only you | A way to undo, tried once |
| Others depend on it; a failure costs hours or rework | Failure modes listed, detection with an owner, a rollback or restore that has been run |
| Large losses of data, money, or trust that cannot be undone | No single point in the critical function, redundancy without shared causes that matter, contained faults, recovery rehearsed on a schedule, an independent review |
| Serious physical harm | The above, plus the single-fault tolerance the hazard analysis calls for, protection independent of the control it protects, and the domain's safety standard |

Over-building is a failure too. A weekend prototype held to the bar of a flight controller never ships, and its extra parts add failure modes of their own.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Independence before redundancy | Two copies on one power source, region, or version, so one event takes both. Two parts that each fail with probability 1 in 1000 over a period, independently, both fail about 1 in a million; if both hang on one supply that fails 1 in 10,000 over the same period, the pair fails about 1 in 10,000 | List everything the copies share. Could one event remove them all? |
| No silent single point | One person, key, file, or part that alone stops the function | Remove each part in turn on paper. Does a critical function stop? |
| Isolate enough to act | An alarm that says something is wrong but not enough to choose a response | From the signal alone, can the receiver choose the safe action? |
| Watch the watcher | A monitor that died quietly, so silence reads as health | Stop the monitor. Does anyone find out, and how soon? |
| Fail loudly where wrong is worse than stopped | A part that fails by giving plausible wrong output, so nothing downstream reacts | Can this part fail silent and wrong? What checks its output against an independent source? |
| Two can detect; three can mask one | Two disagreeing channels and no way to tell which is right | With one channel faulty, do the healthy results set a safe output? When agreement is ambiguous, is that detected and contained? Naming the faulty part needs its own check |
| Contain the blast | One fault cascades through shared pools, retries, or load moved onto the survivors | Fail one part at peak load. What fails with it? Can the survivors carry its load? |
| Degrade on purpose | All or nothing; a fallback that fails open | With each part removed, what does the user get, and is the loss shown? |
| Recovery and standbys are found by use | A standby, spare, backup, or rollback that was broken for months and first tried during the incident | When was each last run end to end, how long did it take, what was lost, and what was checked in the first minute after restart? |
| Know the life pattern | One constant failure rate assumed for parts whose failures cluster early, from defects, or late, from wear | Do field or test data show how failures change with age for this part? Plan screening or replacement only where they do |
| Conditions drift | A design proven under last year's load, temperature, users, or dependencies | What changed since it was proven, and was it proven again? |
| Stage every change: a small, chosen share first, with a signal that halts it, then wider on evidence | A defect reaches everyone at once and cannot be recalled | Who meets the change first, what signal would halt it, and who can halt it? |
| The world repeats, reorders, and interrupts actions, so make each action safe to run twice and to stop midway | A duplicate effect, or a half-applied state after a stop | Run it twice; stop it midway. Is the end state one clean run, or can it resume? |

## Margin

Margin is capacity over demand, against one named failure mode, for any resource: strength, time, money, attention, or capacity. A margin with no mode named means nothing. For loads, this is the factor of safety in `principles-machine`. Check: for each limit that matters, name the mode and the ratio.

## Over its life

A released thing keeps working only while someone keeps it. Plan its upkeep from the start.

- People depend on what it does, not only on what it promises. Before changing a behavior, find who relies on it.
- Every address others cite, such as a link, an identifier, or a part number, keeps resolving or points to its successor.
- Retire in order: announce, give a path to the replacement, support both for a stated window, then remove.
- Name who keeps it when its maker leaves, and keep what they need to do so.

Failure: a better version breaks the people who relied on the old one, or the thing decays once its maker moves on. Check: who relies on each behavior you change, and who keeps the thing next year?

Pairs with: before `principles-verify`, `principles-lessons`; after `principles-method`, `principles-secure`, `principles-machine`, `principles-code`, `principles-integrate`.
