---
name: principles
description: Choose principles for the task and use the six axes of made things. Use when starting a design, build, review, or decision, or when unsure which skill applies.
---

# Principles

In one line: Set the goal, build the smallest complete version, test it against reality, and use axes where they matter.

Use this map to choose relevant skills and examine important choices. The six axes apply across media; treat them as prompts, not a checklist. Consider an axis when it could change the result or its risks, then check consequential choices against reality.

```
Set the goal -> Check assumptions -> Make -> Predict -> Test
     ^                                                  |
     +--------------- Learn and revise <-----------------+
```

Use `principles-method` to scale the work to its consequences. Load the skills the task needs.

## Choose a skill

| Task | Skills |
|---|---|
| Establish what is true | `principles-ground` for inference; `principles-research` for finding and synthesizing sources |
| Define, collect, and compare measurements | `principles-measure` |
| Diagnose a failure in use | `principles-lessons` for the timeline and causes; `principles-measure` for a baseline before trusting a signal; `principles-ground` for competing explanations |
| Work in a medium | `principles-visual`, `principles-sound`, `principles-touch`, `principles-language`, `principles-interaction`, `principles-information`, `principles-code`, `principles-machine` |
| Create and connect | `principles-design` for choosing an approach; `principles-synthesize` for new approaches; `principles-integrate` for joining parts; `principles-world` for one coherent place; `principles-distribute` for reaching people |
| Structure a decision | `principles-represent` for a useful problem structure; `principles-invert` for reverse questions; `principles-horizons` for consequences; `principles-qualities` for value trade-offs |
| Check the result | `principles-verify` for evidence; `principles-craft` for quality; `principles-secure` for misuse; `principles-reliability` for failures and recovery |
| Learn and improve | `principles-lessons` for events; `principles-refine` for revising toward a quality bar; `principles-improve` for measured gains; `principles-simplify` for less complexity; `principles-loop` for feedback; `principles-compound` for lasting gains |
| Help people and agents | `principles-counsel` for advice; `principles-develop` for growth; `principles-mind` for agent design |
| Extend and close the work | `principles-create` for adding a family skill; `principles-tidy` for task cleanup, documentation, and tool discovery |

## The six axes

| Axis | The question | Visual | Sound | Language | Interaction | Code | Machine |
|---|---|---|---|---|---|---|---|
| **Form** | What shape does it take? | shape, scale, proportion | pitch, interval, envelope | word, sentence length | targets, affordances | types, interfaces | geometry, tolerance, fit |
| **Material** | What is it made of? | color, texture, roughness | timbre, resonance | diction, register | states, feedback | language, data structures, dependencies | alloy, polymer, finish |
| **Energy** | What drives it, and how hard? | light, intensity, falloff | dynamics, attack | emphasis, stress | response, effort, latency | compute, memory, power | work, power, leverage, loads, heat |
| **Observer** | Who meets it, from where? | viewpoint, focus, exposure | listener, room, speaker | reader, prior knowledge | user, context, ability | caller, maintainer, operator | user, operator, inspector, sensor |
| **Composition** | How are the parts arranged? | hierarchy, spacing, balance | arrangement, mix | structure, order | flow, information architecture | modules, coupling, data flow | assembly, load paths, interfaces |
| **Time** | How does it change? | motion, transition | rhythm, tempo, decay | pacing, narrative order | sequence, undo, learning | lifecycle, concurrency, versions | wear, fatigue, maintenance |

Choose an axis on purpose when it can affect the result. Keep a sound default elsewhere.

## Using the axes

1. State intent in one sentence: the purpose, the observer, and the one constraint that binds hardest. If you cannot, run `principles-method` first.
2. Load the medium skill. Consider each axis; explain choices that could change the result or its risks.
3. Make the smallest complete version. Address the relevant axes before spending time on polish.
4. Use `principles-verify` at a depth suited to the work. Use `principles-refine` to fix the most important gap first.

Done means the work meets its intent and `principles-verify` finds no material issue. State the choices and remaining gaps that matter to the result.

## Shared principles

- **Contrast** carries meaning. Perception detects difference, not absolute level. When everything is emphasized, nothing is.
- **Hierarchy** puts one thing first. The observer should know where to start within a second.
- **Proportion** beats size. Relationships between parts read before the parts do.
- **Consistency** builds a language. Break it only to say something.
- **Subtraction** finds the work. Remove parts until removing more would break a stated requirement. Margin and redundancy that guard against failure are requirements.
- **No ruin.** A loss that cannot be undone ends every later gain. Before an irreversible act, have a way back that has been tried.
- **Constraint** creates form. A limit chosen early forces a coherent design; a limit met late forces a patch.
- **The observer completes the work.** Design for their real position, knowledge, attention, and body.
- **Time is an axis.** Everything is met in sequence, changes, and wears.
- **Ground truth lives outside language.** Measure, test, or simulate before you believe a description, your own included.
- **Craft lives in the details nobody asked for.** The observer feels them without naming them.
