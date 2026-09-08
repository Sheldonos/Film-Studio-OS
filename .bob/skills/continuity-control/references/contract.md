# Contract — continuity-control

## Runtime capability aliases
- `continuity_extraction`
- `continuity_diff`
- `geography_continuity`
- `screen_direction_validation`
- `action_state_tracking`

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
Use this skill when a work order or user request clearly needs: Extract, inherit, compare and report authoritative continuity state across scenes, shots, props, geography, knowledge and screen direction.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Continuity is causal state, not pixel sameness.
- The most recent relevant canonical state wins; stale takes never update continuity.
- Unknown state stays unknown—do not invent an answer to satisfy a generator.

## Skill-specific output shape
- CharacterState/EnvironmentState/PropState deltas
- continuity constraints for ShotSpec
- violation findings
- stale descendant set
- intentional-discontinuity approvals

## Skill-specific quality checks
- Every state delta has a cause/source version.
- Screen direction/geography checks match planned edit neighbors.
- Stale/rejected takes never become state authority.

## Handoff
shot-specification, continuity-qc, editor.

## Example
Shot B inherits jacket state, prop hand, screen direction and time-of-day from Shot A and flags only the changed emotional state.

## Counterexample
A continuity pass checks wardrobe color but ignores that the character crosses the axis and teleports a prop between hands.
