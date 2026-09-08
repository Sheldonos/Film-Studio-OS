# Contract — script-breakdown-scheduling

## Runtime capability aliases
- `script_element_breakdown`
- `schedule_budget_scenario`

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
Use this skill when the user or work order explicitly requests: Convert a locked screenplay into traceable element breakdowns, stripboard logic, schedule and budget scenarios without claiming a final production plan.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- A breakdown is version-bound; a revised script invalidates affected scenes and their schedule assumptions.
- Bob may estimate scenarios but cannot approve budgets, union interpretations, hiring or final shooting schedules.
- Hidden labor or safety complexity must be surfaced, not compressed into a generic difficulty score.

## Skill-specific output shape
- element breakdown registry
- scene breakdown sheets
- stripboard-ready scene records
- schedule and budget scenarios
- assumption and invalidation register

## Skill-specific quality checks
- Every extracted element cites a scene or page.
- Scenario assumptions are distinct from commitments.
- Company moves, availability and safety dependencies are visible.

## Handoff
line_producer for schedule and budget decisions, production_designer for build/prop review, continuity_supervisor for state changes and safety specialists for flagged hazards.

## Example
A 102-page script is broken into numbered scenes with cast, props, wardrobe states and location moves; two schedule scenarios show how a night exterior cluster changes cost and actor availability risk.

## Counterexample
Bob estimates a 20-day shoot from page count alone, omits minors and stunts, and presents the number as an approved production schedule.

