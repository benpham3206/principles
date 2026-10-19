---
name: interaction
description: Principles of anything a person operates (software interfaces, flows, controls, games, devices, conversational agents, machines with operators), organized on the six axes plus control. Use when designing, directing, or critiquing how something is used, how it responds, or who is in control.
---

# Interaction

An **interaction** is a loop: the person acts, the system responds, the person reads the response and acts again. The person first finds what they can do, then what happened, so every choice is a choice about what they can discover, what they are told, and how long they wait.

## Tree

```
INTERACTION
├── Form          targets, affordances and signifiers, mapping
├── Material      states, feedback, component consistency
├── Energy        response latency, effort, steps, cognitive load
├── Observer      goal, context, device, ability, expertise, distraction, adversary
├── Composition   information architecture, flow, progressive disclosure, choice count, navigation
├── Time          sequence, transitions, undo, learning curve, interruption, long-term use
└── Control       who acts at each moment, handoff, the person in the loop
```

## Form

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Targets | Time to reach a target grows with distance and falls with size (Fitts's law, as a principle: time rises with the log of distance over width). Edges and corners of a screen stop the pointer, so they act as infinitely deep targets | Small targets far from where the hand rests; frequent actions in remote corners | Measure each frequent target. Is it large and near the last action? |
| Affordances and signifiers | An **affordance** is an action the object permits. A **signifier** is the visible cue that tells the person so. Hidden affordances go undiscovered | A control that works but looks inert, or looks live but does nothing | Show it to a newcomer cold. Can they say what is operable and what each part does? |
| Mapping | Control layout should mirror effect layout: the knob nearest a burner works that burner, up raises, right advances | Controls in one arrangement, effects in another, so the person must memorize pairs | Point at a control. Can the person name its effect without a label? |

## Material

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| States | Every element lives in a set of states: empty, loading, partial, error, success, disabled. Design each one, not only the filled one | Only the happy state drawn; empty looks broken, error is a blank | List the states of each element. Is every one designed? |
| Feedback | Every action gets a visible, immediate acknowledgment, and its result reports what changed | Action with no response, so the person repeats it or doubts it | Do an action. Within the latency band, what proves the system heard? |
| Consistency | The same thing looks and behaves the same everywhere; a different thing looks different | Two controls that look alike but act differently, or one action with three shapes | Pick one action. Is it the same component everywhere it appears? |
| Error messages | An error says what happened, why, and what to do next, in the person's terms | Codes, blame, or a message with no next step | Can the person recover using only the message? |

## Energy

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Response latency | Long-standing rules of thumb: about 0.1 s feels instant, about 1 s keeps the train of thought, about 10 s loses attention. Past 1 s show progress; past 10 s let the person leave and return | Silent waits; a spinner with no end in sight | Time the response. Which band is it in, and does the feedback match the band? |
| Effort | Each action costs motion, attention, and memory. Spend the person's effort only on the goal | Effort spent on the system's own needs | Count what the person must do versus what the goal needs |
| Steps | Fewer steps to the goal, and the common path shortest | Rare cases forcing steps on everyone | Count steps on the most common task. Can any go? |
| Cognitive load | Working memory holds only a few items at once; recognition is cheaper than recall | Making the person remember what the screen could show | What must be held in memory between steps? Show it instead |

## Observer

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Goal | The person wants an outcome, not your feature | Layout that mirrors the system's structure, not the task | State the goal in the person's words. Is the path to it plain? |
| Context | Where and when it is used (walking, driving, dim room, noisy floor) sets what works | Designed at a desk, used in a hurry | Test in the real setting, not the studio |
| Device | Input method sets the target size, the gesture set, and what can be hidden | A pointer layout on a touch screen, or the reverse | Test with the real input, the real size, the real hand |
| Ability | Vision, hearing, motor control, cognition, and language vary, and so does one person's ability across a day | One channel carries the message; one precise motion is required | Can it be used with one channel off, by keyboard alone, with a tremor? |
| Expertise | The same person moves from first use to expert. Serve both: guided paths for the first visit, shortcuts for the hundredth | Built only for beginners or only for experts | What does the first minute look like? The thousandth? |
| Distraction | Attention is split and interrupted | Needs unbroken focus; state lost on interruption | Look away for 30 seconds mid-task. Can they resume? |
| Adversary | Some users probe, abuse, or fool the system, and some mistakes are the system's invitation | Trust in input; destructive actions one click from a tap | Try to break it on purpose. What does a hostile or careless person reach? |

## Composition

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Information architecture | Group by the person's mental model, and name by the words they use | Structure that mirrors the organization chart or the database | Card-sort with real users. Do groups match theirs? |
| Flow | One main task has one clear path; everything else steps aside | Competing calls to action; a dead end | Where does the eye go first? Is the next step obvious? |
| Progressive disclosure | Show the common first; reveal the rare on request | Every option on the surface, or power buried with no cue | Is the common 80 percent visible and the rest one step away? |
| Choice count | Decision time rises with the number of options. Cut, group, or default | Long flat menus; choices with no recommended default | Count options at each decision. Can the number halve? |
| Navigation | The person knows where they are, where they can go, and how to return | Lost in depth; no way back; same place reachable by different names | At any screen, can they answer: where am I, what else is here, how do I get back? |

## Time

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Sequence | Order matches the order of the person's thinking: what they know first, then what depends on it | Asking for what the person cannot yet know | Walk the sequence. Does each step have what it needs? |
| Transitions | A change should explain itself: where the thing came from, where it went | State jumps with no cause the person can see | Can they track each object across the change? |
| Undo | Reversibility makes exploration safe. Undo beats confirmation dialogs, which people click through | Irreversible acts with no recovery; a confirmation at every step | For each action: can it be undone? If not, is the person told first? |
| Learning curve | Time to first success, then time to fluency; both can be measured | A steep cliff at the start, or a plateau where nothing improves | Time a newcomer to the first success, and a regular to a repeated task |
| Interruption and resume | Save state as the person works; return them to where they stopped | Work lost on timeout or switch; resume at the start | Close it mid-task and reopen. Where are they? |
| Long-term use | After a year the data piles up, habits harden, and the novelty is gone | Designed for the demo, with a first-day tour but no archive, search, or cleanup | Fill it with a year of data. Does it still work and still look right? |

## Control

Earned because an interaction with an automated system has an owner at each instant, and a failure often lives at the handoff.

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Who acts | At each moment exactly one party is in control, and both know which | Both assume the other has it; or neither does | At this instant, who is acting, and does the person know? |
| Handoff | Handoff states what was done, what remains, and what the next party must check | Automation hands back with no context, during an emergency | Can the receiver act within seconds of the handoff, using only what is shown? |
| Person in the loop | Irreversible, costly, or outward-facing acts need the person's explicit yes, with the effect stated | The system acts, then reports; scope creeps past what was asked | List every irreversible act. Does each need an informed yes? |
| Visibility | The person can see what the system is doing, and can stop it | Hidden activity; no way to interrupt | Can they see current activity and halt it in one action? |

## Laws of the medium

- The person's goal outranks the system's structure. Organize around what they want done.
- Every action gets feedback within the latency band for its cost.
- Make the next step visible and the wrong step hard; make the right step recoverable.
- Reduce what must be remembered. Recognition beats recall.
- Cut steps and choices from the common path; keep the rare path reachable.
- Design for the hurried, distracted, first-time person; the expert will find the shortcuts.
- Friction belongs before irreversible acts only (see `qualities`: agency, trust, smoothness).

## Defaults to replace

The stock empty state, the generic spinner, a confirm dialog on every delete, the blank error, tiny close targets, a flat menu of every option, a tour on first launch, placeholder text used as the label, a modal that blocks without cause, "are you sure?" in place of undo, and an agent that acts first and reports after.
