# Contract — project-intake-diagnostic

## Runtime capability aliases
- `production_readiness_diagnostic`
- `development_question_backlog`

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
Use this skill when the user or work order explicitly requests: Audit a new book, script, treatment or evidence package for missing decisions, risks and prioritized questions before development begins.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- A completeness score measures declared inputs only; it is never a greenlight or quality score.
- Ask consolidated, decision-changing questions rather than an unbounded creative questionnaire.
- Rights, consent, budget, safety and approval gaps remain unresolved until evidence or an authorized owner answers.

## Skill-specific output shape
- ProductionReadinessDiagnostic
- blocking and nonblocking gap registers
- prioritized question backlog
- skill/workflow routing plan
- provenance fingerprint

## Skill-specific quality checks
- Every gap has a question and consequence.
- No answer is fabricated from the source text.
- Blocking decisions appear before optional exploration.

## Handoff
studio_orchestrator for routing, rights_clearance_supervisor for rights evidence, line_producer for feasibility and the authorized project owner for answers.

## Example
A licensed-novel feature arrives with no edition, adaptation mandate or target runtime. The diagnostic cites those three gaps, asks the rights and creative owners once, and routes the project to source intake before outlining.

## Counterexample
Bob reads a manuscript, assumes worldwide adaptation rights and a two-hour runtime, then starts writing scenes without asking who owns those decisions.

