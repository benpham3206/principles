---
name: principles-code
description: Design and review software, interfaces, and data models. Use when writing, structuring, or refactoring code, APIs, schemas, services, or infrastructure.
---

# Code

**Code** is instructions and data that a machine runs and a person can change. Make the interface, data, and logic easy for the next person to follow.

## Laws of the medium

- Keep complexity only when it serves a requirement. Small additions accumulate maintenance cost.
- Data outlives code. Get the data model right; rewrite the code around it as needed.
- Make the right use easy and the wrong use hard: through types, interfaces, and safe defaults.
- Every boundary needs a contract: what comes in, what goes out, what can fail.
- Delete what is not needed. Code not written has no bugs and costs nothing to maintain.
- Measure, then change. Opinions about speed, correctness, and cause lose to a test or a profile.
- Design for change that is likely, and ignore change that is merely possible.

## Defaults to replace

A catch-all error handler that logs and continues, a boolean flag argument, nullable fields everywhere, a utilities module, a generic "manager" or "helper" class, retry with no limit or backoff, copied logic in two places, a dependency added for one function, tests that mirror the implementation line by line, secrets and magic numbers inline, time and randomness read from the environment, comments that restate the code.

## Tree

```
CODE
├── Form          interfaces, types, function shape, naming
├── Material      data structures, language and paradigm, dependencies, state
├── Energy        compute, memory, I/O, latency, power
├── Observer      caller, maintainer, operator, attacker, model reading it as context
├── Composition   modules, coupling and cohesion, data flow, layers, single source of truth, seams
├── Time          lifecycle, concurrency, versions and migrations, retries, failure and recovery, logs
└── Correctness   tests, error handling, invariants, security, observability
```

## Form

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Interface depth | A deep module has a small interface and much behind it; cost is the interface, benefit is the behavior | Shallow modules whose interface is as large as their body | Compare the lines needed to call it with the work it does |
| Types | Make invalid states unrepresentable; encode rules in the type, not in a comment | Flags and nulls that allow combinations the program never handles | List the type's values. Is each one legal? |
| Function shape | One function, one level of abstraction, inputs in and a result out | Functions that read, compute, write, and log in one body | Can you name it without "and"? |
| Signature honesty | The signature states every input, output, and failure | Hidden inputs (globals, clock, environment) and hidden failures | Can you call it from a test with nothing else set up? |
| Naming | A name states what a thing is or does at its level; one concept, one word | One idea under three names, or one name for two ideas | Read only the names. Does the program's story survive? |
| Surface area | Everything exported is a promise; export the minimum | Internals public because it was easier | Delete an export. Who breaks? |

## Material

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Data structures | Choose the data first; the code follows its shape | Clever code compensating for a wrong structure | Draw the data. Does each operation fall out in a line or two? |
| Language and paradigm | Pick the language whose strengths match the problem's hardest part | A familiar tool forced onto a poor fit | What is the hardest part, and what does the language give for it? |
| Dependencies | Each dependency is a liability you inherit: its bugs, its license, its release schedule, its attack surface | Pulling a library for ten lines of work | Could you write it in a day? What happens when it is abandoned? |
| State | Minimize state and localize it; derive what you can instead of storing it | The same fact held in two places that drift | For each stored value, what recomputes it? Who may write it? |
| Representation | Store the lossless form; compute the display form | Rounded, formatted, or truncated values stored as truth | Can the original be recovered from what is stored? |
| Configuration | Config is data with a schema and defaults that are safe | Settings read from scattered places with silent fallbacks | Does a bad value fail at startup, with a clear message? |

## Energy

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Complexity | Cost grows with input size by class: `O(n)` work doubles when n doubles, `O(n^2)` work quadruples | A nested loop that passes on ten rows and stalls on a million | State the cost as a function of n. Is n bounded? |
| Measure first | Profile before optimizing; the bottleneck is rarely where you guess | Tuning code that takes 1% of the time | Where does a profile say the time goes? |
| I/O and latency | Crossing a boundary (disk, network, process) costs orders of magnitude more than arithmetic | A call per item where one batch would do | Count the round trips per request |
| Memory | Peak memory is the limit, not the average; unbounded growth is a leak | Loading a whole input to process it one piece at a time | What is the memory at 10 times the largest input? |
| Power and cost | Idle work, polling, and over-provisioning spend energy and money for nothing | A loop that wakes every few milliseconds to check for nothing | What runs when no one is using it? |
| Budget | Set a latency or resource budget up front; a budget is a requirement | Performance judged by feel | Is there a number, and is it tested? |

## Observer

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Caller | The caller wants the result and a clear contract; spare them the internals | Callers forced to know call order or hidden preconditions | Can a caller use it correctly from the signature and one example? |
| Maintainer | Code is read far more than written; it must make sense cold | Cleverness that needs its author in the room | Hand it to someone with no context. Where do they stall? |
| Comments | Code says what; comments say why, and mark the quirk | Comments that restate the line, or none on the surprising line | Is each comment something the code cannot say? |
| Operator | The person at 3 a.m. needs to see state, find the cause, and act | Errors that say "failed" and nothing else | From the log alone, can you tell what, where, and which input? |
| Attacker | Every input from outside is hostile until validated | Trust given by default because the caller is internal | List the inputs. Who controls each? |
| Model as reader | A model reading code as context sees names, structure, and nearby text only | Naming and layout that need hidden knowledge | Does the file make sense with nothing else loaded? |

## Composition

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Modules and boundaries | Draw boundaries where change is independent; hide the decision likely to change | A change to one decision touching many files | Pick a likely change. How many modules does it touch? |
| Coupling and cohesion | Things that change together live together; things that do not, apart | Unrelated code in one file; one idea split across five | For each module, can you state its one reason to change? |
| Data flow | Data moves one way through layers; callbacks upward are a smell | Cycles in the dependency graph | Draw the dependency arrows. Any loops? |
| Layering | Each layer talks to the one below through its interface only | A top layer reaching into storage details | Can you replace the layer below without touching the one above? |
| Single source of truth | Every fact has one authoritative place; others derive from it | Two copies edited separately | Search for the fact. How many places define it? |
| Seams | Put a seam where behavior can be swapped without editing the code under test | Code that can only be tested by running the whole system | Can the clock, network, and store be replaced in a test? |
| Review thresholds | Use file length and branching thresholds to trigger a review | Metrics treated as goals, or never measured at all | Does a tool enforce the project's thresholds? A file above the threshold needs a stated reason to stay whole |
| Abstraction timing | As a rule of thumb, abstract on the third repeat, from real cases | A general framework built for a case that never came | How many real uses justify this abstraction? |

## Time

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Lifecycle | Every resource has an owner who acquires and releases it | Handles, connections, and tasks that outlive their need | For each resource, who closes it, and on every path? |
| Concurrency and ordering | Shared mutable state under concurrent access needs one rule; prefer sharing nothing | Races that appear only under load | What can run at the same time, and what orders it? |
| Versioning and migration | Change an interface in steps: add the new, migrate callers, then delete the old | Breaking change shipped in one step | Can old and new callers run side by side during the move? |
| Idempotency and retries | An operation that may be repeated must give the same result; retries back off and stop | Duplicate charges, duplicate rows, retry storms | Run it twice. Is the outcome the same as once? |
| Failure and recovery | Assume each dependency fails; define the degraded behavior and the way back | A single failure that takes down everything | Kill each dependency in turn. What does the user see? |
| Logs | A log line records what happened, with identifiers, at the moment it happened | Logs written for the author, or flooding at the cost of signal | Follow one request across the logs. Is it traceable? |
| A year later | Code outlives its context; record the reason, the date of a workaround, and the exit condition | Temporary fixes that become the system | Does each workaround say why it exists and when to remove it? |

## Correctness (code-only branch)

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Change reach | Before editing, list every place the change must reach: callers, tests, fixtures, config, exports. Be minimal in the solution, complete in the change | A small diff that leaves callers, fixtures, or docs broken | Search every use of what you touched. Is each one updated or still correct? |
| Fix once, at the source | A bug in shared code is fixed in the shared code, after finding every caller, not patched at each symptom | The same guard added in three callers while the cause stays | Does the fix live where the wrong value is made? |
| Tests | Test behavior through the interface, not the implementation; a test must fail when the behavior breaks | Tests that pin internals and break on every refactor | Change the internals, keep the behavior. Do tests still pass? Break the behavior. Do they fail? |
| Error handling | Handle an error at the boundary that can act on it; below that, pass it up with context | Swallowed errors, or the same error handled at every layer | For each handler, can it fix, retry, or report? |
| Invariants | State what must always hold and assert it where it could break | Silent corruption found far from its cause | Name the invariants. Where is each checked? |
| Security by default | Least privilege; validate input at every trust boundary; fail closed | Broad permissions and checks added after the leak | Strip each privilege. What breaks? Which input is unchecked? |
| Observability | The running system answers questions you did not plan to ask: logs, metrics, traces | Debugging by redeploying with more prints | Can you explain a failure in production without changing the code? |

Pairs with: before `principles-method`, `principles-represent`; after `principles-integrate`, `principles-secure`, `principles-verify`.
