# Contract — reference-binding

## Runtime capability aliases
- `reference_selection`
- `character_reference_plan`

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
Use this skill when a work order or user request clearly needs: Select and bind authorized character/world/style references to a shot while preserving provenance and usage constraints.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- More references are not automatically better; conflicting anchors can reduce adherence.
- Identity reference and style reference must not silently redefine each other.
- A reference with unclear rights is unusable for production even if visually ideal.

## Skill-specific output shape
- reference binding set
- purpose per reference
- compatibility scores/findings
- rights/consent links
- stale-reference blockers

## Skill-specific quality checks
- Every reference has project provenance and intended role.
- No bound reference contradicts current canon/state.
- Reference versions are immutable and exact.

## Handoff
prompt-compilation/model-routing/generative supervisor.

## Example
The binding chooses approved face, wardrobe and location-state versions that match this exact scene and records why each is authoritative.

## Counterexample
The newest image in a folder is automatically used even though it depicts an obsolete costume.
