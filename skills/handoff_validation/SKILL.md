<!-- LEGACY RUNTIME CATALOG: not IBM Bob activation. Active parent: bob-package-validation. -->
---
skill_id: handoff_validation
name: Handoff Validation
department: studio_governance
owner_agent: studio_orchestrator
version: 0.1.0
---

# Handoff Validation

## Purpose
Reject incomplete cross-department handoffs before downstream agents invent missing decisions.

## Scope
Bounded studio_governance capability; must operate on versioned structured artifacts.

## Out of scope
- final approval outside owner decision rights
- silent mutation of upstream artifacts
- copying protected source-specific expression

## Procedure
1. validate prerequisites
2. load authoritative state
3. perform bounded analysis/generation operation
4. score output against rubric
5. record provenance
6. emit versioned result and handoff

## Decision rules
- do not invent missing upstream decisions
- prefer local repair over global rewrite when scope is local
- escalate when confidence is low and impact is high

## Quality checks
- schema valid
- owner boundary respected
- output traceable
- acceptance test passes

## Failure modes
- missing prerequisite
- scope creep
- generic output
- contradiction with authoritative state
- untraceable result

## Recovery
- request/fetch prerequisite
- narrow operation
- rerun targeted pass
- escalate owner conflict
- rollback to prior version

## Tests
- `test_handoff_validation_schema`
- `test_handoff_validation_boundary`
- `test_handoff_validation_provenance`
