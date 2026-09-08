# Contract — shot-specification

## Runtime capability aliases
- `shot_spec_compilation`

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
Use this skill when a work order or user request clearly needs: Compile a provider-neutral ShotSpec from locked scene, character, world, performance, camera, continuity and audio intent.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- ShotSpec is canonical production intent; prompts are compiled derivatives.
- A shot cannot be “approved” with stale character/location state.
- If one generation would carry incompatible actions, split coverage rather than overload the prompt.

## Skill-specific output shape
- strict ShotSpecV2
- neighbor/edit relationships
- reference requirements
- quality thresholds
- risk/repair plan

## Skill-specific quality checks
- All required IDs/versions resolve.
- Duration and movement are feasible for chosen strategy.
- Rights/consent references cover depicted/synthesized identities/assets.

## Handoff
reference-binding, prompt-compilation, model-routing.

## Example
A ShotSpec binds story function, character states, action, camera, performance, duration, continuity constraints, references and quality requirements.

## Counterexample
A shot spec is only “cinematic close-up, dramatic lighting, 8K”.
