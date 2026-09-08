# Release Report — Film Studio OS v0.4.0

Release date: 2026-08-15  
Audience: Expert Labs, IBM Bob operators and large-production studio technical/creative operations teams.

## Executive recommendation

**Go With Conditions** for a governed local/dry-run beta. All Critical/High repository findings in the lifecycle expansion are resolved; 51 Bob skills, 105 capabilities and all 28 workflows validate; the 478-case offline harness has zero failures; the wheel builds; and five no-spend pilots remain complete. Promotion to connected or live studio production requires the declared dependency install/normal pytest run, enterprise identity/deployment controls and provider/specialist UAT described below.

## Scope and architecture

The release is a local IBM Bob project package plus Python CLI and optional stdio MCP runtime. It has no web frontend or hosted backend. Bob modes/personas/skills coordinate strict provider-neutral domain models, local SQLite work orders and immutable artifacts through validated JSON workflows. Paid providers sit behind adapters; mock generation is executable by default and Higgsfield is disabled by default.

Final inventory:

- 8 Bob modes, 26 accountable personas and 51 active deep skills.
- 105 registered capabilities, 23 v2 workflow families and 5 pilots (28 files, 178 step references).
- 227 production roles across 18 departments, with responsibilities, Bob owner, applicability and human-authority disposition.
- Five master source-to-screen routes, each with a mandatory immediate post-ingest project diagnostic.
- Five new lifecycle workflows: development diagnostic, casting/character lookdev, physical preproduction, production day and release/business.
- SQLite state, approval/reviewer boundaries, retry/resume, budgets, metrics, provider jobs and reproduction manifests.
- Mock and Higgsfield adapters, 15-section PromptSpecV3, direct-provider command guard and optional-provider runbook.

Architecture and scope evidence: `README.md`, `AGENTS.md`, `docs/ARCHITECTURE.md`, and `docs/audit/USE_CASE_FEATURE_STORY_AUDIT_v0.4.0.md`.

## Findings and remediation

Resolved:

- High: no fresh-clone Bob dependency/mode/skill-discovery bootstrap.
- High: no deterministic “gaps and questions” artifact before development.
- High: 12 lifecycle domains existed mainly as roles or legacy aliases, not substantive active skills and reachable capabilities.
- Medium: onboarding/counts could conflate named role coverage with executable skill coverage.

Disproved: no claim is made that Bob project skills require pip installation; official IBM documentation shows they are discovered from `.bob/skills/`.  
External dependencies: installed Bob IDE discovery, standard dev dependencies in this sandbox, live Higgsfield account behavior, qualified physical-production specialists and current local rules.  
Pending later deployment decisions: enterprise identity/tenant architecture and which studio systems of record receive first-class connectors. Neither is silently selected in this release.

## Independent verification

- High-01: ✅ Verified Fixed — default bootstrap is read-only; installation is explicit and recovery is actionable.
- High-02: ✅ Verified Fixed — unanswered requirements remain gaps; CLI/MCP/workflow paths work; all five master routes diagnose immediately after ingestion.
- High-03: ✅ Verified Fixed — 12 skill contracts, 24 capabilities and five lifecycle DAGs resolve with independent review and human boundaries.
- Medium-01: ✅ Verified Fixed — version/counts and active-versus-legacy language agree across package entry points.

Actual source excerpts and focused evidence are in `docs/audit/INDEPENDENT_VERIFICATION_v0.4.0.md`.

## Validation matrix

| Result | Command/check | Evidence |
|---|---|---|
| PASS | `python -m compileall -q film_studio_os` | 0 syntax errors |
| PASS | `python -m film_studio_os validate-bob --root .` | 8 modes, 26 personas, 51 skills |
| PASS | `python -m film_studio_os validate-package --root .` | 105 capabilities, 28 workflows, 178 step references, 0 errors |
| PASS | `python -m film_studio_os validate-release --root . --ignore-runtime-caches` | valid, 0 hygiene issues |
| PASS | `validate-workflow` over every v2 and pilot JSON | 28/28 valid and acyclic |
| PASS | five `film-studio pilot` runs | 5/5 complete, 0 external cost, 75–82 events each |
| PASS | supplemental offline compatibility harness | 478 passed, 0 failed |
| PASS | `PIP_NO_INDEX=1 python -m pip wheel --no-deps --no-build-isolation .` | `film_studio_os-0.4.0-py3-none-any.whl`; SHA-256 `61b35c569d82f8bbea1510598bcbad2ca4c4dae0c681684e748ce72d3221ed2b` |
| SKIP | `pytest -q` with the real pytest package | pytest is not installed in the sandbox; the supplemental harness is reported separately, not as pytest |
| SKIP | backend static type check | no mypy/pyright command configured |
| SKIP | frontend type check | no frontend exists in this package |
| SKIP | lint | no configured linter command |
| SKIP | separate integration suite | integration behavior is covered within current tests/pilots, but no separate command is configured |
| SKIP | browser e2e | no browser UI exists |
| SKIP | live Higgsfield e2e | no provider credentials or paid-action authorization supplied |

## First-time user journeys

Complete: Bob setup/readiness guidance; initial book/script/source gap audit; source ingestion; book adaptation; screenplay/series/animation/documentary development; casting/look/appearance planning; physical preproduction; governed production-day planning; production sound; post/localization/archive; business/finance/release planning; team coverage; and five pilots.

Incomplete with explicit recovery: live Higgsfield UAT and hosted multi-user enterprise deployment. Neither flow reports a false success.

Detailed evidence: `docs/audit/FIRST_TIME_USER_JOURNEYS_v0.4.0.md`.

## Beta readiness and open risks

No Must Fix Before the governed local beta remains.

Must resolve before live enterprise deployment:

1. SSO/RBAC, tenant isolation, centralized secrets, hosted audit storage, backup/retention and deployment threat model.
2. Normal `pytest -q` in connected CI after installing `.[dev,mcp,ingest]`.
3. Current jurisdiction/union/safety sources and qualified human department ownership for physical production.
4. Studio-authorized low-cap Higgsfield UAT before any live paid production.

Should resolve during beta: studio-owned creative benchmarks, a configured linter/type checker, and selected systems-of-record requirements.

## Release contents and operations

The release archive contains source, Bob configuration, runtime, schemas, policies, workflows, tests, examples and documentation. It excludes environment files, credentials, approval records, local databases, caches and generated media.

Upgrade notes:

- Package version moves from 0.3.0 to 0.4.0.
- Active skills move from 39 to 51; capabilities from 81 to 105; validated workflows from 23 to 28.
- `AGENTS.md` is now a bootstrap and operating contract; `scripts/bootstrap_bob.py` provides check/install paths.
- Every master route adds the deterministic project diagnostic after source ingestion.
- Five workflow families cover the adjacent lifecycle responsibilities added in this release.
- Existing SQLite records need no migration; additions are backward-compatible artifacts/capabilities.

Rollback: retain the v0.3.0 archive and state backup; unset `FILM_STUDIO_EXTERNAL_AUTHORIZED`; use the prior package with existing immutable artifacts. Do not downgrade or reinterpret v0.4 lifecycle artifacts without preserving their versions.

Observability: use bootstrap JSON, project diagnostics, work-order states, events, metrics, provider job IDs, request hashes, approvals and reproduction manifests. Do not log credentials, private performer data or committed approval files.

## Decision and release identifiers

Recommendation: **Go With Conditions**  
Recommended Git commit: `feat: release IBM Bob Film Studio OS lifecycle master v0.4.0`  
Recommended tag: `v0.4.0-beta.1`
