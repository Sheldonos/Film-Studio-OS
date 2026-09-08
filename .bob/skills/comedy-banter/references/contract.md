# Contract — comedy-banter

## Runtime capability aliases
- `banter_construction`
- `wit_callback_design`
- `joke_mechanics`

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
Use this skill when a work order or user request clearly needs: Build character-driven wit, banter, joke mechanics and callbacks without interchangeable joke insertion.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Character consequence outranks joke density.
- Do not add interchangeable sarcasm as a substitute for viewpoint.
- A callback earns value by altered context, not repetition alone.

## Skill-specific output shape
- joke/banter beat annotations
- alternate setups/turns/buttons
- callback ledger changes
- tone-risk findings
- performance timing notes

## Skill-specific quality checks
- Every joke is attributable to character/situation.
- Humor does not erase required stakes or information.
- Callbacks have prior setup and changed context.

## Handoff
showrunner/dialogue-voice-subtext; script_editor for tone/comedy audit.

## Example
A meticulous engineer keeps correcting a reckless pilot’s increasingly absurd units of measure; the callback later lands because the correction now has consequences.

## Counterexample
Random punchlines are inserted between dramatic beats even though they do not arise from character, status or situation.
