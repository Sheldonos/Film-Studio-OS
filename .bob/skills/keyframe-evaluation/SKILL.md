---
name: keyframe-evaluation
description: Evaluate keyframes for composition, identity, world state, lighting,
  continuity and motion readiness before video generation.
---

# Keyframe Evaluation

## When to use
Evaluate keyframes for composition, identity, world state, lighting, continuity and motion readiness before video generation.

## Procedure
1. Compare generated keyframe to ShotSpec, bound character/world state, composition/camera/lighting intent and intended motion start/end requirements.
2. Evaluate identity, wardrobe/prop, location geography, pose/blocking, composition, lighting direction, depth, artifact severity and edit compatibility separately.
3. Treat required continuity/identity contradictions as blockers even if aesthetic score is high.
4. Estimate motion viability: whether pose, limbs, occlusion, contact and framing give the motion model a stable starting condition.
5. Classify fix path: accept, local image edit, alternate keyframe, recompose, change coverage or escalate shot design—not blind regeneration.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
