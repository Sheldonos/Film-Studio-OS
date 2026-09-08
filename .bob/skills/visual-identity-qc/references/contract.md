# Contract — visual-identity-qc

## Runtime capability aliases
- `visual_qc`
- `identity_qc`
- `skin_tone_identity_check`

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
Use this skill when a work order or user request clearly needs: Independently review visual quality, character identity, anatomy, lighting, background stability and prompt/spec adherence.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Continuity of identity allows expression and perspective changes.
- A high aesthetic score cannot offset wrong character/wardrobe/injury state.
- Automated identity confidence below threshold requires review, not forced classification.

## Skill-specific output shape
- identity findings by character
- confidence
- blocker/pass recommendation
- reference versions
- repair target

## Skill-specific quality checks
- All depicted required characters evaluated.
- Reference versions match current canon.
- Uncertainty remains explicit.

## Handoff
qc_supervisor/character_director/generation-failure-repair.

## Example
QC compares face, silhouette, age cues and stable identity features against approved references while allowing scene-state dirt and expression to vary.

## Counterexample
Any visual difference from the hero reference is called identity drift, including intentional wardrobe damage.
