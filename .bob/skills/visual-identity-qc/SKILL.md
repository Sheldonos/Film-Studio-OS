---
name: visual-identity-qc
description: Independently review visual quality, character identity, anatomy, lighting,
  background stability and prompt/spec adherence.
---

# Visual Identity Qc

## When to use
Independently review visual quality, character identity, anatomy, lighting, background stability and prompt/spec adherence.

## Procedure
1. Load canonical identity references/model sheet, current CharacterState and ShotSpec; never compare against a random earlier take.
2. Check face structure/landmarks, hair, body proportions, age, distinctive features, wardrobe state, injuries/makeup and permitted expression variation.
3. Separate identity drift from intentional performance/lighting/perspective change; use multiple canonical views where available.
4. For multi-character shots, verify each identity independently and detect blending/swapping.
5. Emit confidence and blocker severity; low-confidence automated review routes to independent human/character director rather than auto-pass.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
