<!-- LEGACY RUNTIME CATALOG: not IBM Bob activation. Active parent: cinematography-design. -->
---
skill_id: camera_motion_design
name: Camera Motion Design
department: camera_lighting_previs
owner_agent: cinematographer
version: 0.1.0
---

# Camera Motion Design

## Purpose
Use static/pan/track/handheld/zoom/crane/orbit only when motivated by subject, reveal or emotion.

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
- `test_camera_motion_design_schema`
- `test_camera_motion_design_boundary`
- `test_camera_motion_design_provenance`
