# Contract — motion-performance-planning

## Runtime capability aliases
- `motion_strategy`
- `performance_prompting`
- `motion_physics_qc`

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
Use this skill when a work order or user request clearly needs: Plan motion and performance with physics, anatomy, interaction, camera-motion and temporal-risk constraints.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Motion complexity is a budget/risk variable; prioritize story-critical motion.
- Camera movement should not compensate for weak subject performance.
- Difficult contact interactions may require cutaways/inserts/composites if dramatic meaning is preserved.

## Skill-specific output shape
- MotionPlan
- PerformanceSpec updates
- timed action beats
- camera/subject/environment motion separation
- risk/fallback plan

## Skill-specific quality checks
- Start/end states match continuity.
- Performance timing fits target duration.
- Physical interaction risks have explicit strategy.

## Handoff
provider-job-operation/animation technical director.

## Example
A tense dialogue shot limits body motion, specifies a glance and hand withdrawal tied to a line beat, and chooses camera movement only after that performance plan.

## Counterexample
The prompt asks for “dynamic motion” without stating who moves, why, when or what must remain stable.
