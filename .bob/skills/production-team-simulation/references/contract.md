# Contract — production-team-simulation

## Runtime capability aliases
- `production_role_coverage`
- `department_contribution_synthesis`

## Authoritative inputs
- Project identifier, project type, lifecycle stage set and physical/hybrid/generative production route.
- Versioned creative package, rights/consent state and optional verified human assignments.
- `policies/production_role_registry.json` with exactly 227 unique role identifiers.

## Missing-input behavior
Fail closed for a missing project identifier, invalid route/type, incomplete role registry, required human authority, rights record, consent or approval. Optional assignees may be absent only when the plan reports them as blockers.

## Output contract
Return a `ProductionTeamContributionPlan` with exactly 227 unique contributions, summary counts, department owner, applicability reason, provenance, human assignee if verified, blockers and readiness state.

## Failure taxonomy
- `incomplete_role_registry`
- `duplicate_role_disposition`
- `invalid_project_context`
- `missing_required_human`
- `rights_or_consent_block`
- `owner_boundary_violation`
- `stale_input`
- `independent_review_required`

## Recovery
Repair the project context or registry, verify the named human assignment, then regenerate the complete matrix. Never erase a role to make the plan appear ready. Require independent review after material changes.

## Positive trigger example
Use this skill to simulate department contributions for a generative feature and identify which real legal, finance, rights, consent and safety authorities remain required.

## Negative trigger example
Do not use it to claim that Bob has hired a crew, obtained a permit, cleared rights, approved a stunt or replaced a licensed professional.

## Skill-specific decision rules
- Every registry role receives exactly one of required_human, simulated_advisory, combined_coverage or not_applicable.
- Documentary-only and animation-only roles are filtered by project type, never silently omitted.
- Physical execution roles can be combined coverage on a generative route, while non-delegable authority remains human.

## Skill-specific output shape
- Project context and selected stages
- 227-row contribution matrix
- Disposition summary and readiness flag
- Required-human blocker list
- Department conflict and handoff summary

## Skill-specific quality checks
- Role count equals registry count and role IDs are unique.
- Every applicable role has an accountable Bob persona or a verified human assignee.
- No advisory simulation is labeled as legal, safety, consent, employment or financial approval.

## Handoff
studio_orchestrator and line_producer; human producer, counsel or qualified specialist for each blocker; qc_supervisor for independent coverage review.

## Example
A generative animated series dispositions all 227 roles, activates animation and episodic departments, combines physical set perspectives, and blocks release until counsel and rights assignments are present.

## Counterexample
A plan lists only twelve department heads and declares the project staffed, silently omitting child welfare, clearance, localization, accessibility and deliverables responsibilities.
