# Contract — localization-accessibility

## Runtime capability aliases
- `voice_consistency`
- `loudness_delivery_qc`

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
Use this skill when a work order or user request clearly needs: Prepare translation, dubbing/subtitle/accessibility requirements while respecting voice consent, culture and territory constraints.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Localization can adapt expression, not silently alter plot/claim/character intent.
- Voice cloning/digital replica use requires explicit consent scope for the intended localization use.
- Machine translation output is a draft until required review/QA.

## Skill-specific output shape
- locale translation/dub/subtitle package
- terminology/voice decisions
- cultural-review findings
- consent links
- timing/QC results
- territory variant

## Skill-specific quality checks
- Critical meaning/claims back-check.
- Subtitle/dub timing references locked picture.
- Consent and territory rights cover the locale/version.

## Handoff
localization delivery supervisor/master-quality-gate/archive.

## Example
A translation preserves joke function rather than literal wording, subtitle timing is checked, and a voice consent restriction prevents unauthorized dubbed cloning.

## Counterexample
A dubbed version reuses a performer’s synthetic voice because it sounds close enough.
