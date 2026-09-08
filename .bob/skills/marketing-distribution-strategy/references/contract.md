# Contract — marketing-distribution-strategy

## Runtime capability aliases
- `audience_release_strategy`
- `distribution_delivery_plan`

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
Use this skill when the user or work order explicitly requests: Develop audience, positioning, publicity, festival, sales and delivery strategies tied to rights, evidence and project maturity.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- Bob never represents a festival selection, buyer interest, rating, revenue forecast or distribution deal as fact without evidence.
- Publicity assets cannot use likeness, music, artwork, quotations or archive material beyond documented permissions.
- Current platform, festival and ratings requirements must be verified at decision time.

## Skill-specific output shape
- audience and positioning brief
- campaign asset/clearance map
- festival and distribution scenarios
- measurement and budget plan
- territory/window/delivery matrix

## Skill-specific quality checks
- Claims are labeled evidence, hypothesis or unknown.
- Every public asset has a clearance dependency.
- Release scenarios expose current-rule verification and human approval gates.

## Handoff
studio_orchestrator for commercial decisions, rights_clearance_supervisor for publicity clearances, localization_delivery_supervisor for territories/accessibility and authorized marketing/distribution humans for outreach and spend.

## Example
A documentary gets three release scenarios, an evidence-labeled audience hypothesis, trailer/EPK clearance map and festival eligibility questions, with no claim that a buyer or festival has accepted it.

## Counterexample
Bob promises viral reach, submits to festivals, buys ads and uses unlicensed music and subject images without current rules or human approval.

