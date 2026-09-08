# Contract — costume-hair-makeup

## Runtime capability aliases
- `costume_look_plan`
- `appearance_continuity_plan`

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
Use this skill when the user or work order explicitly requests: Design character appearance, costume plots, fittings and continuity states across story time, scenes and production methods.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- Design must support character and performance without overriding performer dignity, consent, access or health.
- Costume, hair and makeup states are tied to story chronology and scene numbers, not filenames alone.
- Bob proposes and tracks; qualified humans approve fittings, products, prosthetics and performer-facing practice.

## Skill-specific output shape
- costume and appearance bible
- scene-linked look plot
- fitting/test plan
- continuity state cards
- duplicate/sourcing and risk register

## Skill-specific quality checks
- Every look is linked to scenes and chronology.
- Stunt, duplicate and maintenance needs are visible.
- Consent, allergy, cultural and accessibility issues are escalated.

## Handoff
production_designer and character_director for creative approval, continuity_supervisor for scene states, line_producer for schedule/budget and qualified costume, hair, makeup and prosthetics leads for execution.

## Example
A nonlinear thriller gets numbered looks with before/after injury states, duplicate hero coats, hair continuity, wet-down needs and camera tests mapped to every scene and shoot day.

## Counterexample
Bob generates fashionable outfits disconnected from chronology, ignores stunt duplicates and allergies, and treats the resulting images as approved fitting instructions.

