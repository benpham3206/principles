# Routing eval

Checks whether an agent that reads only the routing text (the `Choose guidance` list in `policy.md` and the map in `skills/principles`) loads the right skill first. Run it after any change to either.

Give a fresh agent the routing text and the numbered situations, and ask for the one skill to load first for each, with no other files. Score the first choice against the expected skill. An entry with two expected skills accepts either. A fresh agent may still see the skills installed on its machine. An answer that names a skill absent from the routing text came from there: score it as a leak, not a routing miss, and rerun on an agent without it.

| # | Situation | Expected |
|---|---|---|
| 1 | You finished a code change and are about to tell the user it works. | verify |
| 2 | A watcher script failed overnight in real use; the logs are thin and you need to find out why. | lessons, ground |
| 3 | Halfway through a task, you are about to add a repository-wide rule that every module must expose the same three functions. | invert |
| 4 | Two explanations fit a bug: a race condition or a stale cache. | ground |
| 5 | A config file supplied by users is parsed and its values passed to a shell command. | secure |
| 6 | The team's build takes 25 minutes and they want it under 10. | improve |
| 7 | The code works, but every small change touches ten files. | simplify |
| 8 | Plan a three-week migration that several agents will work on in parallel. | method |
| 9 | A city is considering free buses; predict how riders, drivers, and car traffic respond over years. | horizons |
| 10 | Design what brings users back to an app each week without manipulating them. | loop |
| 11 | Write the announcement email for a product launch. | language |
| 12 | A payments service must keep running when one database node dies. | reliability |
| 13 | Choose among three approaches for syncing offline edits. | design |
| 14 | A scheduling problem has many constraints and you cannot see where to start. | represent |
| 15 | Pick which numbers go on an operations dashboard and how to chart them. | information |
| 16 | A junior engineer asks you to fix their bug; their manager wants them to learn to debug. | counsel |
| 17 | Merge three services built by different teams into one release. | integrate |
| 18 | Before trusting that a sensor reading means a device is connected, find out what normal readings look like. | measure |
| 19 | The task is done; temporary folders and a background process you started are still around. | tidy |
| 20 | A user asks whether to accept a job offer or stay where they are. | counsel |
| 21 | Decide what to learn and what to record so this year's work makes next year's easier. | compound |
| 22 | A draft works but feels off; compare it with the previous version and tighten it. | refine |
| 23 | Choose a launch channel and a price for a new tool. | distribute |
| 24 | Design the memory and goals of a coding assistant. | mind |
| 25 | Shipping speed and review thoroughness conflict, and the owner must choose which wins. | craft |
| 26 | You need published evidence on whether code review reduces defects. | research |
| 27 | Reach a goal no known approach reaches: a battery that charges in five minutes and lasts twenty years. | synthesize |
| 28 | After a fix, record what happened so the next agent does not repeat it. | lessons |
| 29 | Judge whether a finished landing page is merely fine or excellent. | craft |
| 30 | Make a game's menus, sounds, and story feel like one place. | world |
| 31 | Add a new skill to the principles family. | create |
| 32 | You are about to make code review mandatory for every change, including one-line typo fixes. | invert |
| 33 | Work backward from a launch date to what must be true each week before it. | invert, method |
| 34 | Before asking anyone else to use your new command-line tool, use it yourself for real work and fix what you hit. | loop |
| 35 | Map how people find a product, start using it, drift away, and come back. | loop |
| 36 | Each project starts from scratch; make each one leave something the next one builds on. | compound |
| 37 | Rewrite my task as a deeper professional brief using primary material, specific methods, and outside validation; stop before running it. | scope |
| 38 | Split a product into small pieces around a shared file format so outside developers can write their own adapters. | ecosystem |
| 39 | Add an adapter for a new payment supplier to your own checkout service and prove the release works. | integrate |
| 40 | Find which of four oven settings drive warping in printed parts, and whether any two interact, in as few runs as possible. | measure |
| 41 | A manager asks how to help a new hire grow into leading design reviews within a year. | counsel |
| 42 | Decide when a phone and watch app may interrupt someone with a notification, and how they tune each kind. | interaction |
| 43 | Ship a new version to a small share of users first, with a signal that halts the rollout if something breaks. | reliability |
| 44 | Use the crude first version of a build tool to build and check its own next version. | compound |
