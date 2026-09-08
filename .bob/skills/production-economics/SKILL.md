---
name: production-economics
description: Track budget, schedule, attempts, latency, rework, stale-work cost, provider
  reliability and critical path for production decisions.
---

# Production Economics

## When to use
Track budget, schedule, attempts, latency, rework, stale-work cost, provider reliability and critical path for production decisions.

## Procedure
1. Load project/episode/sequence/shot budgets, schedule targets, approved thresholds, provider capability/cost manifests and historical acceptance/rework metrics.
2. Estimate expected cost from attempt probability and accepted-output rate, not list price alone; separate generation, human review/repair, storage and post costs.
3. Track planned versus actual cost/latency/attempts at work-order and aggregate scopes; attribute rework and stale-work cost to upstream changes/failure classes.
4. Identify critical path from workflow dependencies and current duration estimates; distinguish blocked time, provider queue time and active work.
5. Before a costly retry, compare expected value of regeneration, repair, alternate coverage/provider or human intervention.
6. Escalate budget/schedule variance at configured thresholds; never auto-spend because sunk cost is high.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
