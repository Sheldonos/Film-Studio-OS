<!-- LEGACY RUNTIME CATALOG: not IBM Bob activation. Active parent: source-adaptation. -->
---
skill_id: structure_map
name: Structure Map
department: writing_story
owner_agent: showrunner
version: 0.1.0
---

# Structure Map

## Purpose
Create act/sequence architecture linked to state changes rather than beat-label mimicry.

## Scope
Bounded writing_story capability; must operate on versioned structured artifacts.

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
- `test_structure_map_schema`
- `test_structure_map_boundary`
- `test_structure_map_provenance`
