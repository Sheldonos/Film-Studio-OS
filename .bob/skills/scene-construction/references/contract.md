# Contract — scene-construction

## Runtime capability aliases
- `scene_card_generation`
- `scene_writing`
- `scene_function_audit`
- `scene_necessity_test`

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
Use this skill when a work order or user request clearly needs: Turn approved story objectives into playable scenes with obstacles, tactics, turns, visual behavior and momentum.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- A scene without a turn must justify itself as atmosphere, suspense, montage or setup with measurable downstream value.
- Do not make every participant verbally state their goal.
- Production feasibility may change staging/coverage, not secretly alter approved narrative intent.

## Skill-specific output shape
- SceneCard revision
- SceneBeat list
- playable scene/action/dialogue draft
- incoming/outgoing state delta
- production-risk flags
- handoff notes

## Skill-specific quality checks
- Scene changes at least one meaningful state.
- Objectives/tactics are playable and not identical.
- Continuity and source/mandate constraints resolve.

## Handoff
dialogue-voice-subtext, director-breakdown, script-audit-revision.

## Example
A negotiation begins after pleasantries, each offer changes leverage, a hidden deadline is revealed, and the scene exits on an irreversible concession.

## Counterexample
Two characters explain information they both already know and leave with the same goals, power and knowledge they entered with.
