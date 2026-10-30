---
name: principles-interaction
description: Design how people operate a system. Use when shaping controls, flows, visual or sound feedback, response times, discoverability, recovery, permissions, or handoffs with automation.
---

# Interaction

In one line: Make each action, its result, the wait, and who holds authority clear to the person in the loop.

An **interaction** is a loop: a person acts, perceives the system's response, and acts again. Automation can execute parts of the loop. Make actions, results, waiting time, and authority clear for the actual goal, setting, abilities, and consequences of error.

## Laws of the medium

- The person's outcome outranks the system's internal structure. Organize work around their task.
- Make possible actions, relevant state, and consequences perceivable and operable. Do not rely on a single sensory channel when another is needed for access.
- Acknowledge an action, distinguish progress from completion, and report a result or failure within timing appropriate to the task and its risk.
- Prevent consequential mistakes where practical and provide a path to recover. Add friction where it earns its cost through risk control, consent, security, error prevention, or deliberate tactile feedback.
- Reduce unnecessary steps and memory demands without hiding necessary information, safeguards, or uncommon paths.
- Make the system's authority boundaries legible: what a person has authorized, what automation is doing, what can still be changed, and who can intervene.
- Serve beginners, experienced people, interruptions, and varying abilities without forcing one path on everyone.

Use the timing bands as starting heuristics and the movement and choice models within their stated assumptions. Test the result in its actual use.

## Defaults to replace

The stock empty state, the generic spinner, a confirmation on every reversible delete, the blank error, tiny close targets, a flat menu of every option, an unsolicited first-launch tour, placeholder text as the only label, a blocking modal without cause, color or sound as the only status cue, identical tones for different alerts, confirmation in place of recovery, and an agent that silently exceeds the authority it was given.

## Tree

```text
INTERACTION
├── Form          targets, affordances and signifiers, mapping
├── Material      states, visual and sound feedback, component consistency
├── Energy        response latency, effort, friction, steps, cognitive load
├── Observer      goal, context, device, ability, expertise, distraction, adversary
├── Composition   information architecture, flow, progressive disclosure, choice count, navigation
├── Time          sequence, transitions, undo, learning curve, interruption, long-term use
└── Control       authority, execution, responsibility, consent, handoff, intervention
```

## Form

| Leaf | Principle | Failure | Check |
| --- | --- | --- | --- |
| Targets | Fitts's law models rapid aimed movement: acquisition time generally rises with distance and falls with target width along the approach. A screen edge helps only when it stops overshoot. Check other input methods separately. | Small or closely packed targets, or pointer assumptions applied to touch. | Test frequent targets at real size with the actual input method. Can they be reached reliably? |
| Affordances and signifiers | An **affordance** is an action an object permits; a **signifier** indicates that action. Signifiers need to be perceivable, including to assistive technology. | A working control looks inert, a decorative element looks actionable, or an unlabeled control is invisible to a screen reader. | Can a newcomer identify the operable elements and their effects with the intended input methods? |
| Mapping | Arrange controls and outcomes so their relationship is predictable; use clear labels when spatial mapping alone cannot carry meaning. | Arbitrary control-effect pairings that must be memorized. | Can a person predict an effect before acting, using the available cues? |

## Material

| Leaf | Principle | Failure | Check |
| --- | --- | --- | --- |
| States | Design the states each element can actually enter: empty, loading, partial, error, success, disabled, or pending approval where relevant. | Only the happy state works; waiting, partial results, and recovery are ambiguous. | Enumerate reachable states and transitions. Is each understandable and operable? |
| Feedback | Acknowledge input through a perceivable channel; distinguish receipt, progress, completion, and side effects. | A silent action is repeated, or an acknowledgment is mistaken for success. | After acting, can the person tell what was received, what is pending, and what changed? |
| Visual feedback | Use hierarchy, labels, contrast, and focus to make actions and state changes legible. Use `principles-visual` for appearance. | Color alone carries status; decoration hides a control; a change occurs outside attention. | At actual size, can the person find the next action and notice its result? Check without color and with nonvisual access. |
| Sound feedback | Give useful cues distinct meaning and urgency. Use `principles-sound` for audibility, masking, and repetition. Provide accessible alternatives and control over optional sounds. | Alerts merge, interrupt speech, tire the listener, or carry the only record of an event. | Test in noise, at low volume, on small speakers, and muted. Is the event still clear, with a record when needed? |
| Consistency | The same action should behave predictably across contexts; different consequences deserve distinguishable signals. | Controls look identical but have different effects, or one function changes behavior without reason. | Compare equivalent actions across surfaces. Are differences justified by context or accessibility? |
| Error messages | State what failed, what is known or uncertain about why, and the next safe action in the person's terms. Preserve work and avoid disclosing sensitive details. | Codes, blame, invented explanations, lost input, or no recovery step. | Can the person recover or escalate using the message and retained state? |

## Energy

| Leaf | Principle | Failure | Check |
| --- | --- | --- | --- |
| Response latency | For ordinary interface responses, about 0.1 s can feel immediate, 1 s can preserve the train of thought, and 10 s can strain attention. These are starting heuristics, not deadlines. Direct manipulation and urgent tasks can need tighter timing. | Silent waits, false precision, or a spinner that conceals stalled work. | Measure acknowledgment and completion under representative load. Does feedback fit the wait? Can people recognize stalled work and leave and return where safe? |
| Effort | Each action costs movement, attention, and memory. Spend effort where it advances the goal or protects an important constraint. | Repeated work serves the system rather than the person's task. | Count the required motions, decisions, and remembered facts. What has a justified purpose? |
| Friction | Add effort where its benefit earns the cost: risk control, consent, security, error prevention, or deliberate tactile feedback such as a detent. Use `principles-touch` for physical feel. | Confirmation fatigue, safeguards removed for speed, or resistance that excludes users. | Name what each added step or resistance protects or communicates. Test errors, effort, and an accessible alternative. |
| Steps | Keep frequent, low-risk paths direct while preserving deliberate checkpoints where consequence warrants them. | Rare cases add steps for everyone; needed approvals are optimized away. | Compare common-path completion and error rates before and after removing a step. |
| Cognitive load | Favor recognition, accessible state, and meaningful grouping over unaided recall. | The person must remember information the system already has. | What must be held in memory across screens? Can the system display or preserve it? |

## Observer

| Leaf | Principle | Failure | Check |
| --- | --- | --- | --- |
| Goal | The person seeks an outcome, not a feature. | Navigation mirrors the internal architecture rather than the task. | State the goal in the person's words. Can they identify the next useful action? |
| Context | Physical and social conditions constrain attention and input. Safety-critical situations may require less interaction, not a different prompt. | A calm desktop layout is assumed to work while moving, under stress, or in noise. | Test in representative conditions without encouraging unsafe use. |
| Device | Input modality and display determine reachable targets, feedback channels, and discoverable actions. | A pointer-first layout is assumed to work on touch or keyboard. | Test the actual device, scale, and alternate input. |
| Ability | Vision, hearing, motor control, cognition, and language vary between people and across time. Support accessible controls, status, focus, and alternatives to precise or timed actions. | Meaning is carried by color or sound alone; a gesture or timed response has no alternative. | Can the task work with keyboard and assistive technology, reduced motion, and different sensory or motor abilities? |
| Expertise | The same person may need guidance on first use and shortcuts later. | Forced onboarding for experts or hidden fundamentals for new users. | Observe first success and repeated expert use. Can both complete the task without needless steps? |
| Distraction | People switch context; make partially completed work recognizable and recoverable. | Interruptions cause lost work or uncertainty. | Leave mid-task and return. Are the next action and previous state clear? |
| Adversary | Treat input and delegated actions as potentially mistaken, malformed, or hostile; constrain authority rather than relying on compliant behavior. | Untrusted input gains authority; a careless action causes disproportionate damage. | Try misuse, boundary crossings, and malformed inputs. What can they affect? See `principles-secure`. |

## Composition

| Leaf | Principle | Failure | Check |
| --- | --- | --- | --- |
| Information architecture | Group and name things using the person's understanding of the domain. | Organization chart or database tables determine navigation. | Can representative people locate tasks and explain the groupings? Use a card sort if grouping is uncertain. |
| Flow | Give each important task a clear route and explicit exits; secondary actions need not disappear. | Competing actions, dead ends, or no way to abandon a process. | Can someone start, finish, cancel, and recover from the task without guidance? |
| Progressive disclosure | Prioritize common tasks while making uncommon options discoverable; never conceal a consequence or safeguard essential to consent. | Every setting competes at once, or critical information is buried. | Can a newcomer find the common action and an expert reach the necessary exception? |
| Choice count | Hick-Hyman findings concern response selection among known stimulus-response alternatives under controlled conditions. A menu also involves search, familiarity, and meaning. Group or recommend choices when it helps the task. | A flat menu overloads; excessive reduction removes meaningful alternatives. | Measure choice accuracy and time, including familiar choices and search for an unfamiliar one. |
| Navigation | Convey location, available destinations, and a safe way back. | The person gets lost or loses the work while returning. | Can a person say where they are, what remains, and how to return? |

## Time

| Leaf | Principle | Failure | Check |
| --- | --- | --- | --- |
| Sequence | Ask for information when the person can reasonably know it; surface dependencies before committing. | The flow requests answers that depend on unseen later steps. | At each step, are prerequisites and consequences available? |
| Transitions | Show enough continuity that a person can track meaningful state changes; accommodate reduced-motion preferences. | Important objects disappear or states change without explanation. | Can someone explain what changed without relying on animation alone? |
| Undo | Prefer reversal and recovery over routine confirmations. Distinguish true undo from compensation, which can leave external effects. Explain residual effects and obtain authorization before commitment. | Confirmation fatigue, irreversible mistakes, or false promises of undo. | What can be restored, what remains visible to others, and is the action covered by informed authorization? |
| Learning curve | Measure time to first success and time to proficiency. Judge trade-offs against the intended users and task. | Unnecessary onboarding or no improvement for regular users. | Compare newcomer first-success time with repeated-task performance. |
| Interruption and resume | Preserve work and restore context where feasible, while respecting security and privacy boundaries. | Timeouts, app switches, or device changes erase progress. | Interrupt the task and return. Is saved state sufficient and appropriate? |
| Long-term use | Design for accumulated data, changed habits, maintenance, and eventual exit. | A compelling demo degrades at real scale or traps accumulated work. | Test with representative long-lived data. Can the person find, clean up, export, and leave? |

## Control

Distinguish **authority** (who may decide), **execution** (who does the work), and **responsibility** (who must monitor, respond, and answer for the outcome). Several parties can execute at once. Coordinate exclusive access where conflicting actions would cause harm.

| Leaf | Principle | Failure | Check |
| --- | --- | --- | --- |
| Who acts | Show active executors, their authorized scope, and pending decisions. Coordinate actions on shared resources. | The person assumes an agent is waiting while it acts, or both sides assume the other will intervene. | At this moment, who is executing, who can authorize the next consequential step, and who can stop or revise it? |
| Responsibility | Assign monitoring and response, and name the person or role that answers for the outcome. Give each party the means and time to act. | Everyone assumes someone else will notice or intervene. | Who detects a failure, who responds, who answers for the outcome, and what happens if a party is unavailable? |
| Handoff | Transfer state, completed work, uncertainty, remaining decisions, and urgency. Keep responsibility assigned until receipt is established. | Automation returns an ambiguous result or demands action without sufficient context. | Can the receiver act from the handoff alone in the available time? What happens if they do not receive it? |
| Person in the loop | Obtain informed authorization from someone entitled to grant it. Prior authorization may cover consequential acts within explicit bounds on actions, resources, duration, cost, and external effects. Provide review, revocation, and safeguards proportionate to risk. Applicable rules may require fresh approval. | Consent is bypassed, approvals are repeated mechanically, or scope silently expands. | Does the grant cover this action and its consequences? Can it be inspected and revoked? Request new authorization before exceeding a bound, accepting greater risk, or taking a step that requires fresh approval. |
| Visibility and intervention | Show activity and results. Explain what pause or stop affects, what is still running, and which effects are committed. Provide timely containment or escalation when stopping is unsafe or impossible. | Hidden automation, a stop button that only hides the display, or an implied reversal of committed effects. | Interrupt before and during commitment. Can the person tell what stopped, what remains, and how to contain further harm? |

Use `principles-secure` to enforce authority boundaries outside the actor. Use `principles-verify` to check the main task through waiting, failure, interruption, handoff, and recovery. Distinguish design predictions from observed use.

Pairs with: before `principles-method`, `principles-craft`, `principles-language`, `principles-visual`, `principles-sound`, `principles-touch`, `principles-secure`; after `principles-verify`.
