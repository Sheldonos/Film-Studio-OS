# Contract — color-finishing

## Runtime capability aliases
- `color_normalization`
- `shot_matching`
- `look_grade`
- `sequence_grade_continuity`
- `delivery_color_check`

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
Use this skill when a work order or user request clearly needs: Normalize and match shots, design the creative grade, preserve identity/skin, and verify delivery color requirements.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Shot matching serves continuity; creative contrast can intentionally differ with director/colorist approval.
- A LUT/reference is not a complete color-management pipeline.
- Unknown color metadata blocks technical delivery validation.

## Skill-specific output shape
- grade decision record
- shot-match findings
- look/trim instructions
- color metadata requirements
- delivery variant plan

## Skill-specific quality checks
- Adjacent shots match intended scene state.
- Look does not violate identity/skin/critical art intent.
- Technical color fields are measured or explicitly unavailable.

## Handoff
master-quality-gate/localization_delivery_supervisor.

## Example
Shot matching first normalizes exposure/white balance across the sequence, then the creative grade is applied under an explicit display/delivery target.

## Counterexample
A creative LUT is applied independently to each shot before continuity matching.
