# principles

A library of skills for agents and the people who work with them. Use them to make decisions, create work, and check the result in any medium.

Think big. Build small. Win.

Agents: read [/principles-method](skills/principles-method/SKILL.md) first. Use [/principles-language](skills/principles-language/SKILL.md) whenever writing or editing public-facing text.

## The loop

```
Set the goal -> Check assumptions -> Make -> Predict -> Test
     ^                                                  |
     +--------------- Learn and revise <-----------------+
```

State what the work should do and who it serves. Check the assumptions that could change your approach. Make a small, complete version, predict how it will behave, and test that prediction against reality. Use the result to decide what to keep or change.

Use `principles`, the [skill map](skills/principles/SKILL.md), to choose what to load next. It defines six axes: form, material, energy, observer, composition, and time. Each medium skill applies them; `principles-verify` checks the result. Load only what the task needs.

## Skills

- Medium: `principles-visual`, `principles-sound`, `principles-touch`, `principles-language`, `principles-interaction`, `principles-information`, `principles-code`, `principles-machine`.
- Creation: `principles-design`, `principles-synthesize`, `principles-integrate`, `principles-world`, `principles-distribute`.
- Decisions: `principles-ground`, `principles-research`, `principles-method`, `principles-represent`, `principles-invert`, `principles-horizons`, `principles-qualities`.
- Evaluation: `principles-measure`, `principles-verify`, `principles-craft`, `principles-secure`, `principles-reliability`.
- Learning: `principles-lessons`, `principles-refine`, `principles-improve`, `principles-simplify`, `principles-loop`, `principles-compound`.
- People and agents: `principles-counsel`, `principles-develop`, `principles-mind`.
- Skills and closeout: `principles-create`, `principles-tidy`.

Each skill names a principle, the failure it prevents, and a check. Simplification keeps useful distinctions, safety margins, accessibility, and intentional richness.

Use `principles-design` to choose an approach, `principles-refine` to revise an existing result toward its quality bar, and `principles-improve` for measured gains in a working thing.

Use `principles-measure` for measurements in software and physical work. It defines the quantity, method, references, uncertainty, and comparison; `principles-ground` handles what to infer from the evidence.

Use `principles-research` to frame a source search, trace claims to evidence, and synthesize a cited answer with explicit gaps. It covers gathering and reporting evidence; `principles-ground` owns inference and the decision to learn more.

Use `principles-create` to add a family skill with the repository's conventions and an overlap check. Use `principles-tidy` for task cleanup, dependency and architecture docs, and tool discovery. Tidy works without a cleanup tool, reports tools used, and leaves entry pointers for fresh agents.

## Install

Claude Code:

```
/plugin marketplace add benpham3206/principles
/plugin install principles@principles
```

The plugin namespaces each skill, so commands read `/principles:principles-verify`. For the shorter `/principles-verify`, `/principles-visual`, and so on, install with `install.py` below instead. Either way, agents load a skill on their own when a task matches.

For a harness that reads Agent Skills folders, clone the repo and link or copy each folder in `skills/` into its skills directory. Each folder contains a `SKILL.md` with a name and description.

```
git clone https://github.com/benpham3206/principles
```

If agent-hooks is installed, `install.py` uses its `fanout.py` to link the skills into every harness:

```
python3 install.py --pull     # clone or fast-forward ~/.agents/skill-repos/benpham3206__principles, then link and fan out
python3 install.py --check    # dry run; exit 1 on drift
python3 install.py --all      # this machine, then every other one with an ssh alias (mac, mbp13, windows; aliases name the other machines, see agent-hooks' "Machines and Tailscale")
python3 install.py --check --all   # dry run here and on every other machine; pulls and writes nothing
```

The installer uses the clone at `~/.agents/skill-repos/benpham3206__principles`. It does not install from a working checkout, so unmerged edits stay out of active skills.

On every machine, a pull fast-forwards to exactly `origin/main`. It refuses a clone with local edits, untracked files, or local commits. A link that points elsewhere is reported and left in place.

The installer also writes `policy.md`, the engineering policy, as one managed block into each harness's instruction file. Run `python3 -m unittest` to verify the repository.

## Contributing

Rules live in [AGENTS.md](AGENTS.md). Every skill is built with its own `principles-method` and checked with its own `principles-verify`.

## License

MIT. See [LICENSE](LICENSE).
