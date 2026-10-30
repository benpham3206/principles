---
name: principles-integrate
description: Join parts and verify the whole. Use when combining modules, subsystems, or work from several makers, or deciding which boundaries to keep.
---

# Integrate

In one line: Check units, frames, assumptions, and timing at every interface, then prove the joined whole works.

**Integration** joins separately made parts and proves that the whole works. Check differences in units, frames, assumptions, and timing at each interface. Passing parts can still fail together.

```
INTERFACES ----> THIN SLICE ----> ADD ONE PART ----> CHECK THE SEAM ----> EVERY SURFACE
defined before   one path         at a time, the     test what crosses    each place the
the parts are    through every    whole kept         it, from both        change reaches,
built            layer, working   working            sides                each way in and out
```

## Laws

- Check the whole. Passing checks on separate parts does not show that they work together.
- Faults gather at interfaces. Spend the checking there.
- Integration cost grows faster than the size of the batch. Join small, join often.
- What is not written at an interface is assumed differently on each side.
- Evidence is the whole running, not anyone's account of it.

## Defaults to replace

A big join at the end, interfaces agreed in conversation, units implied by context, parts accepted on their maker's word, a boundary for every team or file, a cycle between modules, the happy path as the only path tested, a way in with no way out, and a seam found and left for later.

## Steps

1. Define each interface before the parts are built: what crosses it (data, force, signal, heat, money, control), its units and frame, its range, its timing, and what each side guarantees when the other fails.
2. Build the thinnest slice that runs end to end through every layer. A crude whole that works teaches more than a polished part that waits.
3. Add one part at a time. After each, the whole must still run. When it breaks, the last part added is where to look.
4. Check each seam from both sides. Send the edge cases across it: empty, maximum, wrong unit, late, missing, repeated.
5. Inspect and run the actual work. Check each part inside the whole; its maker's summary is a claim to verify.
6. Walk every surface the change reaches: entry points, clients, environments, adapters, stored data, documentation, and the way back out of every way in. Name each one and say whether it applies.
7. Fix seams in the same pass that finds them. When a repair is not yet safe, contain the affected path, assign the fix, and keep it out of the release until fixed.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Interfaces first | Parts built against guesses about each other, then forced to fit | Was each interface written down and checked before either side was built, or before existing parts were joined? |
| One definition per interface | Each side keeps its own copy of the contract, and the copies drift | Is there one source both sides read or test against? |
| Units, frames, and conventions cross explicitly | One side sends one unit, the other reads another; signs or axes flipped | Does every value crossing the seam carry its unit and frame? |
| Thin slice before thick parts | Months of parts and a big join at the end, where every fault appears at once | Did a crude end-to-end path run before any part was finished? |
| Integrate small and often | A large merge whose failures cannot be traced to a cause | Can each failure be traced to the one change that caused it? |
| Keep the whole working | A long stretch where nothing runs while parts are swapped | Is there a working whole after every step? |
| Split on reasons to change | Boundaries drawn by size or by who built what, so one change crosses many parts | Does each part change for one reason? Do parts that always change together share a boundary? |
| Merge unneeded boundaries | A boundary with one user and no independent change, paying interface cost for nothing | What would break if these two parts became one? If nothing, merge them |
| Dependencies flow one way | A cycle, so no part can be built or tested first | Can the parts be ordered so each depends only on earlier ones? |
| The integrator reads the parts | A whole accepted because each maker said their part was done | Did someone run each part inside the whole and read what it did? |
| One maker per part at a time | Two makers editing the same part, each overwriting the other | Does every part have exactly one current owner? |
| Every surface, both directions | Works on the tested path and fails on another platform, client, or the undo path | Is each surface listed with a result? Does every way in have a way out? |
| Tolerances stack at seams | Each part within its limit, the assembly out of its limit | Add the worst cases where the whole needs a hard bound. For a stated failure allowance, combine them statistically only with a justified model of their dependence and shared bias; otherwise keep the bounds. Does the whole still meet its limit? |

## Choosing a boundary

- Keep a boundary when the parts change on different schedules, are made or replaced by different owners, must be tested apart, or need a trust or failure limit between them.
- Remove a boundary when only one caller uses it, both sides always change together, or its interface is as large as what it hides.
- A boundary is worth its cost when the interface is small and what it hides is large.

## Vertical integration

**Vertical integration** is owning more of the chain that makes a product, from raw parts to the person who uses it, so that hardware, software, and how it is made are designed together. It is the boundary decision above, made for a whole company or project: an outside supplier adds a boundary you control only in part.

| Principle | Failure | Check |
|---|---|---|
| Own the bottleneck | A supplier's cost, speed, or quality caps the product, and nothing inside can move it | Which outside part limits cost, schedule, or performance most? Could you make it better than you can buy it? |
| Co-design across the seam | Hardware and software built to a frozen interface, so each works around the other's limits | When one side changes, can the other change in the same cycle? Is the interface chosen for the product, or inherited? |
| Merge seams you own when they cost more than they give | Two internal teams keep a formal handoff that only a supplier needed | Owning both sides lets you merge a seam; the rules under Choosing a boundary decide whether you should. Does this one still pay for itself? |
| Shorten the loop | A change waits weeks on another company's schedule | How long from a design change to a tested part in hand? Who sets that time? |
| Make where ownership pays | Making a part in-house that others make better and cheaper, or buying one you could own for better cost, supply, or quality | Over its life, which gives better total value for this part: making it or buying it? |
| Count the full cost | Capital, people, focus, and the risk of owning a weak capability, ignored next to the savings | Over its life, does owning this beat buying it, including what you stop doing to do it? |
| Keep a way out | Integration that locks you to one process or design when it ages | Can you change course, re-source, or open the interface later without rebuilding everything? |

Integrate vertically where the boundary costs more than it saves: where the interface keeps changing, the supplier is the bottleneck, or the seam itself is where the product is won. Buy where the part is stable, standard, and not what makes the product better.

Pairs with: before `principles-code`, `principles-machine`, `principles-represent`; after `principles-ecosystem`, `principles-verify`.
