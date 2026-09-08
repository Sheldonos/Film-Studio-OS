# Contract — generation-failure-repair

## Runtime capability aliases
- `generation_failure_classification`
- `shot_repair_strategy`
- `failure_classification`

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
Use this skill when a work order or user request clearly needs: Classify generation failure before retry and choose repair, regeneration, alternate coverage, compositing or human escalation.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Do not regenerate when deterministic repair is cheaper and safer.
- Repeated same-class failure triggers strategy change, not identical retries.
- An upstream design defect should invalidate downstream attempts instead of being “prompt engineered around.”

## Skill-specific output shape
- FailureClassification
- RepairPlan
- cost/probability estimate
- new-attempt rationale
- learning record
- post-repair regression results

## Skill-specific quality checks
- Root cause maps to chosen recovery.
- Attempt budget/stop condition enforced.
- Rejected attempts remain reproducible.

## Handoff
generative supervisor, VFX supervisor, director or human artist depending class.

## Example
A stable take with one malformed hand is routed to local repair; a take with identity drift and broken geography is regenerated or replaced by alternate coverage.

## Counterexample
Every failure is answered with another full regeneration regardless of what succeeded.
