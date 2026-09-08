# Contract — provider-job-operation

## Runtime capability aliases
- `video_generation_plan`
- `keyframe_generation_plan`

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
Use this skill when a work order or user request clearly needs: Estimate, submit, poll, cancel and archive idempotent provider jobs through approved adapters; default to mock/dry-run.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- External spend requires explicit authorization even if credentials exist.
- Retries reuse idempotency identity for the same logical attempt; changed creative input creates a new attempt.
- Provider success means transport completed, not creative acceptance.

## Skill-specific output shape
- ProviderJob
- request/payload hash
- estimate/actual CostEvent
- normalized output artifact refs
- failure classification/recovery hints

## Skill-specific quality checks
- Submit/poll/cancel are auditable.
- No secrets appear in artifacts/logs.
- Actual provider result hash and cost reconcile before handoff.

## Handoff
keyframe-evaluation/visual QC/production librarian; line producer on budget variance.

## Example
The adapter estimates cost, submits once with an idempotency key, persists normalized job state, polls, records actual cost and archives the request hash.

## Counterexample
A timeout triggers a blind resubmit with a new idempotency key and may purchase the same generation twice.
