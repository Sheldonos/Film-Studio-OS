# Film Studio OS v0.3.0 — Master Technical Audit

Audit date: 2026-08-15  
Scope: all supplied archives and markdown inputs, with `film_studio_os_v0.2.0(2).zip` selected as the broadest canonical base and the strongest non-duplicative material merged from the other packages.

## Architecture Map

| Layer | Technology | Entry Point | Notes |
|---|---|---|---|
| IBM Bob interface | `.bob` modes, personas, skills, hooks | `.bob/custom_modes.yaml`, `.bob/skills/`, `.bob/agents/` | 8 modes, 26 department personas, 39 active bounded skills |
| Local API | Python CLI and optional stdio MCP | `film_studio_os/cli.py`, `film_studio_os/mcp_server.py` | MCP is local/read-bounded and exposes no live provider submission or approval decisions |
| Workflow runtime | Python, JSON workflow definitions | `film_studio_os/workflow.py`, `workflows/v2/` | Persistent dependency execution, approval/review pauses, resume, retries, budgets and lineage |
| Domain/schema | Pydantic v2 and JSON Schema | `film_studio_os/typed_models.py`, `schemas/v2/index.json` | Provider-neutral intent, strict rights/consent/work-order/shot/QC/provider models |
| State/database | SQLite via repository `StateStore` | `film_studio_os/state.py` | Projects, work orders, artifacts, approvals, events, metrics and provider jobs |
| Provider integrations | Adapter interface, mock, Higgsfield CLI | `film_studio_os/adapters/` | Mock is executable/no-spend; Higgsfield is production-contract available but live-disabled by default |
| Media tooling | ffmpeg/ffprobe subprocess argv | `film_studio_os/tools/media.py` | Scoped derivation and deterministic media probes/QC |
| Test infrastructure | pytest tests plus stdlib unittest cases | `tests/` | Dev extra declares pytest; focused offline harness used where sandbox dependency was unavailable |
| Build pipeline | setuptools / PEP 517 | `pyproject.toml` | Package manager: pip; build: `pip wheel --no-deps --no-build-isolation .` |
| Deployment | Local IBM Bob workspace / stdio MCP | `.bob/mcp.json`, `docs/operations/` | No hosted frontend or server deployment; env flag gates external actions; secrets are never committed |
| Documentation | Markdown, ADRs, audit and runbooks | `README.md`, `docs/` | Includes Higgsfield runbook, audit checklists, verification, journeys and release report |

Commands discovered: install `pip install -e '.[dev]'`; package entry point `film-studio`; build `python -m pip wheel --no-deps --no-build-isolation .`; tests `pytest -q`; repository validation `film-studio validate-bob`, `validate-package`, `validate-release`; no configured linter or static type-checker command.

## Findings

### High-01 · Direct Higgsfield commands bypassed the external-action hook [FIXED]
**Severity:** High  
**Location:** `.bob/hooks/pre_tool_guard.py:10-23`  
**Steps to reproduce:** Before remediation, send a Bob command tool input containing `higgsfield generate create kling3_0 --prompt x` without `FILM_STUDIO_EXTERNAL_AUTHORIZED`; the hook returned success because it matched only Film Studio wrapper strings.  
**Root cause:** The original regular expression recognized `film-studio ... --live` or `provider-submit` but no direct Higgsfield create/workflow/upload commands.  
**Recommended fix:** Match the documented side-effecting wrapper and direct provider command forms while allowing read-only discovery; keep adapter approval/cost checks as a second boundary.  
**Effort:** 2 hours.  
**Change summary:** The hook now blocks direct Higgsfield creation, workflow, upload and Soul ID creation commands and explains the remaining gates; focused regression tests cover blocked, read-only and pre-authorized inputs.

### High-02 · Higgsfield adapter used an obsolete command and had no production contract [FIXED]
**Severity:** High  
**Location:** `film_studio_os/adapters/higgsfield.py:15-130`; compatibility shim `adapters/higgsfield_cli.py:16-25`  
**Steps to reproduce:** Before remediation, call the only Higgsfield shim's `build_command`; it emitted `generate create --model ...`, while the current official CLI expects a positional job-set type, and its live path always raised.  
**Root cause:** The repository contained only a dated dry-run shim and no `ProviderAdapter` implementation with schema discovery, cost preflight, request-bound approval or lifecycle normalization.  
**Recommended fix:** Implement the provider contract using current positional syntax and dynamic live schema, keep live disabled by default, and require authorization, cost cap and exact request hash.  
**Effort:** 12 hours.  
**Change summary:** Added a shell-free adapter, current manifest, dry-run/live CLI commands, 15-section request example and IBM Bob/Higgsfield runbook; corrected the legacy shim.

### High-03 · Core book/script use cases lacked executable end-to-end workflows [FIXED]
**Severity:** High  
**Location:** `workflows/v2/book_to_film_v2.json:1-100`, `workflows/v2/script_to_*_v2.json`; compatibility path `workflows/script_to_film.json:1-96`  
**Steps to reproduce:** Before remediation, load `workflows/script_to_film.json` with `load_workflow`; the file used a non-executable `phases` shape and raised `WorkflowValidationError`. No complete book-to-film or format-specific script routes existed.  
**Root cause:** The v2 package had strong departmental workflows but no validated orchestration spine for the requested user-facing conversions; a legacy document remained at the intuitive script path.  
**Recommended fix:** Add the smallest format-specific v2 DAGs reusing registered capabilities, independent reviewers and human gates; replace the misleading legacy path with its executable v2 equivalent.  
**Effort:** 10 hours.  
**Change summary:** Added and validated book-to-film and script-to-feature/series/animation/documentary workflows, with 227-role coverage, mock generation and explicit release gates.

### High-04 · Team simulation could not account for all production roles [FIXED]
**Severity:** High  
**Location:** `policies/production_role_registry.json`; `film_studio_os/team_simulation.py:40-109`  
**Steps to reproduce:** Before remediation, request a role-complete script or production review; only 26 department personas and specialist skills were available, with no deterministic disposition for the 227 supplied production roles.  
**Root cause:** The package correctly avoided one-agent-per-job-title proliferation but did not provide the missing coverage registry and human-authority boundary needed to simulate every role responsibly.  
**Recommended fix:** Import the supplied role/responsibility source as a complete registry and generate exactly one disposition per role under accountable department personas.  
**Effort:** 10 hours.  
**Change summary:** Added all 227 roles across 18 departments, CLI/MCP planning, project-type/stage filtering, required-human blockers, provenance and regression tests.

### Medium-05 · Pilot output reported only the final resume cycle [FIXED]
**Severity:** Medium  
**Location:** `film_studio_os/pilots.py:43-60`  
**Steps to reproduce:** Run any pilot containing independent review pauses; the final JSON previously showed the `executed_steps` value from only the last `WorkflowExecutor.run` call.  
**Root cause:** `result` was overwritten on each resume iteration and the prior cycle counts were not accumulated.  
**Recommended fix:** Accumulate execution transitions across every resume cycle and set the final output after completion.  
**Effort:** 1 hour.  
**Change summary:** Added `total_executed_steps`; all five pilots now report the whole run while preserving complete work-order state.

### Low-06 · Requested audit and release support files were absent [FIXED]
**Severity:** Low  
**Location:** `.bob/skills/repository-release-audit/references/`  
**Steps to reproduce:** Search every supplied archive for `audit-checklist.md`, `verification-checklist.md`, `user-journey-checklist.md` or `release-report-template.md`; none were present.  
**Root cause:** The audit procedure referenced supporting material that was not included with the uploaded packages.  
**Recommended fix:** Add the references as an active, contract-complete IBM Bob audit skill.  
**Effort:** 3 hours.  
**Change summary:** Added all requested references plus invocation examples, runtime capability and validated audit workflow.

### False Positive-07 · Three tests appeared to use pytest without imports
**Severity:** False Positive  
**Location:** `tests/test_adapter_contract_v2.py:3-6`, `tests/test_ingest_v2.py`, `tests/test_artifact_state_v2.py`  
**Steps to reproduce:** Search every `pytest.` use and resolve imports, including function-local imports.  
**Root cause:** The adapter test imports pytest inside the function; the ingest and artifact tests do not use pytest. Source inspection disproved the initial pattern-based suspicion.  
**Recommended fix:** None; do not add unnecessary imports.  
**Effort:** 0 hours.

### Known External Dependency-08 · Live Higgsfield end-to-end execution cannot be certified offline
**Severity:** Known External Dependency  
**Location:** `docs/integrations/HIGGSFIELD_RUNBOOK.md`; `film_studio_os/adapters/higgsfield.py:38-42,94-124`  
**Steps to reproduce:** Attempt live schema/cost/submission verification without an installed authenticated official CLI, paid account and approved project request.  
**Root cause:** Model schemas, account terms, cost and service behavior are live third-party state; the audit environment has no operator authorization or credentials.  
**Recommended fix:** Run provider UAT with a low capped, project-owned fixture after studio security/legal approval; preserve the resulting schema snapshot and job evidence.  
**Effort:** 4 hours plus external approval.

## Product Decision Gate

No source-confirmed Product Decision Required finding was identified. The remediation retained the existing provider-neutral, fail-closed, dry-run-first product policy, so Stage 4 was not blocked.

## Validation summary

- `[PASS] python -m compileall -q film_studio_os adapters .bob/hooks` — 0 syntax errors.
- `[PASS] python -m film_studio_os validate-bob --root .` — 8 modes, 26 personas, 39 skills.
- `[PASS] python -m film_studio_os validate-package --root .` — 81 capabilities, 23 workflows, 143 step references.
- `[PASS] python -m film_studio_os validate-release --root . --ignore-runtime-caches` — 0 errors, 0 hygiene issues.
- `[PASS] all workflows through validate-workflow` — 23/23 load and are acyclic.
- `[PASS] five no-spend pilots` — 5/5 complete with review, provider records and reproduction lineage.
- `[PASS] offline compatibility harness` — 384 focused/unit/contract cases, 0 failures; includes ffmpeg smoke tests.
- `[PASS] python -m pip wheel --no-deps --no-build-isolation .` — built `film_studio_os-0.3.0-py3-none-any.whl`.
- `[SKIP] pytest -q` — declared dev dependency `pytest` is unavailable in this sandbox and network installation is prohibited; no pass is claimed. The compatibility harness is supplemental, not a replacement for release CI.
- `[SKIP] backend static type check` — no mypy/pyright configuration or command is present.
- `[SKIP] frontend type check` — no frontend exists in this package.
- `[SKIP] lint` — no linter configuration or command is present.
- `[SKIP] live Higgsfield e2e` — no credentials, account authorization or paid-action approval supplied.
