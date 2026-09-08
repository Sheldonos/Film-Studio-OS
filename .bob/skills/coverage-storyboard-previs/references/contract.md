# Contract — coverage-storyboard-previs

## Runtime capability aliases
- `coverage_plan`
- `storyboard_plan`
- `animatic_timing`
- `generation_risk_previs`

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
Use this skill when a work order or user request clearly needs: Design coverage, storyboard/animatic timing and generation-risk previs before expensive shot production.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Protect the edit, not the shot list.
- A gorgeous storyboard panel that cannot cut with neighbors is a failed coverage design.
- Use fewer stronger setups when they preserve performance and reduce continuity risk.

## Skill-specific output shape
- CoveragePlan
- storyboard panel specs
- animatic timing
- shot priority
- edit-handle requirements
- risk/alternate-coverage plan

## Skill-specific quality checks
- All required story/performance beats have at least one viable coverage path.
- Axis/geography are legible.
- High-risk shots have fallback strategy.

## Handoff
shot-specification, line_producer, generative/animation supervisor.

## Example
The plan protects geography, the accusation, the silent reaction and a clean exit, then uses an animatic to test whether the reveal reads before generation.

## Counterexample
Coverage consists of generic wide/medium/close shots with no mapping to beats or edit protection.
