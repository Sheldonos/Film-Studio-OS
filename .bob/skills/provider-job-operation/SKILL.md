---
name: provider-job-operation
description: Estimate, submit, poll, cancel and archive idempotent provider jobs through
  approved adapters; default to mock/dry-run.
---

# Provider Job Operation

## When to use
Estimate, submit, poll, cancel and archive idempotent provider jobs through approved adapters; default to mock/dry-run.

## Procedure
1. Resolve an approved RoutingDecision and adapter capability manifest; validate auth by secret reference, project scope, budget, side-effect authorization and idempotency key before submission.
2. Compile adapter payload from canonical request using allowlisted typed fields only; reject arbitrary provider flags not declared by the adapter contract.
3. Estimate cost before submit and block if estimate exceeds work-order/project approval threshold. Dry-run/mock remains default.
4. Submit idempotently; persist normalized ProviderJob before/after external state changes and never duplicate a job on retry with the same key.
5. Poll or consume webhook through normalized lifecycle states; enforce timeout/rate-limit policy and classify temporary, moderation, capability, auth, budget and permanent failures.
6. Cancel when supported; reconcile actual cost and downloaded artifact hashes; record provider/model/version/parameters, moderation and policy metadata.
7. Never promote provider output directly to final selection—hand it to QC/continuity/review first.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
