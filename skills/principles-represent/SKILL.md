---
name: principles-represent
description: Choose a structure that makes a problem easier to solve. Use before planning tangled work or choosing among flows, trees, state machines, graphs, and matrices.
---

# Represent

In one line: Choose the structure that reveals the answer or next action, not the tidiest picture.

A **representation** names parts and their relations while leaving out other detail. Choose one that reveals an answer or next action. A tidy picture that hides the hard part has not helped.

This skill picks the structure. To show it honestly and readably, use `principles-information`. For how it looks, use `principles-visual`.

```
Name the question -> Choose a structure -> Sketch -> Read -> Act
```

## Laws

- Solving a problem is often finding the representation in which the answer is obvious. Try a second form before working harder in the first.
- Structure before polish. A sketch with the right relations beats a finished render of the wrong ones.
- One view, one relation. Combine views by placing them side by side, never by overlaying meanings. The rules for marks and lines are in `principles-information`.
- Conservation is a free check. Anything that flows must balance; use the balance to find what is missing.
- The representation is not the problem. Test what it shows against the real thing before acting on it.
- Delete what the question does not need. Every part left in must help answer it.

## Defaults to replace

A bulleted list where the parts have relations, a block diagram where the arrows mean three things, a flowchart drawn for something that is really a state machine, a tree whose branches overlap, a schedule with no dependencies, a flow with no quantities, a decision matrix with no stated weights, a slide of every box at every zoom level, and a diagram that ends without a next step.

## Steps

1. Write the question the representation must answer, in one sentence. A structure built to show everything answers nothing.
2. Find the dominant relation among the parts. Ask what connects them: something flowing, one thing following another, one containing another, one depending on another, one causing another, or options being compared.
3. Pick the form from the table below. When two relations both matter, draw two views rather than one diagram that mixes them.
4. Sketch it at the lowest fidelity that holds the structure: boxes, arrows, and labels. Name every part with the word the people involved use.
5. Read it. Look for the largest flow, the longest path, the loop, the empty cell, the box nobody owns, the arrow nobody can explain. That is where the work is.
6. Write the actions. Each finding becomes a step with a verb, an owner, and a check that shows it is done. Order the steps by the dependencies the representation exposed.
7. Redraw when the problem changes. A representation is a model; when reality moves, the model goes stale.

## Problem shape to form

| Dominant relation | Form | What it reveals | Failure |
|---|---|---|---|
| Something flows and is conserved (energy, mass, money, time, people) | Sankey or flow balance: band width proportional to quantity | Where most of it goes, where it is lost, which split is worth attacking first | Inputs and outputs that do not balance, so a loss or a double count hides in the gap |
| Steps follow one another, with choices | Flowchart | Branches, dead ends, loops, the path most cases take | Decisions with an unlabelled branch; no end state |
| Steps pass between actors | Swimlane or sequence diagram, one lane per actor | Handoffs, waits, who blocks whom | Lanes for roles that never act; a handoff with no message named |
| A thing has modes and switches between them | State machine: states as nodes, events as labelled edges | Missing transitions, unreachable states, states with no exit | Two states that differ only in name; an event with no defined effect in some state |
| A whole splits into parts | Tree: issue tree, work breakdown, goal decomposition | Gaps and overlaps, the size of each branch, where to start | Children that overlap or do not add up to the parent |
| Tasks need other tasks first | Dependency graph, directed and with no cycles | The critical path, what can run in parallel, what blocks the most | A cycle, which means the plan cannot start; dependencies left implicit |
| A system has parts and interfaces | Block or architecture diagram at one zoom level; an interface matrix for many parts | Boundaries, data or load paths, the interfaces that need a contract | Several zoom levels on one page; an arrow that means data in one place and control in another |
| Effects feed back on causes | Causal loop diagram, each link marked same or opposite direction | Reinforcing loops that run away, balancing loops that resist change, delays | A loop drawn without its sign, so its behavior cannot be read |
| Many possible causes for one effect | Cause tree or fishbone, then a test for each branch | Which causes are tested, which are guessed | Branches ranked by opinion rather than by evidence |
| Options compared on criteria | Decision matrix: options as rows, criteria as columns, weights stated | The criterion that decides it, options dominated on every column | Weights chosen after the scores to favor a winner |
| Two variables split the field | Two-by-two matrix | Which quadrant each item sits in and what to do in each | Axes that are not independent; every item in one quadrant |
| Events in time | Timeline or schedule bar chart | Overlaps, slack, what falls on the same date | No dependencies shown, so a slip looks local when it is not |
| Things in space | Map, plan, or section drawing to scale | Distances, clashes, access, routes | Not to scale while being read as if it were |

## Principles

| Principle | Failure | Check |
|---|---|---|
| The representation serves one question | A diagram of everything known, so nothing stands out | Can a stranger say what question it answers? |
| Completeness is checkable | A tree or flow that looks finished but leaks | Do the children add up to the parent? Do inputs equal outputs plus losses? Does every state have an exit? |
| Show quantity where quantity decides | Equal-sized boxes for a part that is most of the cost and a part that is none of it | Is the biggest thing drawn biggest, or labelled with its number? |
| Name the unknowns | Guesses drawn with the same weight as facts | Mark each part as measured, estimated, or assumed (see `principles-ground`) |
| Chunk to what a reader can hold | Thirty boxes on one level | More than about seven items on one level (a rule of thumb) means a missing grouping |
| One zoom level per view | System context, modules, and functions on one page | Could every box on the page be described at the same level of detail? |
| A representation ends in actions | A clear diagram and no change in what anyone does | List the steps it implies. If there are none, it was decoration or the question was wrong |
| Keep it as text when it must change | A diagram nobody updates because redrawing costs an hour | Can it be regenerated from a text source or the data itself, and diffed? |

## Reading a representation for action

- The widest band in a flow is the first target. Cutting a small loss twice is worth less than cutting the largest once.
- The longest path in a dependency graph sets the finish date. Shorten it, or the rest does not matter.
- A cycle in a dependency graph is a decision nobody has made. Break it by deciding.
- An empty cell in a matrix is a question: missing data, an impossible combination, or an untried option.
- A box with no owner is where the work stops.
- A reinforcing loop with no balancing loop grows until something outside breaks.
- An arrow nobody can explain is either an interface to specify or a relation to delete.

Pairs with: before `principles-method`; after `principles-integrate`, `principles-verify`.
