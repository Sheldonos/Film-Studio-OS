# Contract — production-economics

## Runtime capability aliases
- `budget_envelope`
- `critical_path_analysis`
- `production_status_report`

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
Use this skill when a work order or user request clearly needs: Track budget, schedule, attempts, latency, rework, stale-work cost, provider reliability and critical path for production decisions.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Optimize cost per accepted second/artifact and quality-adjusted throughput, not cheapest generation.
- Unknown provider price/policy prevents confident estimate and may block routing.
- Budget authority is distinct from creative authority.

## Skill-specific output shape
- planned/actual CostEvents
- latency/attempt/acceptance/rework metrics
- critical path
- variance forecast
- intervention recommendation

## Skill-specific quality checks
- Costs reconcile to provider/jobs where available.
- Attempt/rework metrics use accepted/rejected status correctly.
- Escalation threshold decisions are recorded.

## Handoff
line producer/studio orchestrator/model-routing.

## Example
Routing compares predicted quality, policy, latency and cost, then tracks actual attempts and stale-work after an upstream revision.

## Counterexample
The budget report counts generated clips but not rejected attempts or repair labor.
