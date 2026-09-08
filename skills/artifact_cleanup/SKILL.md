<!-- LEGACY RUNTIME CATALOG: not IBM Bob activation. Active parent: security-threat-review. -->
---
skill_id: artifact_cleanup
name: Artifact Cleanup
department: generative_vfx
owner_agent: vfx_supervisor
version: 0.1.0
---

# Artifact Cleanup

## Purpose
Remove flicker, morphs, edge chatter, background warping and transient visual defects without changing intent.

## Scope
Bounded generative_vfx capability; must operate on versioned structured artifacts.

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
- `test_artifact_cleanup_schema`
- `test_artifact_cleanup_boundary`
- `test_artifact_cleanup_provenance`
