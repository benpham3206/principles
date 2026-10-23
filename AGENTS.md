# AGENTS.md

Rules for working on this repo, for every agent and every person. [CLAUDE.md](CLAUDE.md) points here.

## What this is

`principles` is a skills plugin: axioms, principles, and philosophies that make agents and people better at making things, in any medium, software or physical. It is meant to stay true as models grow more capable. Write what will still hold in a hundred years.

`policy.md` is the always-on engineering policy. `install.py` writes it into every harness's instruction file, so every agent reads it in every session. Keep it to 50 lines: it says when to load which skill, and the skills hold the depth.

The bar:

- **Timeless over dated.** Physics, perception, logic, and judgment stay. Tools, products, versions, and prices do not belong here.
- **Principle, failure, check.** Every principle names the failure it prevents and a check that catches it.
- **Positive form.** Say what to do. A prohibition earns its place only when no positive form exists.
- **Honest status.** Write each claim as the kind it is, using the kinds of claim in `principles-ground`: law within stated assumptions, empirical regularity, heuristic, hypothesis, convention, or value. A heuristic states its limit. A hypothesis says how to test it. Mark the kind only where it changes how a reader should use the claim.
- **One fact, one place.** The six axes live in `skills/principles`. Other skills use them and never redefine them.

## Files

```
skills/<name>/SKILL.md     the skills; skills/principles is the map and owns the six axes
policy.md                  always-on policy, written into every harness's instruction file
install.py                 links skills and writes policy.md on every machine
test_skills.py             mechanical checks of the rules in this file
test_install.py            install.py against a temp home
README.md                  human entry point; lists every skill
evals/judgment/            preliminary A/B eval of the guidance: tasks, harness, results, raw data
.claude-plugin/            Claude Code plugin and marketplace manifests
.github/workflows/         CI runs the verify command on every push to main and every PR
```

## Hazards

- **Installed clone is live.** Agents load skills through links into `~/.agents/skill-repos/benpham3206__principles`. An edit there reaches every agent at once, unreviewed. Work in a separate clone or a worktree.
- **policy.md reaches every session on every machine.** A wrong line there misleads every agent until the next install. Treat a policy change as the highest-consequence change in the repo.
- **install.py writes outside the repo.** It edits harness instruction files and links folders on this machine and, with `--all`, on others. Test it against a temp home, as `test_install.py` does; run `--check` before a real run.
- **Policy tests need agent-hooks.** `TestPolicy` skips when agent-hooks `fanout.py` is absent, as it is in CI. Run the suite on a machine with agent-hooks before merging an `install.py` change.

## Dogfood

This repo is built by its own skills. Before adding or changing a skill or `policy.md`:

1. Run `principles-method`: intent, definition of done, the gate.
2. Write it.
3. Run `principles-verify` on it: three distances, six axes, taste faults, verification.
4. Before the pull request opens, get an independent review from a different model or person, and fix each material issue it finds. The author reviewing in another session is not independent.
5. A change is done when `principles-verify` and the independent review find no remaining material issue, and the skill reads as plain instructions to a capable stranger.

## Skill layout

```
skills/<name>/SKILL.md      one skill, frontmatter name equals folder name
```

Frontmatter: `name` and `description`. The description front-loads what the skill is and lists only distinct triggers, under 45 words.

Put what an agent most needs first. Some harnesses read only the first 60 to 120 lines of a skill, so laws, defaults, steps, and failures go above lookup tables.

### Medium skills

Every medium skill (`principles-visual`, `principles-sound`, `principles-touch`, `principles-language`, `principles-interaction`, `principles-information`, `principles-code`, `principles-machine`) follows the same shape, with `principles-visual` as the reference:

```
# <Medium>
<What a work in this medium is, and what the observer does first, in one or two sentences.>
## Laws of the medium     5 to 7 principles that hold across the axes
## Defaults to replace    the unchosen values that mark generic work
## Tree            ASCII tree: the six axes, then any branch only this medium needs
## <Axis>          one section per axis: table of Leaf | Principle | Failure | Check
```

## Writing rules

- Plain words, short sentences, active voice, one idea per sentence.
- Sentence-case headings. `-` for bullets. No em or en dashes. No curly quotes. No emoji.
- No filler. Delete any sentence that restates the heading or the sentence before it.
- Concrete words over these: crucial, delve, robust, comprehensive, seamless, leverage (as a verb), utilize, ensure, landscape.
- Name a mechanism or a number, never a feeling.
- Bold only defined terms.
- No notes about process. The reader sees only the principle.

## Verify

`python3 -m unittest` runs the install tests and the skill checks. Run it before every commit; a change is not done until it passes. CI runs it on every pull request.

`test_skills.py` enforces frontmatter, name equals folder, description length, references that resolve, ASCII outside code fences, one `Pairs with:` line per skill, the medium skill shape, the stock vocabulary ban, the six axes in one place, every skill listed in the README and the map, and the policy line limit. The other rules here need a reader. When a rule can be checked mechanically, add the check before adding more rules.

## Git

Work on a branch and open a pull request. Never push to `main` without the owner's yes.
