---
name: principles-ecosystem
description: Design pieces that outside makers adopt and extend through a shared contract. Use when opening a format, protocol, or plugin point to others, promising compatibility to them, or splitting a product into pieces people adopt or replace separately.
---

# Ecosystem

In one line: Put one small contract at the center, ship a core useful alone, and grow through adapters.

An **ecosystem** is a set of pieces, made by different makers, that work together through a shared contract. A **contract** is the format, protocol, or interface every piece reads or writes. An **adapter** connects the contract to something people already use. Use this skill to design how makers you do not coordinate build on a contract. Use `principles-integrate` to prove that any assembled whole works, whoever made its parts.

## Laws

- The contract outlasts every piece built on it. Keep it small, versioned, and readable with ordinary tools.
- The core earns adoption alone. Adapters and extensions state their purpose and dependencies, and can be replaced without touching the core.
- Own what grows scarce and rent what grows cheap. Build where a piece gains value as capability gets cheaper; adapt to the rest. This is a heuristic; check it with `principles-horizons`.
- Extend at the edges. New providers, channels, and tools plug in through adapters, so the core stays small and changes rarely.
- Draw the extension point from real adapters. For a new interface, a default is to write it after two or three first-party adapters exist. An established contract or existing independent implementations can supply that evidence instead.
- Compatibility is a promise to strangers. A break costs every maker downstream, so add, migrate, and then remove.
- People can leave with their work. A format they cannot read without you is a trap, not an ecosystem.

## Steps

1. Name the people and the one outcome the first piece delivers on its own. Use `principles-design` when the outcome is unclear.
2. Find the contract: the smallest shared record or message that the pieces must agree on. Write it as plain, versioned files or messages, with a validator and a known-bad example that must fail.
3. Split the work into pieces. Give each one job, one owner, the part of the contract it reads or writes, its dependencies, and a check that runs with them. Mark each piece own or rent.
4. Ship the core with a one-command install, a way to try it once without installing, and a page that shows it working. Use `principles-distribute` to reach the first people.
5. Add adapters for what people already use and pay for. Give every adapter one shared test kit, so "compatible" means "passes the kit".
6. Open the extension point once real adapters, or an established contract, show its shape. State the admission rules: declared source, pinned version, declared powers, and the test kit. Use `principles-secure` for the boundary.
7. Where several surfaces show the same work, make one of them the authority and the rest views of it, and state how freshness is checked. Otherwise, state at the contract who owns each record and how it is exchanged.
8. Measure by use: pieces adopted, adapters built by others, and the time a new maker needs to ship a working adapter. Use `principles-loop` for the return path and `principles-compound` for what each release carries forward.

## Principles

| Principle | Failure | Check |
|---|---|---|
| Contract first | Pieces agree by habit, then drift apart | Can a new piece be built from the contract and its validator alone? |
| A core worth using alone | A core that does nothing until five extensions join, or extensions that cannot be replaced | Does the core give a useful result by itself? Can each extension be removed or swapped without changing the core? |
| Small core | Every integration lands in the core, so each change breaks someone | Which parts of the core could move to an adapter? |
| One test kit | Each adapter is tested its own way, so "compatible" means nothing | Does one kit run against every adapter, including a known-bad one that must fail? |
| Bring what people have | People must replace a tool, model, or subscription to join | Does the piece work with what its user already pays for? |
| Stated ownership | Two surfaces or stores disagree about the same work, and nobody can say which is right | Where surfaces are views of one source, change it there: do the others update or mark themselves stale? Otherwise, does the contract state ownership, exchange, and conflict rules? |
| Proof at the door | The page describes the ecosystem instead of showing a piece at work | Does the first screen show a real piece doing its job, with one command to try it? |
| Versioned promises | A silent breaking change strands makers downstream | Is every contract versioned, with a migration path and a stated support window? |
| Declared trust | Extensions run with powers nobody listed | Does each extension declare its source, version, and powers, and run where its harm is bounded? |
| Exit | People stay because leaving loses their work | Can a person export everything and read it with ordinary tools? |

Pairs with: before `principles-integrate`, `principles-distribute`, `principles-secure`; after `principles-design`, `principles-horizons`.
