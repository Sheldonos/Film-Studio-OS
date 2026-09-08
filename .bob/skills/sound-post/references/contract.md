# Contract — sound-post

## Runtime capability aliases
- `dialogue_edit`
- `adr_strategy`
- `sync_validation`
- `foley_design`
- `ambience_design`
- `sound_effects_design`
- `mix_plan`
- `audio_qc`

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
Use this skill when a work order or user request clearly needs: Plan and audit dialogue edit, ADR, sync, Foley, ambience, SFX and mix priorities for a locked or near-locked sequence.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Sound should add physical/story information, not merely fill silence.
- ADR must match character/performance/consent and should not erase useful production texture.
- Missing technical measurement is a blocker for delivery QC, not a guessed pass.

## Skill-specific output shape
- AudioSpec/cue sheet
- dialogue/ADR decisions
- Foley/ambience/SFX plan
- sync findings
- mix/delivery requirements

## Skill-specific quality checks
- Every audible source has purpose/perspective.
- Sync-critical events align to edit.
- Unavailable deterministic metrics remain explicit.

## Handoff
editor/composer/master-quality-gate.

## Example
Dialogue edit, room tone, Foley and ambience support the physical action; ADR is proposed only where intelligibility/performance cannot be repaired cleanly.

## Counterexample
Sound design adds effects to every visible object regardless of perspective or dramatic focus.
