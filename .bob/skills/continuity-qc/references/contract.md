# Contract — continuity-qc

## Runtime capability aliases
- `continuity_qc`

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
Use this skill when a work order or user request clearly needs: Independently fail or flag shot/sequence continuity contradictions across identity, props, wardrobe, geography, light/time and action.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- A continuity contradiction is a hard blocker when it changes story/state comprehension.
- Minor texture variation may be tolerable if invisible at edit speed and below quality threshold.
- Never update canonical state from a rejected take.

## Skill-specific output shape
- ContinuityQC report
- neighbor comparisons
- hard blockers/tolerances
- repair/edit workaround
- state update eligibility

## Skill-specific quality checks
- All explicit ShotSpec constraints checked.
- Edit-frame context included.
- Intentional discontinuities have approval evidence.

## Handoff
editor/generation-failure-repair/continuity supervisor.

## Example
The checker flags a cup switching hands and a reverse shot violating established screen direction while accepting a motivated lighting change after the door opens.

## Counterexample
Continuity is reduced to face similarity, so prop hand, screen direction, geography, wardrobe condition, lighting state and character knowledge are never evaluated.
