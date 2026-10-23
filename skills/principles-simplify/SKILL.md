---
name: principles-simplify
description: Remove complexity while preserving what matters. Use when work is cluttered, repetitive, hard to understand, or costly to change, or when asked to simplify it.
---

# Simplify

**Simplification** reduces what someone must understand, operate, or maintain while preserving the intended result. Fewer words or parts help only when the difficulty has not moved elsewhere.

## Steps

1. Name the purpose, the person using the work, and what must stay true. Include safety, accessibility, error handling, and useful distinctions.
2. Find the source of difficulty: repeated facts, unnecessary choices, hidden state, extra steps, or parts that exist only to support other parts.
3. Try deletion first. Then combine duplicates, use an existing convention, or make the remaining relation explicit. Use `principles-language` for words and `principles-integrate` for boundaries.
4. Compare the whole before and after. Include callers, instructions, recovery, and work passed to other people or systems. A shorter front end with harder upkeep is a trade-off, not a clear reduction.
5. Check the preserved requirements with `principles-verify`. Stop when the next cut would lose a required result or make the work harder to use.

## Failure checks

| Principle | Failure | Check |
|---|---|---|
| Remove the cause of complexity | Renaming or moving parts leaves the same work to do | Which step, choice, state, or fact no longer needs upkeep? |
| Keep one home for each fact | Copies drift apart | Can one edit update the rule wherever it is used? |
| Preserve needed distinctions | A shorter rule merges cases that need different actions | Try two such cases. Does each still lead to the right action? |
| Keep context at the point of use | Detail moves behind a link nobody knows to open | Can a new reader finish the task and find its limits? |
| Preserve intentional richness | Minimalism removes texture, expression, or depth the person values | Does the result still serve the stated experience? |

Examples: replace duplicate instructions with one source and a clear reference; keep separate controls when they perform different actions. A backup or a recovery path can be necessary even when the usual path never uses it.

Pairs with: before `principles-language`, `principles-integrate`, `principles-verify`; after `principles-improve`.
