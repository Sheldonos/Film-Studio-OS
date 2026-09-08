# Contract — model-routing

## Runtime capability aliases
- `model_routing`
- `production_strategy_selection`

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
Use this skill when a work order or user request clearly needs: Route a production task to a compatible provider/model using capability evidence, policy, privacy, quality, latency and cost constraints.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- No single provider is “best”; route per shot/task requirement and evidence.
- Policy incompatibility is a hard filter, not a weighted preference.
- Benchmark evidence expires; stale capability claims trigger re-verification.

## Skill-specific output shape
- RoutingDecision
- eligible/rejected candidate reasons
- primary/fallback
- estimated cost/latency/attempts
- confidence/evidence timestamp

## Skill-specific quality checks
- Every selected capability satisfies hard constraints.
- Unknown privacy/training/rights fields are handled explicitly.
- Decision cites benchmark/capability evidence, not popularity.

## Handoff
provider-job-operation and line_producer for budget threshold.

## Example
A lower-scoring model is selected because the higher-scoring candidate has unknown retention/training policy for a confidential project, and the reason is recorded.

## Counterexample
The router selects whichever model has the highest average benchmark even though commercial use is unverified.
