# Contract — archive-reproduction

## Runtime capability aliases
- `archive_packaging`
- `reproduction_manifest`
- `lineage_reconstruction`
- `provenance_capture`

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
Use this skill when a work order or user request clearly needs: Create immutable archive and reproduction manifests that trace final artifacts to exact sources, versions, decisions, attempts, QC and approvals.

## Negative trigger example
Do not activate this skill merely because the project is a film; do not use it for unrelated departments or to bypass another role's approval.

## Skill-specific decision rules
- Reproducibility means explainable reconstruction from retained evidence, not a promise that nondeterministic providers return identical pixels.
- Provenance history is immutable; corrections append events/versions.
- Secrets and expired signed URLs are references, never archive payload.

## Skill-specific output shape
- ArchiveManifest
- ReproductionManifest
- checksum list
- environment/version record
- known non-determinism/limitations
- retention constraints

## Skill-specific quality checks
- Every final component traces to sources/decisions/attempts/QC/approvals.
- Hashes validate.
- No secret material or forbidden provider asset is packaged.

## Handoff
production librarian / authorized archive or delivery system.

## Example
The final master manifest walks source, script, shot, take, provider job, QC and approval versions and records where exact reproduction is impossible.

## Counterexample
Only the final MP4 and final prompt are archived, leaving rejected takes, exact source versions, approvals and provider parameters impossible to reconstruct.
