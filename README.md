# principles

Axioms, principles, and taste for agents and the people who work with them. Any medium, software or physical. Written to stay true as models grow more capable.

Think big. Build small. Win.

## The map

```
    INTENT    why, for whom, under which limits
       |      shape it with represent, weigh values with qualities
       v
+-> GROUND ------> MAKE --------------------> SIMULATE -----> REALITY
|   what is true   six axes, one medium       test the model  ship, measure
|   ground         visual  sound  touch       horizons           |
|                  language  interaction                         |
|                  information  code  machine                    |
|                  integrate, to join the parts                  |
|                  world, to make the parts one place            |
|                  synthesize, for the new                       |
|                                                               v
+----------- LESSONS <----------------------- VERIFY <-----------+
             what changes next                is it true, is it good
             lessons  improve                 verify  craft  secure

  method runs the loop, with rigor scaled to consequence.
  Beside the loop, for people and agents: counsel, mind, develop, compound.

  SIX AXES OF ANY MADE THING
  Form | Material | Energy | Observer | Composition | Time
```

Every made thing is a set of choices along six axes. `principles` defines them once, each medium skill fills them in, and `principles-verify` checks the result against reality.

## Skills

| Skill | What it gives |
|---|---|
| `principles` | The map, the six axes, and the laws that hold in every medium |
| `principles-ground` | What is fundamentally true; map versus territory; first principles as a procedure |
| `principles-visual`, `principles-sound`, `principles-touch`, `principles-language`, `principles-interaction`, `principles-information`, `principles-code`, `principles-machine` | Each medium on the six axes: principle, failure, and check for every leaf |
| `principles-world` | Many parts as one place: canon, persistence across thresholds, agreeing senses, in-world interface, voice |
| `principles-craft` | Good, great, timeless: what defines each and how to check; taste, pride, and the faults of generic work |
| `principles-verify` | Done means true, works, and good: evidence on the real thing, taste at three distances, a bar you would sign |
| `principles-secure` | Safe from misuse and from its own compromised parts: threat model, trust boundaries, authority, fail closed, review |
| `principles-method` | How to work: gate, plan, build, refine; decisions under uncertainty |
| `principles-represent` | Put a problem into the structure that shows the next action: flows, trees, state machines, graphs, matrices |
| `principles-lessons` | Learn from what happened: facts, causes, the class, a check that fails without the fix, then move on |
| `principles-integrate` | Join parts into one working whole: interfaces first, thin slice, one part at a time, every surface |
| `principles-improve` | Make a working thing better in order: measure, bottleneck, delete, simplify, speed up, automate |
| `principles-synthesize` | Invent from a Herculean goal: complete output, plan, verify |
| `principles-horizons` | First to nth-order consequences |
| `principles-qualities` | Intention, agency, trust, craft, delight and the rest; fluid versus textured |
| `principles-counsel` | Advising a person, and keeping their agency across a capability gap |
| `principles-mind` | Designing an agent: memory, cycles, budgets, calibration, invariants |
| `principles-develop` | How people and agents grow; map, path, and advice modes |
| `principles-compound` | What compounds, and how to invest so gains build on gains |

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
```

It installs from that clone, never from a working checkout, so unmerged edits never reach an agent. Pulls are fast-forward only, and a link that points elsewhere is reported, never replaced. It also writes `policy.md`, the always-on engineering policy, as one managed block into every harness's instruction file. Verify: `python3 -m unittest`.

## Contributing

Rules live in [AGENTS.md](AGENTS.md). Every skill is built with its own `principles-method` and checked with its own `principles-verify`.

## License

MIT. See [LICENSE](LICENSE).
