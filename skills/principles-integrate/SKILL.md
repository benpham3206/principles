---
name: principles-integrate
description: Join separately made parts into one whole that works, and prove it end to end. Interfaces, seams, boundaries to merge or keep, incremental integration, and checking every surface. Use when combining modules, subsystems, or work from several people or agents.
---

# Integrate

**Integration** is joining parts made apart into one whole, and proving the whole does what each part was for. Parts that each pass alone can still fail together, because the faults live at the seams: a unit, a frame, an assumption, or a timing that two makers read differently. The integrator owns the whole, not the parts.

```
INTERFACES ----> THIN SLICE ----> ADD ONE PART ----> CHECK THE SEAM ----> EVERY SURFACE
defined before   one path         at a time, the     test what crosses    each place the
the parts are    through every    whole kept         it, from both        change reaches,
built            layer, working   working            sides                each way in and out
```

## Laws

- The whole is the product. A part that passes alone has passed nothing yet.
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
5. Read the actual work, not the report of it. A summary of a part is a claim; the part itself, run in the whole, is the evidence.
6. Walk every surface the change reaches: entry points, clients, environments, adapters, stored data, documentation, and the way back out of every way in. Name each one and say whether it applies.
7. Fix seams in the same pass that finds them. A seam left for later is a fault shipped.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Interfaces first | Parts built against guesses about each other, then forced to fit | Was each interface written down before either side was built? |
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
| Tolerances stack at seams | Each part within its limit, the assembly out of its limit | Add the worst cases across the chain. Does the whole still meet its limit? |

## Choosing a boundary

- Keep a boundary when the parts change on different schedules, are made or replaced by different owners, must be tested apart, or need a trust or failure limit between them.
- Remove a boundary when only one caller uses it, both sides always change together, or its interface is as large as what it hides.
- A boundary is worth its cost when the interface is small and what it hides is large.
