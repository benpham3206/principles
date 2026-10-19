# principles

Axioms, principles, and taste for agents and the people who work with them. Any medium, software or physical. Written to stay true as models grow more capable.

Think big. Build small. Win.

## The map

```
                         INTENT   why, for whom, under which limits
                            |
  GROUND --------------> MAKE ---------------> SIMULATE ------> REALITY
  what is true           six axes, any medium   test the model    ship, measure
  (cognitive)            (generative)                                |
       ^                                                             |
       +------------------ JUDGE  is it true, is it good  <----------+
                           (recognitive)

  SIX AXES OF ANY MADE THING
  Form | Material | Energy | Observer | Composition | Time

  MEDIUMS            WORK              VALUES        MIND
  visual             method            qualities     counsel
  sound              synthesize                      mind
  touch              horizons                        develop
  language           judge                           compound
  interaction
  information
  code
  machine
```

Every made thing is a set of choices along six axes. `principles` defines them once, each medium skill fills them in, and `judge` checks the result against reality.

## Skills

| Skill | What it gives |
|---|---|
| `principles` | The map, the six axes, and the laws that hold in every medium |
| `ground` | What is fundamentally true; map versus territory; first principles as a procedure |
| `visual`, `sound`, `touch`, `language`, `interaction`, `information`, `code`, `machine` | Each medium on the six axes: principle, failure, and check for every leaf |
| `judge` | Taste and verification; three distances; check before you generate |
| `method` | How to work: gate, plan, build, refine; decisions under uncertainty |
| `synthesize` | Invent from a Herculean goal: complete output, plan, verify |
| `horizons` | First to nth-order consequences |
| `qualities` | Intention, agency, trust, craft, delight and the rest; fluid versus textured |
| `counsel` | Advising a person, and keeping their agency across a capability gap |
| `mind` | Designing an agent: memory, cycles, budgets, calibration, invariants |
| `develop` | How people and agents grow; map, path, and advice modes |
| `compound` | What compounds, and how to invest so gains build on gains |

## Install

Claude Code:

```
/plugin marketplace add benpham3206/principles
/plugin install principles@principles
```

Skills then appear as `/principles:visual`, `/principles:judge`, and so on, and agents load them on their own when a task matches.

Any harness that reads Agent Skills folders (`SKILL.md` with `name` and `description`): clone the repo and link or copy each folder in `skills/` into that harness's skills directory.

```
git clone https://github.com/benpham3206/principles
```

With agent-hooks present (its `fanout.py` links one folder into every harness), `install.py` does all of it:

```
python3 install.py --pull     # clone or fast-forward ~/.agents/skill-repos/benpham3206__principles, then link and fan out
python3 install.py --check    # dry run; exit 1 on drift
python3 install.py --all      # this machine, then every other one with an ssh alias (mac, mbp13, windows)
```

It installs from that clone, never from a working checkout, so unmerged edits never reach an agent. Pulls are fast-forward only, and a link that points elsewhere is reported, never replaced. Tests: `python3 -m unittest test_install`.

## Contributing

Rules live in [AGENTS.md](AGENTS.md). Every skill is built with its own `method` and checked with its own `judge`.

## License

MIT. See [LICENSE](LICENSE).
