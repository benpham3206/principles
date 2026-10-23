---
name: principles-synthesize
description: Create a new approach from known truths. Use for ambitious goals, unsolved problems, ideas from other fields, or experiments that compare factors and tolerate noise.
---

# Synthesize

**Synthesis** combines known truths into something new. Ask what is true, generate possibilities, and check them against reality.

```
COGNITIVE                 GENERATIVE                RECOGNITIVE
what is true?      -->    what is possible?   <-->  is it true, is it consistent?
axioms, limits            many candidates,          simulate, then test in reality,
(see ground)              common and strange        compare known to unknown
                                                    (see verify)
```

**Axiomatic constraint creates novelty.** Constrain a design by what must be true, and keep a convention only where its compatibility or familiarity serves the goal. When convention is removed and only laws remain, the space of answers that fits is often one nobody has explored.

## Steps

1. **Take a Herculean goal.** State it as an outcome a person can see, with a number: not "better batteries" but "a car battery that charges in 5 minutes and lasts 20 years."
2. **Write the complete output as if it already exists.** The finished spec, the product page, the paper's abstract, the user's day with it. Completeness forces every hidden requirement into view.
3. **Work backward to a plan**, as in `principles-invert`. List each step from today to that output, and the technology each step needs. Mark each technology as existing, existing but too costly, or not yet invented.
4. **Bound it with ground.** Check every step against physics and logic. A step that breaks a law is removed, not optimized.
5. **Generate candidates for each open step.** Draw from two places:
   - the common distribution: the known approaches, most likely to work;
   - the tail: approaches from other fields, inverted assumptions (see `principles-invert`), extreme parameters. These fail more often and win larger.
6. **Verify.** Simulate where a model exists, stating where it holds. Then run the cheapest real test that could fail. Reality outranks the model.
7. **Report the gaps.** Whatever remains unverified or uninvented is the research agenda, ranked by how much of the goal it blocks.

Done when the output is complete, every step is marked verified, plausible, or open, and each open step has the cheapest next test named.

## Combining fields

Most invention is transfer. To find a candidate from another field:

- Restate the problem in general terms: "move heat out of a small volume", "find a signal in noise", "keep a crowd moving."
- Ask which field solves that general problem every day: biology, logistics, music, finance, games, materials.
- Bring back the mechanism, not the surface. Check that the conditions it depends on hold here.

## Experiment design

- Choose which experiment to run by its value to the decision, as in `principles-ground`.
- **Vary several factors at once** with a design that separates the effects and interactions the decision needs. Factorial designs can reveal interactions that changing one factor at a time misses. Fractions and orthogonal arrays reduce runs but can mix effects; state which effects the design cannot separate and keep needed interactions estimable. An uncontrolled before-and-after comparison cannot separate several changes.
- Randomize run order against unknown drift. Group runs by known nuisance conditions. Use independent repeat runs at the same settings to estimate pure error; repeated readings of one run are different. Repeated center points can test for net curvature. Add points that identify the curved terms the decision needs.
- Work in stages: screen many factors with few runs, model the few that matter as a response surface to find the best settings, then confirm with fresh runs. Validate the model where the decision will use it; extrapolation needs its own justification.
- **Design against noise in three stages**, as in Taguchi's method. System design chooses the architecture. Parameter design finds settings less sensitive to wear, temperature, and use. Tolerance design tightens only the remaining critical tolerances. Compare the cost of better settings with tighter tolerances. Vary noise deliberately and repeat runs enough to estimate both mean and spread.
- For costly runs, use earlier results to choose the next run by its expected value to the decision and its cost. A Gaussian process can model a few factors with a smooth response. Its uncertainty depends on its assumptions; check it on fresh runs.
- Carry prior knowledge into the analysis as in `principles-ground`.
- Prefer many cheap, fast, reversible experiments over one large one.
- Decide before running what result would kill the idea.
- Record every run, including failures. A failed run is data; an unrecorded one is lost.

## Think big, build small, win

Hold the full vision while you build the smallest piece that proves the hardest part. Prove the riskiest assumption first. Then widen.

Pairs with: before `principles-ground`, `principles-horizons`; after `principles-method`, `principles-verify`, `principles-invert`.
