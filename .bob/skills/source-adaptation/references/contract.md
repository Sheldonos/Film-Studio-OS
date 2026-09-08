# Contract — source-adaptation

## Runtime capability aliases
- `creative_constraint_extraction`
- `structure_map`

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
Use this skill when a work order or user request clearly needs: Convert a licensed book, treatment, article, memoir or source package into a traceable adaptation mandate and change ledger.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Preserve function before surface wording: compress events only if the causal/emotional function remains.
- A newly invented scene must be labeled “add” with a reason; it must not masquerade as source canon.
- Do not merge characters when the merge destroys distinct rights, representation, plot function or later payoff.

## Skill-specific output shape
- AdaptationMandate
- source-to-screen decision ledger
- canon/contradiction map
- target structure mapping
- unresolved author decisions
- fidelity regression findings

## Skill-specific quality checks
- Every adaptation change points to source and mandate.
- No locked invariant changes without approval.
- Removed/merged/reordered material has downstream payoff/continuity analysis.

## Handoff
story_architect/showrunner; rights_clearance_supervisor for scope exceptions.

## Example
An eight-chapter novella becomes a 12-minute short by preserving the central relationship, merging two minor encounters and logging each compression against cited source passages.

## Counterexample
The adaptation invents a new ending that contradicts the locked mandate without an approval record.
