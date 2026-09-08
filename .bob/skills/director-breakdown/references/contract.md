# Contract — director-breakdown

## Runtime capability aliases
- `scene_intention_breakdown`
- `performance_objective_design`
- `blocking_plan`
- `shot_priority_map`
- `pickup_identification`

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
Use this skill when a work order or user request clearly needs: Translate scene meaning into audience information, performance intention, blocking, coverage priorities and pickup protection.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Ask “what must the audience experience?” before “what should we generate?”.
- Coverage is insurance against performance/edit risk, not a quota of shot sizes.
- A technically difficult action may be reblocked if dramatic meaning and continuity remain intact.

## Skill-specific output shape
- DirectorBreakdown
- performance objectives/tactics
- blocking/geography plan
- visual information order
- coverage priorities
- pickup protection

## Skill-specific quality checks
- Every planned shot/coverage need traces to dramatic or editorial purpose.
- Blocking is spatially coherent.
- Performance notes are playable, not adjectives alone.

## Handoff
cinematography-design, coverage-storyboard-previs, shot-specification.

## Example
The breakdown says the audience should discover the betrayal through the listener’s reaction before the speaker confirms it, driving performance and coverage choices.

## Counterexample
The director breakdown begins with a camera model and lens before defining dramatic intention.
