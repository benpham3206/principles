---
name: principles-synthesize
description: Create a new approach from known truths. Use for ambitious goals, unsolved problems, or ideas from other fields.
---

# Synthesize

In one line: Combine known truths into new possibilities, then check each one against reality.

**Synthesis** combines known truths into something new. Ask what is true, generate possibilities, and check them against reality.

```
Known facts and limits -> Possible approaches -> Simulate and test
                                  ^                    |
                                  +------ Revise <------+
```

Start from what must be true. Keep a convention when its compatibility or familiarity serves the goal. Questioning other conventions can reveal approaches that have not been tried.

## Steps

1. **Set an ambitious goal.** State an outcome a person can observe and measure: for example, "a car battery that charges in 5 minutes and lasts 20 years."
2. **Write the complete output as if it already exists.** The finished spec, the product page, the paper's abstract, the user's day with it. Completeness forces every hidden requirement into view.
3. **Work backward to a plan**, as in `principles-invert`. List each step from today to that output, and the technology each step needs. Mark each technology as existing, existing but too costly, or not yet invented.
4. **Check the limits.** Test every step against physics and logic. Replace any step that breaks a law.
5. **Generate candidates for each open step.** Draw from two places:
   - known approaches, which are more likely to work;
   - unusual approaches: ideas from other fields, inverted assumptions (`principles-invert`), or extreme parameters. These fail more often but may offer larger gains.
6. **Verify.** Simulate where a model exists, stating where it holds. Then run the cheapest real test that could fail. Reality outranks the model. To separate the effects of several factors, use the experiment design in `principles-measure`.
7. **Report the gaps.** Whatever remains unverified or uninvented is the research agenda, ranked by how much of the goal it blocks.

Done when the output is complete, every step is marked verified, plausible, or open, and each open step has the cheapest next test named.

## Combining fields

Most invention is transfer. To find a candidate from another field:

- Restate the problem in general terms: "move heat out of a small volume", "find a signal in noise", "keep a crowd moving."
- Ask which field solves that general problem every day: biology, logistics, music, finance, games, materials.
- Bring back the mechanism, not the surface. Check that the conditions it depends on hold here.

## Think big, build small, win

Hold the full vision while you build the smallest piece that proves the hardest part. Prove the riskiest assumption first. Then widen.

Pairs with: before `principles-ground`, `principles-measure`, `principles-horizons`; after `principles-method`, `principles-verify`, `principles-invert`.
