<!-- LEGACY RUNTIME CATALOG: not IBM Bob activation. Active parent: editorial-dailies. -->
---
skill_id: dailies_review
name: Dailies Review
department: editorial_post
owner_agent: editor
version: 0.1.0
---

# Dailies Review

## Purpose
Review all generated takes against story intent, performance, continuity and edit utility.

## Scope
Bounded editorial_post capability; must operate on versioned structured artifacts.

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
- `test_dailies_review_schema`
- `test_dailies_review_boundary`
- `test_dailies_review_provenance`
