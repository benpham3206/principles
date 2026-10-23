# principles

Axioms, principles, and taste for agents and the people who work with them. Any medium, software or physical. Written to stay true as models grow more capable.

Think big. Build small. Win.

## The loop

```
INTENT -> GROUND -> MAKE -> SIMULATE -> REALITY
  ^                                      |
  +----------- LESSONS <- VERIFY <--------+
```

State the purpose, find what is true, make the thing, and check it against reality. Use what happened to choose the next action. Scale the work to its consequences with `principles-method`.

Start with `principles`, the [skill map](skills/principles/SKILL.md). It defines six axes once: form, material, energy, observer, composition, and time. Each medium skill applies them; `principles-verify` checks the result. Load only what the task needs.

## Skills

- Medium: `principles-visual`, `principles-sound`, `principles-touch`, `principles-language`, `principles-interaction`, `principles-information`, `principles-code`, `principles-machine`.
- Creation: `principles-synthesize`, `principles-integrate`, `principles-world`, `principles-distribute`.
- Decisions: `principles-ground`, `principles-method`, `principles-represent`, `principles-invert`, `principles-horizons`, `principles-qualities`.
- Evaluation: `principles-verify`, `principles-craft`, `principles-secure`, `principles-reliability`.
- Learning: `principles-lessons`, `principles-improve`, `principles-simplify`, `principles-loop`, `principles-compound`.
- People and agents: `principles-counsel`, `principles-develop`, `principles-mind`.

Each skill names a principle, the failure it prevents, and a check. Simplification keeps useful distinctions, safety margins, accessibility, and intentional richness.

## Install

Claude Code:

```
/plugin marketplace add benpham3206/principles
/plugin install principles@principles
```

The plugin namespaces each skill, so commands read `/principles:principles-verify`. For the shorter `/principles-verify`, `/principles-visual`, and so on, install with `install.py` below instead. Either way, agents load a skill on their own when a task matches.

Any harness that reads Agent Skills folders (`SKILL.md` with `name` and `description`): clone the repo and link or copy each folder in `skills/` into that harness's skills directory.

```
git clone https://github.com/benpham3206/principles
```

With agent-hooks present (its `fanout.py` links one folder into every harness), `install.py` does all of it:

```
python3 install.py --pull     # clone or fast-forward ~/.agents/skill-repos/benpham3206__principles, then link and fan out
python3 install.py --check    # dry run; exit 1 on drift
python3 install.py --all      # this machine, then every other one with an ssh alias (mac, mbp13, windows; aliases name the other machines, see agent-hooks' "Machines and Tailscale")
python3 install.py --check --all   # dry run here and on every other machine; pulls and writes nothing
```

It installs from that clone, never from a working checkout, so unmerged edits never reach an agent. Pulls fast-forward to exactly `origin/main` and refuse a clone with local edits, untracked files or local commits, here and on every other machine, and a link that points elsewhere is reported, never replaced. It also writes `policy.md`, the always-on engineering policy, as one managed block into every harness's instruction file. Verify: `python3 -m unittest`.

## Contributing

Rules live in [AGENTS.md](AGENTS.md). Every skill is built with its own `principles-method` and checked with its own `principles-verify`.

## License

MIT. See [LICENSE](LICENSE).
