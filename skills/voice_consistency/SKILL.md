<!-- LEGACY RUNTIME CATALOG: not IBM Bob activation. Active parent: localization-accessibility. -->
---
skill_id: voice_consistency
name: Voice Consistency
department: sound_music
owner_agent: sound_supervisor
version: 0.1.0
---

# Voice Consistency

## Purpose
Check timbre, accent/register, pace, emotional state and identity across synthesized/recorded lines.

## Scope
Bounded sound_music capability; must operate on versioned structured artifacts.

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
- `test_voice_consistency_schema`
- `test_voice_consistency_boundary`
- `test_voice_consistency_provenance`
