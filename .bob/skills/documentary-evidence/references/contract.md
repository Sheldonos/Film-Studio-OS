# Contract — documentary-evidence

## Runtime capability aliases
- `provenance_capture`
- `rights_risk_triage`

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
Use this skill when a work order or user request clearly needs: Maintain documentary claims, evidence, source provenance, contradictions, consent and fact-check boundaries.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Absence of contradictory evidence is not proof.
- Never convert an allegation into a fact through narration grammar.
- Editorial rhythm cannot override source meaning or consent scope.

## Skill-specific output shape
- claim/evidence ledger
- counterevidence register
- interview/transcript linkage
- archival-rights findings
- fact-check report
- synthetic/reconstruction disclosure list

## Skill-specific quality checks
- Every material factual claim has a source locator.
- Contradictions/uncertainties remain visible.
- Consent/archival rights status follows each used source into the cut.

## Handoff
showrunner/editor for narrative construction; qc_supervisor and authorized legal/standards reviewer before release.

## Example
A narration claim is linked to two source passages, one conflicting interview is preserved as counterevidence, and unresolved certainty is stated in the finding.

## Counterexample
A strong visual reenactment is treated as proof of a historical event without source linkage or disclosure.
