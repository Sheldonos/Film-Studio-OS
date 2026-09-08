# Contract — cinematography-design

## Runtime capability aliases
- `camera_language_design`
- `shot_size_selection`
- `lens_strategy`
- `camera_motion_design`
- `composition_design`
- `lighting_design`

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
Use this skill when a work order or user request clearly needs: Translate dramatic intent into camera grammar, shot size, lens/perspective, movement, composition, depth and lighting plans.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Focal length is a perspective/space decision coupled with camera distance, not “more cinematic = longer lens.”
- Movement must have a reason and an edit endpoint.
- Lighting continuity preserves source direction/ratios while allowing shot-specific exposure/composition needs.

## Skill-specific output shape
- camera/lens grammar
- CameraSpec/LightingSpec
- sequence visual rules
- movement motivations
- depth/focus plan
- technical/generation risk notes

## Skill-specific quality checks
- Camera choices cite intended audience effect.
- Axis/screen-direction plan is compatible with coverage.
- Lighting sources remain spatially plausible across adjacent shots.

## Handoff
coverage-storyboard-previs and shot-specification; continuity supervisor for axis/light state.

## Example
A restrained 50mm eye-level language holds until a power reversal motivates a lower, wider setup and increased subject-background separation.

## Counterexample
Every shot receives a different lens and moving camera because variety is treated as cinematic intention.
