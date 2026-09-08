---
name: reference-binding
description: Select and bind authorized character/world/style references to a shot
  while preserving provenance and usage constraints.
---

# Reference Binding

## When to use
Select and bind authorized character/world/style references to a shot while preserving provenance and usage constraints.

## Procedure
1. Read ShotSpec identity/world/style requirements and retrieve only project-authorized reference assets with immutable hashes and rights/consent compatibility.
2. Classify each reference purpose: identity, wardrobe, location, prop, composition, movement, lighting, material/style or continuity—not “inspiration” without role.
3. Score canonical relevance, view/pose/lighting compatibility and contradiction risk; prefer the smallest set that constrains the target without conflicting signals.
4. Bind reference IDs and versions to the generation plan. Never substitute a visually similar third-party asset without rights evidence.
5. Detect stale references after character/world updates and invalidate dependent generation plans before submit.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
