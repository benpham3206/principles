# Judgment eval: preliminary results

A small A/B check of whether the guidance changes decisions. It is a smoke test with 3 samples per cell, not proof.

## Setup

- Tasks: 4, one each in mechanical engineering, software reliability, control, and research under uncertainty (`tasks.json`). Each has 5 or 6 key items written before any run.
- Arms: `none` (task only), `old` (task plus the matching skills at `d16de56`), `new` (the same skills at `ae09e1e`; software adds `principles-reliability`).
- Generator: one model for every arm, in a clean room with no user instructions, skills, rules, or tools (`run.py`). 3 samples per task and arm, 36 runs, 0 errors.
- Grader: the same model family, blind to arm, one answer at a time, skill names redacted. 36 grades, 0 unparsed. A grader from a second model family was planned and not run.
- Run: `python3 evals/judgment/run.py generate|judge|report`. Raw runs, grades, and the blinding map are in `data/`.

## Results by arm

| arm | key items met | correctness | failure detection | decision (1-5) | verification (1-5) | output tokens | input tokens | seconds |
|---|---|---|---|---|---|---|---|---|
| none | 0.86 | 0.83 | 0.94 | 4.75 | 4.00 | 648 | 16,699 | 33.4 |
| old | 0.90 | 0.85 | 0.96 | 4.83 | 4.00 | 645 | 18,093 | 30.6 |
| new | 0.93 | 0.92 | 0.88 | 4.83 | 4.33 | 567 | 17,691 | 26.7 |

## Results by key item (samples meeting it, of 3)

| task | item | none | old | new |
|---|---|---|---|---|
| control | rejects faster polling | 0 | 0 | 3 |
| control | delay is the cause | 2 | 3 | 3 |
| software | DB replica shares a zone | 1 | 2 | 2 |
| research | refuses revenue attribution | 3 | 3 | 2 |
| every other item | | same in all arms | | |

## What it shows

- No arm made a different decision. On the control task, all 9 answers rejected faster polling as the fix. The item gap (0, 0, 3) is wording: new-guidance answers said the change is likely to worsen the swings, the others said it is unlikely to fix them and could worsen them, and the key item asked for the stronger claim. That is a difference in stated confidence, read from 9 answers, not a changed decision.
- Mechanical and research tasks hit a ceiling: all arms met nearly every item. Tasks this model already solves cannot show a gain.
- The reliability skill did not beat the old code skill on the software task (same item counts); both beat no guidance on one item, by one sample.
- The one drop (research, new arm, one sample) was a grader judgment that the answer refused attribution without naming the small effect as a reason; the answer did refuse it.
- Cost: the new arm used about 6 percent more input tokens than `none`, about 12 percent fewer output tokens, and finished faster per answer. The grader scored its verification slightly higher (4.33 against 4.00), a subjective score from one grader.
- Verdict: no measured improvement in decisions, and no measured harm, at this model's strength on these tasks. The additions stay on the strength of review and correctness, not of this eval.

## Limits

- 3 samples per cell. A difference of one sample is noise.
- One grader, from the generator's family. Its scores of decision and verification quality are subjective; the key items are the firmer measure.
- Single-turn answers, so iterations to completion were not measured.
- Answers with guidance may echo its words, which a blind grader can still notice.
- The new arm used `ae09e1e`; later review fixes reworded three sentences and did not change any rule an item tests.

## Next

Harder tasks that the unguided model fails, a second grader family, and 10 or more samples per cell would turn this into evidence.
