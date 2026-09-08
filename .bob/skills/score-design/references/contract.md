# Contract — score-design

## Runtime capability aliases
- `score_spotting`
- `cue_brief`
- `motif_design`
- `music_transition_design`
- `temp_track_risk_audit`

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
Use this skill when a work order or user request clearly needs: Spot score, define cue and motif function, manage transitions and avoid temp-track imitation risk.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Silence is a valid score decision.
- Music should not tell the audience an emotion the performance contradicts unless counterpoint is intentional.
- Temp love never creates a rights assumption.

## Skill-specific output shape
- spotting sheet
- CueBriefs
- motif ledger
- timing/hit points
- temp-rights warnings
- revision impacts

## Skill-specific quality checks
- Each cue has dramatic purpose.
- Dialogue intelligibility space is planned.
- Motif reuse follows narrative state rather than repetition habit.

## Handoff
composer/sound supervisor/editor/master QC.

## Example
A motif introduced sparsely in uncertainty returns reharmonized after the character’s choice, with spotting notes protecting dialogue and silence.

## Counterexample
Continuous music is used to instruct the audience how to feel in every scene.
