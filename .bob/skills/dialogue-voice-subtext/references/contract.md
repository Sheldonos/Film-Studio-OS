# Contract — dialogue-voice-subtext

## Runtime capability aliases
- `dialogue_voice_construction`
- `subtext_writing`
- `exposition_concealment`
- `silence_pause_design`
- `interruption_overlap_design`
- `actor_speakability`
- `dialogue_voice_audit`

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
Use this skill when a work order or user request clearly needs: Write or audit differentiated dialogue, subtext, exposition concealment, pauses, interruptions and actor speakability.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Subtext is not vagueness: the audience still needs enough evidence to infer intent.
- A joke that any character could say is a rewrite target.
- If the image carries the information more strongly, prefer behavior/silence over redundant dialogue.

## Skill-specific output shape
- DialogueLine annotations
- revised lines/options
- voice-differentiation score
- subtext/exposition findings
- timing/performance notes
- lines retained/removed with reason

## Skill-specific quality checks
- Each important line has a tactic/listener effect.
- At least pivotal speakers remain distinguishable with names removed.
- No line gives a character knowledge they do not possess.

## Handoff
showrunner for authored changes; script_editor/qc_supervisor for independent audit.

## Example
One character answers a direct apology by asking whether the door is locked, using avoidance and action to reveal distrust without stating it.

## Counterexample
Every character uses the same polished cadence and says exactly what they feel.
