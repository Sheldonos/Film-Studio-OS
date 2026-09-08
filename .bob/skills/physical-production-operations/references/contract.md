# Contract — physical-production-operations

## Runtime capability aliases
- `production_operations_plan`
- `shoot_day_control`

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
Use this skill when the user or work order explicitly requests: Coordinate prep and shoot-day logistics, call-sheet inputs, crew handoffs, media flow and daily production reporting.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- Bob drafts and reconciles operations artifacts but does not command a set, issue emergency instructions or replace qualified production management.
- Personal contact, medical and payroll data must be minimized and access-controlled.
- Issued call sheets and daily reports are immutable versions; corrections create a new version.

## Skill-specific output shape
- shoot-day operations plan
- reviewable call-sheet dataset
- change and incident ledger
- media/asset transfer log
- daily production report

## Skill-specific quality checks
- Unverified call-sheet fields are visibly pending.
- Turnaround, moves, meals and contingencies are explicit.
- Actuals and issued plans are never silently merged.

## Handoff
line_producer and authorized production management for issue/changes, safety specialists for incidents, continuity_supervisor for state, editor for media notes and production_librarian for archive.

## Example
A two-location day gets a draft call-sheet dataset, verified access and transport fields, weather contingency, card handoff plan and immutable end-of-day actuals for human issuance.

## Counterexample
Bob emails an unreviewed call sheet containing private phone numbers, changes crew calls on its own and overwrites the original when the schedule slips.

