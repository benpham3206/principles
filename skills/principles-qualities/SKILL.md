---
name: principles-qualities
description: Choose which qualities matter most. Use when setting a design philosophy, choosing fluid or textured presentation, or resolving a conflict between useful values.
---

# Qualities

A **quality** is a property an observer experiences in finished work. Qualities can conflict. A **design philosophy** states which one takes priority and why.

## The qualities

| Quality | What it is | Test | Failure |
|---|---|---|---|
| **Intention** | Every part exists for a stated reason | Can you say why each part is there? | Parts added because they were easy or expected |
| **Agency** | The observer stays in control of what matters to them | Can they undo, stop, choose, and see what happens? | Choices made for them, without their knowledge |
| **Responsibility** | The maker owns the consequences, including misuse and failure | What happens on the worst day? Who carries it? | Harm pushed onto users, bystanders, or the future |
| **Familiarity** | It uses conventions the observer already knows | Does a newcomer get it without a lesson? | Novelty where convention would have worked |
| **Flexibility** | It adapts to uses the maker did not foresee | Does it still work at other sizes, users, and contexts? | Brittle fit to one case |
| **Simplicity** | The fewest parts that meet the need | What could you remove? | Complexity that has not earned its place |
| **Craft** | Care visible at every scale | Does it hold up close? | Polish on the surface, neglect underneath |
| **Delight** | A moment of joy beyond function | Does anything make the observer smile, and does it serve them? | Delight that costs time or clarity |
| **Time** | It respects the observer's time and ages well | How long to the first useful result? How does it look in ten years? | Waiting, trends that date, wear that ruins it |
| **Trust** | It behaves as promised, every time | Does behavior match appearance and claims? | Surprises, hidden states, broken promises |
| **Smoothness** | Transitions between states are continuous and expected | Can you see a seam, hear a click, feel a stutter where none is meant? | Jank, abrupt jumps, mismatched rhythm |

## Fluid or textured

Every design language sits on a dial between two poles.

- **Fluid**: continuous, low friction, unbroken transitions, mechanism hidden. It suits flow states, frequent tasks, and calm.
- **Textured**: discrete steps, tactile feedback, mechanism visible, friction on purpose. It suits deliberate actions, irreversible acts, and craft that wants to be seen.

Choose a position per intent and hold it across every axis. A fluid surface over textured behavior, or the reverse, reads as a mistake. Friction is a tool. Put it in front of irreversible actions, and remove it everywhere else.

## Senses and flow

The senses are the channels: sight (`principles-visual`), sound (`principles-sound`), touch (`principles-touch`). **Flow** is the direction of travel through the work: reading order, signal path, load path, data flow, the user's journey. Every work has one. Make it single, obvious, and continuous across the senses. A click you hear should match the motion you see and the detent you feel.

## Resolving conflicts

Common conflicts and the usual resolution. These are defaults; the stated philosophy overrides them.

| Conflict | Usual resolution |
|---|---|
| Simplicity and flexibility | Simple by default, flexible on demand. Hide power until it is asked for |
| Familiarity and delight | Familiar structure, delight in the details |
| Smoothness and agency | Smooth for reversible actions, deliberate friction for irreversible ones |
| Craft and time | Craft where the observer touches; speed where they never will |
| Trust and novelty | Novel only where you can keep the promise every time |

## Writing a design philosophy

1. State the intent and the observer.
2. Rank the qualities for this work. The top three decide most conflicts.
3. Place it on the fluid to textured dial.
4. Name one reference that embodies it and one that violates it.
5. Write it in five lines or fewer, so every maker on the project can hold it in their head.

Pairs with: before `principles-method`, `principles-world`; after `principles-visual`, `principles-sound`, `principles-touch`, `principles-language`, `principles-interaction`, `principles-information`, `principles-machine`.
