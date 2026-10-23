---
name: principles-synthesize
description: Invent something new by working backward from a goal too large for known solutions. Use for Herculean goals, novel products or research, combining ideas across fields, designing experiments, or choosing settings that tolerate noise, or when every obvious answer has already been tried.
---

# Synthesize

**Synthesis** is making something that did not exist by combining known truths in a new arrangement. It runs on one loop: what is true (cognitive), what is possible (generative), and is it true (recognitive).

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
3. **Work backward to a plan.** List each step from today to that output, and the technology each step needs. Mark each technology as existing, existing but too costly, or not yet invented.
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

- **Vary several factors at once** in a designed experiment, choosing a design that can separate the effects and interactions the decision needs, and state which remain confounded. Such a design can estimate interactions that changing one factor at a time cannot see. Several changes in one uncontrolled before-and-after comparison do not identify their separate effects.
- Choose which experiment to run by its value to the decision, as in `principles-ground`.
- Factorial designs and their fractions, such as orthogonal arrays, are the standard forms. A fraction buys fewer runs by confounding some effects with others; state which.
- Randomize run order against drift you cannot see, block on nuisances you can, and repeat runs to measure pure error. Center points reveal curvature.
- Work in stages: screen many factors with few runs, model the few that matter as a response surface to find the best settings, then confirm with fresh runs. A fitted model holds only inside the region it was fitted on.
- **Design against noise in three stages.** System design chooses the architecture. Parameter design chooses the settings that make performance insensitive to noise you cannot control, such as wear, temperature, and use. Tolerance design then tightens only the tolerances that still matter. Insensitivity bought with settings is usually cheaper than precision bought with tolerances. Vary the noise on purpose in the experiment, and model the mean and the spread separately.
- When each run is costly, choose runs one at a time with a model that carries its own uncertainty, such as a Gaussian process, placing the next run where the model is most promising or least known. It suits a few factors and smooth responses; check it on runs it has not seen.
- State what was known before as a prior, update it with the data, and show how much the conclusion depends on the prior. When the data are few, the prior decides; say so.
- Prefer many cheap, fast, reversible experiments over one large one.
- Decide before running what result would kill the idea.
- Record every run, including failures. A failed run is data; an unrecorded one is lost.

## Think big, build small, win

Hold the full vision while you build the smallest piece that proves the hardest part. Prove the riskiest assumption first. Then widen.

Pairs with: before `principles-ground`, `principles-horizons`; after `principles-method`, `principles-verify`, `principles-invert`.
