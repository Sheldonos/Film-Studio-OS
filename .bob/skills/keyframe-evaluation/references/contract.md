# Contract — keyframe-evaluation

## Runtime capability aliases
- `keyframe_evaluation`
- `composition_lighting_qc`

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
Use this skill when a work order or user request clearly needs: Evaluate keyframes for composition, identity, world state, lighting, continuity and motion readiness before video generation.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- A beautiful still that cannot animate or cut is not an accepted keyframe.
- Identity/continuity hard failures do not average with aesthetics.
- Repair locally when the defect is localized and preserves approved composition.

## Skill-specific output shape
- KeyframeEvaluation
- per-dimension findings/scores
- hard blockers
- motion-readiness decision
- repair/regeneration recommendation

## Skill-specific quality checks
- Comparison uses exact state/reference versions.
- Decision separates technical blocker from preference.
- Selected keyframe has adequate edit/motion handles.

## Handoff
motion-performance-planning or generation-failure-repair.

## Example
A keyframe passes composition and identity but fails prop orientation, so it is corrected before motion generation rather than hoping video generation fixes it.

## Counterexample
A visually striking frame advances despite using the wrong character identity.
