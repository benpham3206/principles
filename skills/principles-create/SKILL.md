---
name: principles-create
description: Create or revise a skill in the Principles family. Use when adding a family skill, choosing its scope, or checking that its format and discovery match the library.
---

# Create

In one line: Add a skill only when a distinct task needs guidance no existing skill supplies; otherwise extend one.

A skill earns a place when a distinct task needs guidance that existing skills do not supply. Use this procedure to make a Principles skill. Keep the rules in the repository instructions as the source of its format.

## Steps

1. State the task, intended reader, trigger, and observable result. Name one realistic request the skill should handle and one nearby request it should leave to another skill.
2. Read the map and the closest existing skills. Compare their actual instructions, not just their names. Extend an existing skill when the new guidance serves the same trigger and result. Create a skill when independent discovery or a separate decision path earns the extra context cost. Report the overlap and the reason for the choice.
3. Read the target repository's instructions and one representative skill. Work outside an installed copy that agents load. Follow the medium skill shape when the new skill concerns a medium; otherwise choose steps, reference, or both to fit the task.
4. Write `skills/<name>/SKILL.md`. Use a lowercase name with hyphens and matching frontmatter. Give the description distinct triggers. Put the purpose, binding limits, and first useful action near the top. Add supporting files only when a real branch needs them.
5. Write principles that change a decision. For each, name the failure it prevents and a check that can expose that failure. State limits where a heuristic could be mistaken for a guarantee. Keep the six axes in the map and use them by reference.
6. Make the procedure portable. Read project conventions from their source. Use an available specialist tool when it helps, and supply a direct path when it is optional. Declare any real prerequisite before the step that needs it. Preserve the user's scope and authority.
7. Connect discovery. Add the skill to the README and map. Add relevant `Pairs with:` links and check that another skill can reach it. Give each shared rule one home; link to it where needed.
8. Validate the complete change. Run the repository's verify command and an available skill format validator. Read every new instruction and resolve its references. Walk the realistic request and the nearby request through the instructions. Check that each path ends in an observable result without assuming the missing tool exists. Use `principles-measure` when claiming a measured improvement.
9. Obtain independent review when the repository requires it or the skill controls consequential actions. Fix material findings before publication. Use the host's reviewed installation path; retain its receipt. Keep the authored source separate from the installed copy.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Earn a separate trigger | A second skill repeats an existing workflow under a new name | Which request now reaches useful guidance that it could not reach before? |
| Standardize the contract | Every skill invents a different way to declare purpose, scope, and completion | Can a reader find the trigger, limits, action, and result in the family's usual places? |
| Teach the decision | A checklist lists activity without saying when a choice is sound | Give the reader a changed case. Can the instructions still guide the choice? |
| Keep one authority | Copied rules drift between the skill and repository instructions | Trace each shared rule to its source and remove duplicate definitions |
| Prove the path | A valid document assumes a tool, context, or permission the reader lacks | Walk a fresh reader through a realistic task with optional tools absent |
| Retire as well as add: merge or remove entries that no longer serve a distinct need, since every entry raises the cost of each later choice | Overlap and dead entries pile up until the right one cannot be found | When was each entry last the right answer to a real request, and what would merging or removing it change? |

## Completion

The skill has a distinct purpose or the existing skill has been extended. Its format checks pass, discovery reaches it, and review findings are resolved or reported. Report the source path, overlap, validation, and installation status separately. A file on disk alone does not prove a harness can discover it.

Pairs with: before `principles-method`, `principles-language`, `principles-mind`; after `principles-verify`, `principles-tidy`.
