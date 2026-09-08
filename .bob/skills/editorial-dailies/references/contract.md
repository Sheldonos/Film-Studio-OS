# Contract — editorial-dailies

## Runtime capability aliases
- `dailies_review`
- `edit_compatibility_scoring`
- `assembly_edit`
- `scene_pacing_evaluation`
- `edit_qc`

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
Use this skill when a work order or user request clearly needs: Compare takes, test edit compatibility, build assemblies, diagnose pacing and identify pickups without hiding continuity defects.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- The best isolated take may not be the best cut.
- Reaction timing and off-screen sound can carry story; do not over-cut merely because coverage exists.
- Picture lock is human-authorized and cannot be inferred from lack of notes.

## Skill-specific output shape
- DailiesDecision per take
- select/alt/reject list
- rough assembly/timing
- pickup list
- stale editorial regions

## Skill-specific quality checks
- Every selected take passed required gates.
- Reject reasons and alternatives recorded.
- Sequence remains causally/spatially comprehensible.

## Handoff
editor, director, post/VFX/sound; picture-lock human gate.

## Example
Dailies rank takes by story beat, performance, continuity and cut compatibility, preserving rejection reasons for pickup planning.

## Counterexample
The sharpest-looking take is selected even though the reaction lands too early for the edit.
