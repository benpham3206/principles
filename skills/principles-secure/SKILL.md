---
name: principles-secure
description: Protect against misuse and compromised parts. Use when handling outside input, secrets, data, permissions, agent authority, or changes to a control.
---

# Secure

A thing is **secure** when its actions stay within rightful authority and its remaining risks stay within limits accepted by affected people or their legitimate representatives. Check hostile inputs, compromised parts, and mistakes. Affected people include users, bystanders, and people described by the data. Security depends on boundaries and what crosses them.

```
ASSETS ----> ADVERSARIES ----> BOUNDARIES ----> AUTHORITY ----> CONTROLS ----> FAILURE ----> REVIEW
what is      who wants it,     where trust      who may do     what enforces   what happens  what the
worth        what they can     changes          what, and      each rule,      when a        change
protecting   reach and spend                    who said so    outside the     control       touched,
                                                               actor           cannot tell   traced end to end
```

## Laws

- **Information is not authority.** A request, a document, or a model's output can ask for an action. Only a grant from someone who holds the authority can allow it.
- Every part can fail or be turned. Design so one compromised part reaches as little as possible.
- Trust lives at boundaries. Check at the boundary where trust changes, not only where it is convenient.
- When a control cannot decide, it fails to the state that limits harm. For access to an asset that is usually closed; for a safety path, such as a fire exit or an emergency stop, it is open or stopped. An open default chosen by accident is a hole with a delay.
- The defender must cover every path; the attacker needs one. Shrink the paths before hardening them.
- A control the actor can change is advice, not a control.
- Security that people route around is no security. The safe way must also be the easy way.

## Defaults to replace

Trust because the caller is internal, a permission granted broadly "for now", one credential shared by many parts, secrets in code, config, logs, or examples, a denylist of bad inputs, checks only in the client or the prompt, errors that fail open, an agent that can edit the rules that bind it, a model's output passed straight to a shell, query, path, or tool, recovery keys within reach of everyday work, a review of the changed lines only, and severity set by alarm instead of reach.

## Steps

1. Name the assets and the people at risk: data, money, access, privacy, physical safety, reputation, and the control system itself. Rank them by the harm of their loss, counting harm to people who are not the owner.
2. Name the adversaries and the accidents: who would want each asset, what they can reach, what they can spend, and which honest mistakes do the same damage. Include the paths that need no code: physical access and tampering, a persuaded or coerced insider, a lost device, an impersonated person.
3. Draw the trust boundaries: every place where data, commands, or control pass between parties that trust each other differently. Inputs from people, networks, files, other services, and models all cross one.
4. Write the authority: for each actor, the actions it may take, who granted them, and how long the grant lasts. Anything not written is denied.
5. Place a control at each boundary that the actor on the far side cannot change: validation against an allowlist, a permission check, a sandbox, a rate limit, a required approval.
6. Decide each failure: when identity, permission, or validation cannot be established, the control denies access and says why. Where denial itself causes harm, as with a safety path, write the safe fallback instead. Log the decision where an operator will see it.
7. Limit the blast radius: separate credentials per part, narrow scopes, short lifetimes, destructive and production power held apart from everyday workers, recovery kept out of reach.
8. Review every change that touches a boundary, an authority, or a control, as below. Re-run the model when the thing gains a new input, actor, asset, or power.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Least privilege | A part holds power its job does not need, so its compromise costs more than its job | For each permission, which authorized task needs it, on which path? Remove the ones with no answer |
| Separate request from grant | An instruction found in an email, page, file, or tool result is obeyed as if the owner gave it | For each action, can you name who authorized it, outside the content that asked? |
| Enforce outside the actor | A rule written only in the prompt, the client, or the docs of the thing it binds | Remove the actor's cooperation. Does the rule still hold? |
| No self-granted authority | An agent or process edits the policy, key, or config that limits it | Can any actor widen its own grant without the authority that granted it? |
| Validate at the boundary, by allowlist | A filter of known bad inputs that the next input walks around | Is each input checked against what is allowed, at the point it crosses? |
| Untrusted until checked | Model, tool, and third-party output treated as safe because it came from your own system | Trace each output to the place it is acted on. Is it checked there? |
| Fail to the safe state | A timeout, parse error, or missing policy that grants access, or a safety path that locks shut when power fails | Break the check: kill its dependency, cut its power, feed it garbage. Does it land in the state the threat model chose? |
| Contain the compromise | One stolen credential opens everything | Assume each part is taken over in turn. What else can it reach? |
| Keep secrets out of the work | A key in a commit, log, example, URL, or test fixture | Search history, logs, and fixtures for secrets. Do production keys appear outside their store? |
| Defense in depth | One control between the attacker and the asset | For each asset, how many independent controls must fail before it is lost? |
| Verify the person, not the claim | An attacker who calls, writes, or walks in sounding like someone with authority is obeyed | Is each request for a sensitive action confirmed through a channel the requester does not control? |
| Make the safe path the easy path | People disable a control because it costs them every day | Watch someone do the task. Do they keep the control on? |
| Record the decisions | A breach or misuse that leaves no trace of who did what | From the log alone, can you tell who acted, on what authority, with what result? |
| Plan the way back | Recovery that depends on the thing that was compromised | Can you revoke, rotate, and restore without the broken part? |

## Reviewing a change for security

- Review what changed, and trace it to everything it reaches. A one-line change can move a boundary, widen a permission, or ungate a feature far from the diff.
- Look first for changes to boundaries, authority, and controls: who may call it, what it trusts, what it can reach, what happens when a check fails.
- Check gates. A feature meant for some users, a flag, or an internal-only path must stay closed to everyone else on every route.
- Check what breaks for the honest user, too: renamed secrets, moved config, changed ports, new manual steps.
- Separate intended from unaware. A change meant to remove a safeguard, with a tight scope, needs no alarm about intent; still weigh what it exposes against the threat model and the authority for the change. A change whose author may not see the full reach does, and so does one that looks hostile.
- Report a confirmed, urgent exposure at once with its known reach. Otherwise finish the trace before reporting. A finding that says "unless the other side handles it" is unfinished when the other side can be read.
- Rate severity by reach and likelihood, not by fear. A reviewer who calls everything critical is soon ignored.
- Form your own view before reading other reviews, then compare. Fresh eyes find what anchored eyes miss.

## Where to look

- Every place outside text becomes an action: a shell command, query, file path, URL, template, deserializer, or tool call.
- Every credential: where it lives, who can read it, how long it lasts, how it is rotated.
- Every default: what a new user, a new part, or a missing config gets.
- Every error path: what a failed check returns, logs, and leaves open.
- Every actor that can change its own controls, including the people and agents who run the system.
- Every new input, integration, or power since the threat model was last written.

Pairs with: before `principles-verify`, `principles-code`, `principles-reliability`; after `principles-horizons`, `principles-mind`.
