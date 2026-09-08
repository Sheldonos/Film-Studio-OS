# Contract — production-safety-coordination

## Runtime capability aliases
- `production_risk_register`
- `specialist_safety_handoff`

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
Use this skill when the user or work order explicitly requests: Identify production hazards and route them to qualified human specialists without issuing safety, medical or legal approval.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- Bob never declares a stunt, effect, location, weapon, medical condition or workday safe.
- Risk rank is triage only and must not be used to waive specialist review or legal obligations.
- Emergency response follows local professionals and production protocols, not generated instructions.

## Skill-specific output shape
- production risk register
- scene-to-hazard map
- specialist and permit dependency matrix
- briefing/evidence checklist
- stop-work escalation register

## Skill-specific quality checks
- Every high-consequence flag has a named human specialist dependency.
- Unknown conditions are not scored as low risk.
- Evidence authorship and expiration are recorded.

## Handoff
line_producer and studio_orchestrator for escalation, qualified local safety and department specialists for decisions, rights_clearance_supervisor for consent and production_librarian for evidence retention.

## Example
A scene with a minor near water, drone plates and simulated gunfire yields three separate specialist handoffs, permit/consent questions and stop conditions; Bob does not prescribe the controls.

## Counterexample
Bob generates a generic safety checklist, labels the shoot low risk and tells the crew that no stunt, child-welfare or aviation specialist is needed.

