---
name: generation-failure-repair
description: Classify generation failure before retry and choose repair, regeneration,
  alternate coverage, compositing or human escalation.
---

# Generation Failure Repair

## When to use
Classify generation failure before retry and choose repair, regeneration, alternate coverage, compositing or human escalation.

## Procedure
1. Compare failed take to ShotSpec, keyframe/motion plan and QC findings; classify the earliest root failure rather than listing every visible symptom.
2. Choose failure class: identity/state drift, prompt/adherence, composition, anatomy/contact, temporal/physics, camera, environment, lip-sync/audio, provider error, edit incompatibility or upstream shot-design defect.
3. Select least-destructive recovery: parameter/prompt correction, local inpaint/repair, new keyframe, motion retry, alternate model, composite, alternate coverage, upstream reblock or human artist intervention.
4. Estimate cost/attempt/time and probability of success before another generation; enforce attempt budget and stop conditions.
5. Preserve failed attempt, exact payload, QC and rejection reason as learning data. Never overwrite it.
6. After repair, re-run the failing gate plus regression checks for identity/continuity/edit compatibility.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
