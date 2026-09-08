# Contract — world-character-canon

## Runtime capability aliases
- `world_bible_creation`
- `location_bible_creation`
- `prop_canon_design`
- `wardrobe_canon`
- `identity_state_separation`

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
Use this skill when a work order or user request clearly needs: Create persistent world, location, prop, wardrobe and character identity/state canon for reuse across shots and episodes.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Identity and state are different objects.
- A reference image is evidence/anchor, not sole canon; textual/structured constraints remain authoritative.
- Visual novelty cannot override story-world rules without art-direction approval.

## Skill-specific output shape
- CharacterBible/identity anchors
- WorldBible/LocationBible
- wardrobe/prop/motif canon
- reference acceptance findings
- state/identity separation map

## Skill-specific quality checks
- Canonical IDs are stable and referenced downstream.
- Approved variation boundaries are explicit.
- Rejected variants cannot be selected as canonical by accident.

## Handoff
continuity-control, reference-binding, director/cinematographer, animation technical director.

## Example
A character model sheet separates face/body invariants from scene-specific wet clothing and an injured wrist, while the location bible fixes doorway geography.

## Counterexample
A prompt bakes temporary mud and lighting into the permanent character identity anchor.
