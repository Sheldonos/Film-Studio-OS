# Contract — story-architecture

## Runtime capability aliases
- `premise_stress_test`
- `causal_chain_construction`
- `progressive_complication`
- `setup_payoff_tracking`
- `reveal_ordering`
- `runtime_budgeting`

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
Use this skill when a work order or user request clearly needs: Design or diagnose premise, causal structure, escalation, reveals, setups/payoffs, climax and runtime allocation.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Structure terminology is diagnostic, not mandatory; beats exist only if they change state.
- Escalation must arise from prior choices/constraints, not arbitrary larger events.
- The climax resolves the central dramatic pressure through character action, not external rescue unless that is the premise being argued.

## Skill-specific output shape
- premise stress test
- dramatic-question/story-engine record
- sequence/act map
- causal chain
- setup-payoff ledger
- reveal order
- runtime budget
- structural alternatives/recommendation

## Skill-specific quality checks
- Every major sequence has a causal predecessor/successor.
- Midpoint/crisis/climax change agency, stakes or information.
- Genre/audience promises have explicit fulfillment points.

## Handoff
showrunner/scene-construction; script_editor for independent structure audit.

## Example
A courier chooses to protect a witness, which causes pursuit, forces a betrayal choice at midpoint and makes the climax a consequence of that earlier decision.

## Counterexample
Scenes are arranged as “and then” events that escalate spectacle but not character options or causal pressure.
