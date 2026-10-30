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
- Creation: `principles-design`, `principles-synthesize`, `principles-integrate`, `principles-ecosystem`, `principles-world`, `principles-distribute`.
- Decisions: `principles-scope`, `principles-ground`, `principles-research`, `principles-method`, `principles-represent`, `principles-invert`, `principles-horizons`.
- Evaluation: `principles-measure`, `principles-verify`, `principles-craft`, `principles-secure`, `principles-reliability`.
- Learning: `principles-lessons`, `principles-refine`, `principles-improve`, `principles-simplify`, `principles-loop`, `principles-compound`.
- People and agents: `principles-counsel`, `principles-mind`.
- Skills and closeout: `principles-create`, `principles-tidy`.

Each skill names a principle, the failure it prevents, and a check. Simplification keeps useful distinctions, safety margins, accessibility, and intentional richness.

Use `principles-scope` to deepen a task into a reviewable prompt through professional methods, primary material, and outside evidence. It stops before execution.

Use `principles-design` to choose an approach, `principles-refine` to revise an existing result toward its quality bar, and `principles-improve` for measured gains in a working thing.

Use `principles-measure` for measurements in software and physical work. It defines the quantity, method, references, uncertainty, and comparison; `principles-ground` handles what to infer from the evidence.

Use `principles-research` to frame a source search, trace claims to evidence, and synthesize a cited answer with explicit gaps. It covers gathering and reporting evidence; `principles-ground` owns inference and the decision to learn more.

Use `principles-create` to add a family skill with the repository's conventions and an overlap check. Use `principles-tidy` for task cleanup, dependency and architecture docs, and tool discovery. Tidy works without a cleanup tool, reports tools used, and leaves entry pointers for fresh agents.

## Install

Ask your coding agent, in any harness, on Windows, macOS, or Linux:

```
Install the principles skills and engineering policy from https://github.com/benpham3206/principles by following the Install section of its README.
```

In Claude Code you can install the plugin instead:

```
/plugin marketplace add benpham3206/principles
/plugin install principles@principles
```

The plugin installs skills only, without the engineering policy. It namespaces each skill, so commands read `/principles:principles-verify`. Either way, agents load a skill on their own when a task matches.

To install by hand, or for the policy and every harness on the machine, you need Python 3.9 or later and git (use `python` on Windows):

```
git clone https://github.com/benpham3206/principles
cd principles
python3 install.py --pull
```

This clones the installed copy to `~/.agents/skill-repos/benpham3206__principles` and links each skill into `~/.agents/skills`. It then links them into every coding agent's skills folder, such as `~/.claude/skills`, `~/.codex/skills`, and `~/.cursor/skills`, when that harness's own folder exists. It creates a missing skills folder or instruction file for such a harness. It needs no admin rights; on Windows the links are junctions. Run the same command again to update. `python3 install.py --check` is a dry run that exits 1 when anything would change.

The installer works from that installed clone, never from a working checkout, so unmerged edits stay out of active skills. The list of agents it knows lives in `harnesses.py`. When [agent-hooks](https://github.com/benpham3206/agent-hooks) is installed, its `fanout.py` is used instead, which adds its skill scan. `python3 install.py --all` also updates configured machines with the generic ssh aliases `mac` and `windows`, when they exist; `--check --all` is the dry run.

For a harness the installer does not know, link or copy each folder in `skills/` into its skills directory. Each folder contains a `SKILL.md` with a name and description.

On every machine, a pull fast-forwards to exactly `origin/main`. It refuses a clone with local edits, untracked files, or local commits. A link that points elsewhere is reported and left in place.

The installer also writes `policy.md`, the engineering policy, as one managed block into each harness's instruction file. Run `python3 -m unittest` to verify the repository.

Install tests use temporary homes, including one that runs the real installer in a blank home with no agent-hooks. When agent-hooks is installed, the policy scenarios also run against its `fanout.py`. `harnesses.py` records its upstream commit, source hash, and local policy naming and migration changes. The always-on policy has a 50-line and 550-word budget; detailed execution procedures live in `principles-method`.

## Uninstall

The plugin uninstalls with `/plugin uninstall principles@principles`. For an `install.py` installation, ask your agent to follow these steps, or follow them yourself. `~` means your home folder (`$HOME` in PowerShell). Keep the clone until you finish removing its links and policy blocks.

1. Remove only skill links that lead to `~/.agents/skill-repos/benpham3206__principles`: first those in each harness's skills folder, then those in `~/.agents/skills`. See `SKILL_DIRS` in [harnesses.py](harnesses.py) for harness paths. On macOS, inspect each link with `ls -l "<link>"`, then use `unlink "<link>"`. On Windows, inspect its target with `Get-Item -LiteralPath '<link>' | Select-Object FullName, LinkType, Target`, then use `cmd /c rmdir "<link>"`. Replace `<link>` with the full link path. Windows links are junctions; removing one this way does not delete its target. Keep real folders and links to other clones.
2. In each instruction file, delete only the managed policy block, including both marker lines below. Keep all other text. Older installations can use different marker prefixes and filenames; match the engineering policy block by its managed source, not its prefix. See `instruction_targets` in [harnesses.py](harnesses.py) and `policy` in [install.py](install.py) for paths, including the Hermes policy reference and pointer. Delete `~/.grok/rules/managed-engineering-policy.md` and `~/.cursor/rules/managed-engineering-policy.mdc` only if they contain nothing you added; otherwise remove just the block. Removing a block from a newly created instruction file leaves it empty, which is harmless.

   ```
   <!-- BEGIN managed-engineering-policy (managed by propagate-across-harnesses; edit ~/.agents/skill-repos/benpham3206__principles/policy.md, then rerun) -->
   <!-- END managed-engineering-policy -->
   ```

3. Move `~/.agents/skill-repos/benpham3206__principles` to Trash on macOS or the Recycle Bin on Windows. Keep any local work you still need.

## Contributing

Rules live in [AGENTS.md](AGENTS.md). Every skill is built with its own `principles-method` and checked with its own `principles-verify`.

## License

MIT. See [LICENSE](LICENSE).
