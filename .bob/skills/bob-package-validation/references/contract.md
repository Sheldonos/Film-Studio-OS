# Contract — bob-package-validation

## Runtime capability aliases
- `handoff_validation`

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
Use this skill when a work order or user request clearly needs: Validate Film Studio OS Bob modes, personas, skills, MCP config, hooks and references against current project conventions.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Do not equate a file existing with Bob discovering it.
- Never invent unsupported Bob workflow/config formats.
- A valid static package can still have environment/version limitations; report them.

## Skill-specific output shape
- Bob validation report
- component counts
- errors/warnings
- runtime-discovery caveat

## Skill-specific quality checks
- Zero structural errors for release.
- All active skills/descriptions resolve.
- Actual Bob activation is not claimed without environment evidence.

## Handoff
studio orchestrator/operator.

## Example
Static validation confirms modes, persona/skill frontmatter, references, hooks and MCP syntax, while the report still states that installed-IDE activation was not exercised.

## Counterexample
The package declares “Bob verified” merely because a `.bob` folder exists.
