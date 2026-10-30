---
name: principles-scope
description: Deepen a task brief before execution. Use when asked to strengthen a prompt through professional methods, primary material, and outside validation while preserving its outcome and boundaries.
---

# Scope

In one line: Deepen the task through better material, methods, and evidence, then return a rewritten brief for review.

Start from the user's task. Preserve its outcome, audience, deliverable, budget, deadline, and authority. Return four answers and a self-contained rewritten prompt, then stop for review before executing it. Use `principles-method` for execution planning after the user accepts the brief.

## Steps

1. Restate the task and its binding constraints. If no task was supplied, ask for it. Ask about a missing constraint only when it could change the rewrite; otherwise label the assumption.
2. Answer these four questions for the task's field, with concrete choices:
   - What would a leading professional do here that the request leaves out? Name an action and the failure it would catch. Prefer changed practice over expert vocabulary.
   - What primary material would they start from? Trace summaries toward original records, observations, source files, or measurements. Choose the least processed material that could change the answer. State what is available and what would require access.
   - Which specific methods and tools would they use? Name the method, its input, and why it fits. Name a tool when it helps implement the method. Separate verified capabilities from proposals; offer a direct alternative when an optional tool is absent.
   - What evidence beyond the user or model's confidence would show the result is right? Name the claim, a check that could fail, and the observable success condition. Use `principles-verify` to choose evidence and `principles-measure` for quantities. For experiential work, use named criteria and observation by its intended audience; state what remains judgment.
3. Select the changes that improve this task within its constraints. A more elaborate method earns its cost only when it could change the result. If a necessary input or check is unavailable, expose that dependency and the claim it limits. Keep any proposed change to outcome, budget, deadline, access, or deliverables separate for the owner's decision.
4. Rewrite the prompt so it stands alone. Include the original outcome and constraints, selected professional actions, source material, methods, required access, deliverable, and evidence of success. Carry forward uncertainties and stop conditions. Use concrete instructions instead of a request to act like an expert.
5. Compare the rewrite with the original. Remove added goals and deliverables that serve no stated requirement. Confirm that every selected improvement appears in the prompt, and that unavailable inputs are conditions rather than assumed possessions.
6. Present the four answers, followed by the rewritten prompt. End at the review boundary. Approval of the brief is a separate decision from permission for any later consequential action.

## Principles

These are heuristics for finding a stronger brief. More raw data, more tools, and more demanding targets do not by themselves improve work.

| Principle | Failure | Check |
|---|---|---|
| Preserve the destination | A request for depth becomes a larger project | Does the rewrite retain the same outcome and deliverable within the owner's constraints? |
| Change practice | Expert language hides an unchanged approach | Which action, input, or test differs from the original request? |
| Trace material to its source | A polished summary hides an assumption or missing observation | Can the important claim be checked against its originating evidence, and is access known? |
| Make methods earn their cost | Sophisticated tools consume the budget without changing the answer | What decision could this method change, and is a simpler method sufficient? |
| Let evidence disagree | The maker's confidence certifies its own result | Could the proposed check reject a plausible but wrong result? |
| Keep review before execution | A rewritten prompt silently authorizes new work | Has the agent returned the brief and stopped before performing it? |

## Completion

The user has four concrete answers and a prompt they can review and run separately. Dependencies, assumptions, and limits of validation are visible. The underlying task remains unexecuted.

Pairs with: before `principles-method`, `principles-design`; after `principles-research`, `principles-craft`, `principles-verify`.
