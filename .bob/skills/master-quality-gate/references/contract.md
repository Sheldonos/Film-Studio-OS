# Contract — master-quality-gate

## Runtime capability aliases
- `master_qc`
- `benchmark_evaluation`

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
Use this skill when a work order or user request clearly needs: Run independent master QC with hard blockers for rights, approvals, corrupt assets, continuity contradictions and missing evidence.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- No average score can override missing rights, consent, approval, corrupt media or required technical metric.
- “Provider job succeeded” is irrelevant to master acceptance unless the resulting asset passes gates.
- Release approval is a human decision and remains auditable/revocable according to policy.

## Skill-specific output shape
- MasterQC GateResult
- technical/perceptual/creative findings
- waiver requests
- release blockers
- approved delivery checksum/provenance refs

## Skill-specific quality checks
- All hard blockers zero or explicitly unresolved with no release.
- Reviewer independent of authors of critical artifacts.
- Master hash matches archived/released candidate.

## Handoff
authorized release authority and production librarian.

## Example
Release fails because a required rights approval is missing even though visual, audio and story metrics all score highly.

## Counterexample
A 4.8 aggregate score overrides a corrupt file or legal blocker.
