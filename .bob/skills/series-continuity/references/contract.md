# Contract — series-continuity

## Runtime capability aliases
- `character_state_tracking`
- `relationship_state_tracking`
- `knowledge_state_tracking`

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
Use this skill when a work order or user request clearly needs: Maintain series/season/episode canon and identify cross-episode stale dependencies after upstream changes.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Series canon outranks a single episode draft unless showrunner approves canon change.
- An episodic reset cannot undo an irreversible serialized event without explicit story mechanism.
- Reuse is valid only when the asset’s state/version matches the episode timeline.

## Skill-specific output shape
- series/season continuity ledger
- cross-episode stale-dependency set
- knowledge timeline
- setup-payoff tracker
- episode-lock findings
- recap requirements

## Skill-specific quality checks
- No character acts on unavailable knowledge.
- Cross-episode state changes are monotonic or explicitly reversed on-screen.
- Upstream canon changes identify all affected descendants.

## Handoff
showrunner, episode writer/director, continuity_supervisor, production_librarian.

## Example
An episode-two secret changes what a character can plausibly say in episode four; revising the reveal marks only dependent later scenes stale.

## Counterexample
Episode five uses a prop destroyed in episode three because each episode was reviewed in isolation.
