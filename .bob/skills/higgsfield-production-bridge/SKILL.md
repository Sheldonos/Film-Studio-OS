---
name: higgsfield-production-bridge
description: Discover Higgsfield capabilities and prepare governed image, video or audio jobs through the official CLI boundary.
---

# Higgsfield Production Bridge

## When to use
Use when a production plans to generate or monitor Higgsfield image, video or audio work while preserving Film Studio OS rights, budget, approval and provenance controls.

## Procedure
1. Load the approved ShotSpec, PromptSpec, exact upstream versions, reference hierarchy, rights/consent records, project budget and requested modality; reject raw untraceable prompts.
2. Confirm the official CLI is installed and authenticated, then discover current job-set types and fetch the exact live model schema with `higgsfield model get <job-set-type> --json`.
3. Compile the provider-neutral 15-section prompt contract into the discovered flags without shell interpolation, unrecognized parameters or hidden defaults; retain the canonical request hash.
4. Build a dry-run command and run `higgsfield generate cost` with the same job-set type and parameters. Stop when cost cannot be normalized or exceeds the project cap.
5. For live work, require the external-authorization environment boundary plus an unexpired human approval bound to project, provider, operation, request hash and maximum cost. Never infer approval from conversational enthusiasm.
6. Submit through the adapter, persist external job ID and request hash, poll without duplicate submission, register returned artifacts with provenance, and send outputs to independent quality review.

## Required behavior
- Query live schemas because Higgsfield job-set types and parameters can change.
- Default to dry run; no live submission is exposed through the local MCP surface.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
