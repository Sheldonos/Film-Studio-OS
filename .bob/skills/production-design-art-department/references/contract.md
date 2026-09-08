# Contract — production-design-art-department

## Runtime capability aliases
- `production_design_package`
- `art_department_execution_plan`

## Authoritative inputs
- Versioned source and upstream artifacts required by the procedure.
- Locked creative invariants plus relevant rights, consent and approval records.
- Applicable budget, schedule, jurisdiction, provider-policy, safety and quality constraints.

## Missing-input behavior
Fail closed for missing rights, consent, required human approval, authoritative version, locked-invariant context or a decision that would make the output misleading. Record ordinary optional omissions and continue only when the result remains valid.

## Output contract
Return structured, versioned results with `schema_version`, project/artifact identifiers, exact upstream version IDs, decisions/findings, evidence versus assumption labels, confidence where uncertain, provenance, downstream consumers, acceptance state and escalation owner.

## Failure taxonomy
- `missing_authoritative_input`
- `stale_or_conflicting_input`
- `rights_or_consent_block`
- `locked_invariant_conflict`
- `human_authority_boundary`
- `schema_or_quality_failure`
- `safety_or_jurisdiction_escalation`
- `budget_schedule_or_provider_block`

## Recovery
Repair locally when evidence supports it, preserve the superseded version, rerun only invalidated descendants and route consequential uncertainty to the accountable human. Never turn an unresolved dependency into an invented fact.

## Positive trigger example
Use this skill when the user or work order explicitly requests: Turn the world bible into buildable sets, props, graphics, dressing and virtual art-department execution packages.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- Visual references guide intent but never prove the right to reproduce a protected design, logo or artwork.
- Engineering, structural, electrical, rigging, fire and hazardous-material decisions require qualified humans.
- Design canon, construction data and scene-state continuity remain separately versioned.

## Skill-specific output shape
- production design bible
- set/prop/graphic breakdowns
- build/procurement schedule
- scene-state ledger
- clearance and technical handoff register

## Skill-specific quality checks
- Every build or prop maps to scenes and camera needs.
- Protected graphics and artwork have clearance status.
- Physical/virtual interfaces include scale, color and ownership.

## Handoff
production_designer for state ownership, director/cinematographer for camera fit, vfx_supervisor for digital boundaries, line_producer for cost/schedule and qualified art/construction/safety leads for execution.

## Example
A period street set package connects elevations, signage clearance, hero props, rain-state duplicates, VFX extensions, build milestones and scene-specific dressing changes to the locked script.

## Counterexample
Bob produces attractive concept art with no dimensions, scene mapping, clearance, construction sequence or distinction between practical builds and VFX.

