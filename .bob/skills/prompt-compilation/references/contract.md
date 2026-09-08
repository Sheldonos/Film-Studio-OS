# Contract — prompt-compilation

## Runtime capability aliases
- `prompt_compilation`
- `negative_constraint_compilation`
- `prompt_versioning`

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
Use this skill when a work order or user request clearly needs: Compile canonical shot intent into a structured provider-neutral prompt packet with field-level provenance and negative constraints.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Prompt wording never outranks ShotSpec.
- Unsupported provider fields remain explicit warnings rather than silently dropped intent.
- Use structured layers where they improve control; do not concatenate every database field.

## Skill-specific output shape
- canonical PromptPacket
- unsupported-field warnings
- provenance/compiler version
- negative constraints
- reference bindings

## Skill-specific quality checks
- Same canonical inputs yield same packet hash.
- All critical ShotSpec fields are represented or explicitly unsupported.
- No provider/model identifier leaks into domain intent.

## Handoff
model-routing/provider-job-operation.

## Example
Canonical intent is compiled into identity, state, action, camera, lighting, reference and negative-constraint layers while retaining upstream IDs.

## Counterexample
Vendor-specific syntax is written back into the canonical ShotSpec and becomes the only source of camera intent.
