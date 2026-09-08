---
name: model-routing
description: Route a production task to a compatible provider/model using capability
  evidence, policy, privacy, quality, latency and cost constraints.
---

# Model Routing

## When to use
Route a production task to a compatible provider/model using capability evidence, policy, privacy, quality, latency and cost constraints.

## Procedure
1. Load ShotSpec requirements, canonical prompt/reference needs, current dated provider capability manifests, project policy, rights/privacy constraints, budget/latency target and benchmark evidence.
2. Filter hard incompatibilities first: unsupported modality/input/duration/control, region/privacy/training/license restriction, unavailable provider, missing authorization or budget ceiling.
3. Score remaining candidates on measured task-specific quality dimensions—not one global average—plus reliability, expected attempts, latency and normalized expected cost per accepted second/artifact.
4. Record confidence and evidence date. Unknown policy fields block policy-sensitive jobs rather than receiving a neutral score.
5. Choose primary and fallback adapter/model strategies; fallback must preserve critical controls/rights rather than merely be cheaper.
6. Re-route only on classified failure or changed availability/policy; avoid provider thrashing between attempts.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
