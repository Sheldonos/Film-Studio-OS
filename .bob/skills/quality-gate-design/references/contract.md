# Contract — quality-gate-design

## Runtime capability aliases
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
Use this skill when a work order or user request clearly needs: Define hard blockers, required metrics, independent reviewers, weighted preferences and waiver/escalation rules for a production gate.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Missing required evidence is failure, not zero-weight data.
- Do not combine unrelated dimensions into an opaque average.
- Reviewer independence is part of gate validity for high-risk creative artifacts.

## Skill-specific output shape
- versioned GateSpec
- hard-blocker taxonomy
- metrics/rubrics
- review/waiver authority
- test fixtures

## Skill-specific quality checks
- Every required metric has a producer/measurement source.
- Blockers are tested against high-score masking.
- Gate result is reproducible from recorded inputs.

## Handoff
qc supervisor/runtime test suite/workflow owner.

## Example
Rights and corrupt-file findings are hard blockers; composition and rhythm remain weighted preferences with required metrics explicitly enumerated.

## Counterexample
All checks are averaged so a missing consent record can be offset by high image quality.
