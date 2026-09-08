<!-- LEGACY RUNTIME CATALOG: not IBM Bob activation. Active parent: none. -->
---
skill_id: transition_previs
name: Transition Previsualization
department: camera_lighting_previs
owner_agent: storyboard_previs
version: 0.1.0
---

# Transition Previsualization

## Purpose
Design match cuts, action cuts, sound bridges, entrances/exits and continuity masks.

## Scope
Bounded camera_lighting_previs capability; must operate on versioned structured artifacts.

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
- `test_transition_previs_schema`
- `test_transition_previs_boundary`
- `test_transition_previs_provenance`
