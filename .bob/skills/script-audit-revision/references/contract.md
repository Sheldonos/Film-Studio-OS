# Contract — script-audit-revision

## Runtime capability aliases
- `cold_read_audit`
- `premise_theme_audit`
- `structure_causality_audit`
- `continuity_logic_audit`
- `genre_tone_audit`
- `production_feasibility_audit`
- `revision_plan`
- `revision_regression_audit`

## Authoritative inputs
- Versioned upstream production artifacts required by the workflow step.
- Locked creative invariants and relevant rights/consent/approval records.
- Applicable project budget, schedule, provider-policy and quality constraints.

## Missing-input behavior
Fail closed for missing rights, consent, required approval, authoritative version, required metric, or locked-invariant context. For ordinary optional context, record the absence and continue only when the output remains valid.

## Output contract
Return a structured result with `schema_version`, artifact/work-order identifiers, exact upstream version IDs, decisions or findings, confidence where judgment is uncertain, acceptance result, provenance, downstream consumers, and escalation/handoff state.

## Failure taxonomy
- `missing_authoritative_input`
- `stale_input`
- `rights_or_consent_block`
- `locked_invariant_conflict`
- `owner_boundary_violation`
- `schema_or_contract_failure`
- `quality_gate_failure`
- `budget_or_policy_block`

## Recovery
Repair locally when the failure is local. Do not silently rewrite upstream creative intent. Re-run only invalidated descendants. Escalate high-impact uncertainty to the state owner or required human authority.

## Positive trigger example
Use this skill when a work order or user request clearly needs: Run independent multi-pass screenplay diagnosis, ranked revision planning and regression verification without silent rewrites.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Auditor diagnoses; writer authors. Auditor never silently rewrites the accepted draft.
- Severity follows audience/production consequence, not reviewer preference.
- A revision is complete when the targeted defect is demonstrably improved and regression checks pass—not when prose merely changed.

## Skill-specific output shape
- AuditFinding set
- deduplicated note clusters
- revision plan
- approved change set
- semantic/regression diff
- remaining-risk register

## Skill-specific quality checks
- Author and final reviewer identities differ.
- Every high-severity note has evidence and root cause.
- Revision scope matches authorized change budget.

## Handoff
showrunner for revision, qc_supervisor for independent regression, production_librarian for lineage.

## Example
The audit diagnoses a weak midpoint with scene evidence, proposes three bounded fixes, then regression-checks the selected revision against theme and setup/payoff.

## Counterexample
The auditor silently rewrites six pages and marks its own rewrite approved.
