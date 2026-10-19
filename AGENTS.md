# AGENTS.md

Rules for working on this repo, for every agent and every person. [CLAUDE.md](CLAUDE.md) points here.

## What this is

`principles` is a skills plugin: axioms, principles, and philosophies that make agents and people better at making things, in any medium, software or physical. It is meant to stay true as models grow more capable. Write what will still hold in a hundred years.

The bar:

- **Timeless over dated.** Physics, perception, logic, and judgment stay. Tools, products, versions, and prices do not belong here.
- **Principle, failure, check.** Every principle names the failure it prevents and a check that catches it.
- **Positive form.** Say what to do. A prohibition earns its place only when no positive form exists.
- **Honest status.** Separate established principle from heuristic from hypothesis. A heuristic states its limit. A hypothesis says how to test it.
- **One fact, one place.** The six axes live in `skills/principles`. Other skills use them and never redefine them.

## Dogfood

This repo is built by its own skills. Before adding or changing a skill:

1. Run `principles-method`: intent, definition of done, the gate.
2. Write it.
3. Run `principles-verify` on it: three distances, six axes, taste faults, verification.
4. A change is done when `principles-verify` finds no material issue and the skill reads as plain instructions to a capable stranger.

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

`python3 -m unittest` runs the install tests and the skill checks. Run it before every commit; a change is not done until it passes.

## Git

Work on a branch and open a pull request. Never push to `main` without the owner's yes.
