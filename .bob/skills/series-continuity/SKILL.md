---
name: series-continuity
description: Maintain series/season/episode canon and identify cross-episode stale
  dependencies after upstream changes.
---

# Series Continuity

## When to use
Maintain series/season/episode canon and identify cross-episode stale dependencies after upstream changes.

## Procedure
1. Load locked SeriesBible, season arc, all released/locked episode outlines, CharacterState/RelationshipState, world rules, recurring assets and prior episode knowledge ledger.
2. Model season and episode time explicitly; track what each character/audience knows before and after every episode/scene.
3. Track long-range setup/payoff, relationship progression, injuries, wardrobe/prop/location state, availability and asset reuse across episode boundaries.
4. Validate A/B/C story progression against season engine and serialization/reset policy; flag episodes that consume a setup without payoff capacity or reset irreversible change without reason.
5. When SeriesBible or season canon changes, compute affected episodes/assets and mark only descendants stale; preserve unrelated locked work.
6. Prepare recap/reintroduction requirements from actual audience knowledge gaps rather than repeating exposition automatically.
7. Run season-wide regression before episode lock and escalate canon conflicts to showrunner rather than inventing a local exception.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
