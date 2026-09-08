---
name: prompt-compilation
description: Compile canonical shot intent into a structured provider-neutral prompt
  packet with field-level provenance and negative constraints.
---

# Prompt Compilation

## When to use
Compile canonical shot intent into a structured provider-neutral prompt packet with field-level provenance and negative constraints.

## Procedure
1. Read validated ShotSpec and bound reference set as authority; never infer missing story/continuity facts from provider syntax.
2. Compile a structured model-neutral packet in layers: identity/state, location/state, action, performance, camera, lighting, composition/depth, atmosphere, continuity, audio/edit requirements and negative constraints.
3. Separate positive desired behavior from true constraints; avoid giant adjective lists and duplicate/conflicting instructions.
4. Preserve stable anchor wording for identity/world fields across related shots while allowing action/performance/camera deltas.
5. Attach provenance: exact ShotSpec version, reference versions, compiler version and unresolved/unsupported fields.
6. Only an adapter may translate the canonical packet into provider/model-specific parameters; compilation must remain deterministic for the same input versions.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
