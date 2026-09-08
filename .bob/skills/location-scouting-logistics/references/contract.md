# Contract — location-scouting-logistics

## Runtime capability aliases
- `location_scout_matrix`
- `location_feasibility_plan`

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
Use this skill when the user or work order explicitly requests: Translate story needs into creative, technical, access, permit, logistics and safety location evaluation packages.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- A web image or map is not proof of access, current condition, ownership, permit or safety.
- Bob cannot issue permits, enter property, approve rigging or declare a location safe.
- Creative fit and operational feasibility must be scored separately so beauty does not conceal blockers.

## Skill-specific output shape
- scene location brief
- candidate scout matrix
- technical scout checklist
- logistics and permit dependency plan
- backup and restoration register

## Skill-specific quality checks
- Remote facts are marked unverified and dated.
- Every candidate has access, sound, power and safety fields.
- A backup or explicit single-point risk exists for critical locations.

## Handoff
director and production_designer for creative fit, line_producer for cost/schedule, production sound for noise review, rights_clearance_supervisor for agreements and qualified location/safety personnel for in-person approval.

## Example
Three mansion candidates are compared for period fit, owner access, sound, truck parking, power, sun, restoration, scan needs and permit lead time; the recommendation remains conditional on a tech scout.

## Counterexample
Bob selects a location from social media photographs, tells production it is permitted and quiet, and omits residents, power, access and weather constraints.

