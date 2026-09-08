---
name: quality-gate-design
description: Define hard blockers, required metrics, independent reviewers, weighted
  preferences and waiver/escalation rules for a production gate.
---

# Quality Gate Design

## When to use
Define hard blockers, required metrics, independent reviewers, weighted preferences and waiver/escalation rules for a production gate.

## Procedure
1. Define the artifact decision the gate protects and split non-negotiable blockers from weighted quality preferences.
2. Specify required evidence/metrics, measurement method, owner, independent reviewer, threshold/anchor examples and acceptable uncertainty.
3. Use deterministic validators for measurable facts and model/human review only for genuinely perceptual/creative judgments.
4. Define waiver policy explicitly: which failures are never waivable by software, which require authorized human, and what rationale/evidence is stored.
5. Add positive, negative, missing-evidence and adversarial fixtures; include the case where high average scores coexist with one critical blocker.
6. Version the gate so historical projects keep the rule they were actually reviewed under.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
