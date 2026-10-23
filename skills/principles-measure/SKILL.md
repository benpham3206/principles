---
name: principles-measure
description: Define and check measurements. Use when choosing metrics, benchmarking software, measuring physical quantities, calibrating instruments, analyzing dimensions, estimating uncertainty, or comparing measured results.
---

# Measure

A **measurement** assigns a value to a defined quantity through a stated procedure. A useful result says what was measured, under which conditions, against which reference, and with what uncertainty. This procedure applies to software and physical work.

Use `principles-design` to choose the approach and the property a prototype must test. Use this skill to measure that property. Return to design when the result rejects the approach or shows that the prototype cannot answer the question. Use `principles-ground` to reason from the evidence and decide whether more information would change the choice.

## Steps

1. Name the decision the measurement serves. Set the relevant limit or smallest difference that would change the choice, and the other requirements that must hold. Match the effort to the consequence of a wrong reading.
2. Define the quantity before collecting it. Name the object or population, unit, reference frame, boundaries, time window, denominator, and summary statistic as applicable. Separate the property of interest from a proxy for it. A server response time covers a different interval from the time a person waits for a usable result.
3. Choose and check the method. Check resolution, bias, noise, lag, range, and the effect of observing the system. Test known inputs or references across the relevant range. Correct known bias and carry the uncertainty of the correction. A fine display does not establish accuracy.
4. Plan the comparison. Use a baseline and comparable conditions. Record or control workload, environment, initial state, and other causes that can move the result. Use `principles-synthesize` for randomized or blocked experiments and designs that separate factors and interactions. State the sampling and stopping rule before using the results to choose a winner.
5. Collect the readings and their conditions. Sample the population and operating range the claim covers. Distinguish independent runs, specimens, or participants from repeated readings of one. Account for correlation and drift before treating more readings as more independent evidence. Keep failed runs and exclusions with their reasons.
6. Calculate the result and its uncertainty with the model below. Report the spread or tail that the decision depends on; an average can hide stalls, peaks, or variation. State what an interval describes and how it was obtained. Round the result to a precision its uncertainty supports.
7. Compare the result with the decision limit and the other requirements. Judge a difference using the uncertainty of that difference. If the evidence cannot resolve the choice, report it as unresolved. Improve the measurement, gather more independent evidence, or make a bounded decision under uncertainty with `principles-ground`. Leave the record below so another person can repeat the procedure.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Define what the number stands for | A repeatable proxy mistaken for the intended outcome | Could this number improve while the actual goal gets worse? Check the goal separately |
| Tie results to references | A changed clock, scale, or definition appears to be a change in the thing | Can another observer recover the unit, reference, and method? Does a known case give the expected result within uncertainty? |
| Separate resolution, repeatability, and accuracy | Many stable digits conceal a shared error | What sets the smallest step, the spread of repeats, and the possible offset from a reference? |
| Measure under the conditions of the claim | A benchmark or bench test is generalized beyond its workload or environment | Which claimed conditions were sampled, and which remain unchecked? |
| Account for the observer | Profiling changes execution time; probe force changes the dimension | Compare measurement methods or vary the instrument's influence. Does the effect matter at the decision limit? |
| Keep the comparison identifiable | Drift or several simultaneous changes are credited to one intervention | What else changed, and how does the design separate its effect? |
| Keep the evidence behind the summary | An average hides failures, or a discarded run changes the verdict | Can the result be rebuilt from the retained readings, exclusions, and processing steps? |

## References and calibration

Use a reference with a stated value, uncertainty, and relevant conditions. Calibration establishes a relation between indications and reference values; adjustment changes the instrument. Verify the result after adjustment. Recheck references after changes that can alter the measurement.

For physical quantities, metrological traceability belongs to the result. It requires a documented, unbroken chain of calibrations to a stated reference, each contributing uncertainty. A calibrated instrument alone does not establish that a particular result is fit for its use. Check the whole procedure against the required uncertainty.

Reproducible references let measurements survive changes in instruments and standards. When replacing a reference, compare old and new results within their uncertainties. Failure: a reference change looks like progress or drift. Check: can the two sets of results be compared on a common basis?

## Uncertainty and differences

List the important contributions from the reference, instrument, sampling, environment, corrections, and model. Distinguish the spread of individual observations from uncertainty in an estimated mean, percentile, or other result. More repeats reduce uncertainty from independent random variation; they do not remove a shared bias or a missing condition.

Express each contribution as a **standard uncertainty**, an estimated standard deviation, before combining it with others. For the mean of $n$ independent repeats of a stable quantity under the same conditions, the random component is $s/\sqrt{n}$, where $s$ is the sample standard deviation. This reduction applies to the mean, not to the spread of individual readings or shared systematic contributions.

If a certificate reports expanded uncertainty $U = k u$, recover standard uncertainty with $u = U/k$ using its stated coverage factor $k$. For a bound, justify a distribution before converting it to a standard uncertainty. A uniform distribution between $-a$ and $a$ gives $u = a/\sqrt{3}$. Keep a range as a range when a probability model cannot be justified. Failure: unlike uncertainty statements are combined as equivalent magnitudes. Check: can each input's standard uncertainty or retained bound be traced to its data or assumptions?

For a nearly linear calculation, scale each input's standard uncertainty by the result's sensitivity to it. Combine independent terms by the square root of their squared sum. Correlated terms need their covariance. If dependence is unknown, the sum of the absolute scaled terms bounds the combined standard uncertainty within this linear approximation. For strongly nonlinear calculations, propagate justified ranges or joint samples through the calculation itself, preserving dependencies.

For a difference between two results, include the covariance between them. A shared additive bias cancels when it enters both with equal sensitivity; a bias that differs does not. Paired measurements can resolve a difference smaller than the noise of one reading. Failure: an apparent gain depends on treating shared errors as independent, or repeated noise as systematic error. Check: recompute the uncertainty for the actual comparison and its dependencies.

## Dimensions and similarity

| Principle | Failure | Check |
|---|---|---|
| Equations must respect dimensions | A conversion or model adds unlike quantities or hides a missing scale | Do both sides have the same dimensions? Does converting units preserve the physical result? Dimensional consistency is necessary, not proof that the model is correct |
| Use dimensionless groups to expose scale | A small prototype is assumed to behave like a larger system | Form independent dimensionless groups from the governing quantities. With a complete set of quantities, their number is the number of quantities minus the rank of their dimensions |
| Similarity depends on the governing model | Matching size ratios hides changed flow, heat, friction, or boundary conditions | Are the relevant dimensionless groups, operating regime, and boundary conditions comparable? State any unmatched effect before extrapolating |

## Checks by domain

| Domain | Define and record | Failure to expose |
|---|---|---|
| Software | The user or system boundary being timed, elapsed time or CPU time, workload and concurrency, versions, machine, initial state, and measurement overhead. Use a monotonic clock for durations. Separate cold and warm conditions when both occur in use | A warm cache beats a cold baseline; a timer stops before asynchronous work finishes; averages hide tail delays; many requests in one run are counted as independent experiments |
| Physical work | The feature and datum, reference conditions, instrument range, alignment, fixture, contact force, and temperature. Use `principles-machine` for measurement geometry, including Abbe's principle | Angular error at an offset, thermal expansion, or fixture deformation exceeds the claimed difference despite stable readings |

## Measurement record

Keep the question and decision limit, quantity definition, procedure or command, instrument and system versions, references, conditions, raw readings, sampling and exclusion rules, calculation, uncertainty basis, result, and decision together. A manual procedure is repeatable evidence when its setup and observations are recorded. Scale the record to the claim; a single reading still needs a unit and a defined meaning.

Pairs with: before `principles-method`, `principles-design`, `principles-ground`; after `principles-synthesize`, `principles-improve`, `principles-verify`.
