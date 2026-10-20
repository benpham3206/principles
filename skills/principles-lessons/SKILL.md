---
name: principles-lessons
description: Learn from failures, near misses, and successes, then move forward. Root cause analysis, blameless reviews, turning a lesson into a check, and closing the loop. Use after an incident, a bug, a missed goal, a surprise, or a project ends.
---

# Lessons

A **lesson** is a change in what a person, team, or system does next, caused by something that happened. A conclusion written down that changes nothing is a note, not a lesson. The test of learning is the next time: the same cause meets a check, a design, or a habit that stops it.

`principles-method` calls for root causes in its refine step; this skill is how to find them and make them stick.

```
EVENT ----> FACTS ----> CAUSES ----> CLASS ----> CHANGE ----> CHECK ----> CLOSE
what        timeline,   why it       every       design,      the test    record it,
happened    evidence,   was          case like   check, or    fails when  stop carrying
            no blame    possible     this one    habit        cause back  it, move on
```

## Laws

- The same cause will return until the system changes. People change slowly; designs change once.
- Blame ends learning. People report what is safe to report.
- Hindsight makes every past choice look obvious. Judge decisions by what was known when they were made.
- Evidence decays. Collect it before the analysis, not after.
- The cheapest lesson is the near miss. Pay attention before the bill arrives.

## Defaults to replace

A single root cause, "human error" as a finding, "be more careful" as the action, a review only after harm, a write-up with no owner or date, a fix with no test that fails without it, a timeline written after the cause was chosen, a lesson filed where no one will meet it, and the same failure reviewed for the third time.

## Steps

1. Stabilize first. Stop the harm, restore service, keep the part. Analysis waits until nothing is getting worse, and evidence waits for no one, so preserve it now.
2. Write the facts as a timeline: what happened, when, what each person saw and did, and what they believed at that moment. Mark each item as observed, reported, or inferred.
3. Find the causes. Ask why it was possible, not who did it. Follow each branch until you reach something that can be changed by design.
4. Name the class. Ask where else the same cause lives: other parts, other code paths, other projects, other people facing the same trap.
5. Choose the change, strongest form first: remove the hazard, then make the error impossible, then make it detectable, then train or document. A reminder is the weakest fix.
6. Add the check. Write the test, alarm, review item, or gate that would have caught it. Confirm it fails with the cause present and passes with it removed.
7. Close. Record the lesson where the next person will meet it, assign each change an owner and a date, and stop re-arguing the event. Moving forward is the point.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Facts before causes | A cause chosen in the first hour, and evidence gathered to fit it | Was the timeline written before any cause was named? |
| Ask how it was possible, not who | A person blamed, so the next person hides the next mistake | Would someone in the same seat, with the same information, have done the same? If yes, the cause is the seat |
| Local rationality | Hindsight calls an action obviously wrong | Rebuild what the person knew at the moment. Did the action make sense then? |
| Causes are plural | One root cause named, the other contributors left in place | Does the cause tree have more than one branch? If not, ask what else had to be true |
| Stop at a changeable cause | "Human error" or "bad luck" as the answer | Can someone change this by design next week? If not, ask why once more |
| Each why needs evidence | A chain of plausible guesses that reads like an explanation | Is each link backed by an observation, a measurement, or a reproduction? |
| Reproduce before you claim | A fix shipped for a cause never shown | Can you make it fail on demand, then stop it failing by removing the cause? |
| Fix the class, not the instance | The same failure returns in a neighboring part | Search for every other place the cause can act. Is each one covered? |
| Prefer design over vigilance | "Be more careful" as the action item | Rank the fix: eliminate, prevent, detect, warn, train. Is a stronger rank possible? |
| A lesson is a check | A write-up that changes nothing | What test, gate, or rule would catch it next time? Is it in place and seen to fail? |
| Learn from near misses | Only harm triggers review, so cheap warnings go unread | Do near misses and surprises get the same short review as failures? |
| Learn from success | Wins credited to skill and never examined | What went right, and was it design or luck? Would it hold under a worse day? |
| Severity sets depth | A full review for a typo, or a one-line note for a lost vehicle | Does the depth of review match consequence, as in the gate of `principles-method`? |
| Close the loop | Action items open for months, then forgotten | Does every action have an owner and a date, and was each one verified done? |

## Finding causes

- Work backward from the effect on a cause tree. Each node is something that had to be true for the node above it. Keep branches that evidence supports; mark the rest as untested.
- Separate three layers: the trigger (what set it off), the conditions (what let the trigger cause harm), and the defenses (what should have caught it and did not). Most lasting fixes sit in the conditions and the defenses.
- Ask what changed. Compare the failing case with the last working one: code, material, supplier, load, operator, procedure, weather. The difference is where to look first.
- Look for the missing barrier. Every serious failure passed through several holes lined up. Each hole is a fix.
- Suspect the system when the same failure has many owners. A trap that catches different people is a design fault.
- Stop at about five levels of why (a rule of thumb). Fewer usually stops at a symptom; many more usually leaves what anyone can change.

## Moving forward

- Decide, then let it go. Once the changes are owned and the checks are in place, the event is closed. Return to it only when new evidence arrives.
- Keep the lesson short enough to be read. One sentence of cause, one of change, and a link to the check.
- Put the lesson where the work happens: in the test suite, the checklist, the template, the design rule. A lesson kept only in a report is forgotten with the report.
- Promote the class. When a lesson applies beyond this project, move it into the shared template, standard, or tool, so the next project starts with the guardrail.
- Prune old lessons. When a design change removes the hazard, retire the rule that guarded against it.
- Watch for repeats. A failure that returns means the last lesson fixed an instance, not the class. Review the lesson, not only the failure.

Pairs with: before `principles-verify`; after `principles-improve`, `principles-compound`.
