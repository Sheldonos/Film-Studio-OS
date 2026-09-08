# Contract — casting-performance-development

## Runtime capability aliases
- `casting_breakdown`
- `audition_evaluation_plan`

## Authoritative inputs
- Versioned source and upstream artifacts required by the procedure.
- Locked creative invariants plus relevant rights, consent and approval records.
- Applicable budget, schedule, jurisdiction, provider-policy, safety and quality constraints.

## Missing-input behavior
Fail closed for missing rights, consent, required human approval, authoritative version, locked-invariant context or a decision that would make the output misleading. Record ordinary optional omissions and continue only when the result remains valid.

## Output contract
Return structured, versioned results with `schema_version`, project/artifact identifiers, exact upstream version IDs, decisions/findings, evidence versus assumption labels, confidence where uncertain, provenance, downstream consumers, acceptance state and escalation owner.

## Failure taxonomy
- `missing_authoritative_input`
- `stale_or_conflicting_input`
- `rights_or_consent_block`
- `locked_invariant_conflict`
- `human_authority_boundary`
- `schema_or_quality_failure`
- `safety_or_jurisdiction_escalation`
- `budget_schedule_or_provider_block`

## Recovery
Repair locally when evidence supports it, preserve the superseded version, rerun only invalidated descendants and route consequential uncertainty to the accountable human. Never turn an unresolved dependency into an invented fact.

## Positive trigger example
Use this skill when the user or work order explicitly requests: Develop casting breakdowns, audition materials and evidence-based evaluation plans while preserving human hiring, consent and accessibility authority.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- Bob supports casting decisions but never hires, rejects or represents a performer as attached.
- Criteria must be role-relevant and reviewed for bias, accessibility and unlawful discrimination.
- No voice, scan, likeness or audition material may be reused for generation without specific documented consent.

## Skill-specific output shape
- role casting breakdown
- audition-side package
- evaluation matrix
- recall and chemistry plan
- consent/accessibility risk register

## Skill-specific quality checks
- Every criterion maps to performance or production need.
- Human decision authority and accommodations are explicit.
- Digital-replica and audition-data usage are fail-closed.

## Handoff
director and human casting leadership for selection, line_producer for availability/deals, rights_clearance_supervisor for consent and character_director for performance objectives.

## Example
For an ensemble drama, Bob creates five role briefs, protected audition sides and a weighted chemistry rubric, then records conflicts and accommodations for a human casting panel rather than choosing actors.

## Counterexample
Bob scrapes performer images, scores candidates on appearance, declares a winner and treats a self-tape as permission to synthesize the actor's voice.

