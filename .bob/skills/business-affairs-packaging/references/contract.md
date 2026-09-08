# Contract — business-affairs-packaging

## Runtime capability aliases
- `business_affairs_checklist`
- `production_finance_package`

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
Use this skill when the user or work order explicitly requests: Build chain-of-title, financing, talent/vendor, insurance, incentive and greenlight dependency packages without giving legal or financial approval.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- Bob does not give legal, tax, investment or labor advice and never signs, negotiates or represents a deal as closed.
- A name in a pitch deck is not an attachment; a budget assumption is not committed financing.
- Sensitive deal and personal data must be minimized, access-controlled and excluded from broad creative artifacts.

## Skill-specific output shape
- chain-of-title and rights matrix
- package/attachment status register
- deal-document checklist
- finance and cash-flow scenarios
- greenlight dependency matrix

## Skill-specific quality checks
- Every claimed right or attachment links to evidence.
- Assumptions and commitments are visibly distinct.
- Jurisdiction-dependent questions have qualified human owners.

## Handoff
rights_clearance_supervisor and authorized counsel for legal review, line_producer for budget/cash flow, studio_orchestrator for greenlight and production_librarian for controlled evidence.

## Example
A book package records option term, screenplay engagement, director target, conditional cast letter, finance scenario and insurance/incentive dependencies without calling any party contracted or funded prematurely.

## Counterexample
Bob interprets contracts, guarantees an incentive, lists uncontacted actors as attached and tells the studio the chain of title is clear.

