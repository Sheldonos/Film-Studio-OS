# Film Studio OS v0.4.0 — IBM Bob Master Package

A **provider-neutral, rights-aware, quality-gated Film Studio Operating System** for IBM Bob and a repository-owned Python runtime. It accepts properly owned/licensed source material and coordinates development/adaptation, screenplay work, canon, direction/previs, dry-run generation, QC, editorial/post, localization, delivery and archival lineage.

This version is a **production-foundation / governed-integration release**. Core workflows and pilots run locally. Live paid provider execution remains disabled by default and requires an adapter-level request-bound approval, cost preflight, rights/consent clearance and explicit operator authorization.

## What is executable now

- IBM Bob project package: 8 modes, 26 least-privilege department personas, 51 deep active skills, rules, direct-provider command guards, bounded MCP config and structural validator.
- 105 registered runtime capabilities used by 23 v2 workflow families plus 5 reproducible pilot workflows.
- Executable master routes for book-to-film and script-to-feature, series, animation and documentary.
- A deterministic first-project diagnostic that identifies blocking gaps, asks prioritized questions and routes to the right lifecycle skills without inventing decisions.
- Deep, runtime-backed workflows for casting and character look development; costume/hair/makeup; script breakdown and scheduling; location scouting; production design; physical operations; safety coordination; production sound; business affairs/finance packaging; and marketing/distribution.
- A deterministic 227-role production registry and contribution planner. Every role is dispositioned; Bob advisory simulation never impersonates legal, finance, safety, consent, employment or final-approval authority.
- Persistent SQLite work orders/events, retries, independent review, human approval pauses, budgets, resume, cancellation, targeted artifact invalidation and critical-path reporting.
- Immutable artifact versions, hashes, dependencies, decisions/approvals, provider-job records, metrics and reproduction manifests.
- Strict Pydantic/domain models plus v2 JSON Schemas for rights, consent, approvals, work orders, shots, QC and provider jobs.
- Safe source ingestion for text/Markdown/Fountain/SRT/VTT/CSV/DOCX/EPUB/FDX and optional PDF.
- Capability-based provider adapters with a zero-cost idempotent mock and a production-contract Higgsfield CLI adapter. Higgsfield supports live schema discovery, 15-section PromptSpec compilation, correct positional job-set syntax, cost preflight and request-bound approval; it is disabled by default.
- Hard-blocker-aware QC, rights/consent release blocking, untrusted-input guards and package/repository validators.

## Architecture

`Bob / CLI / MCP -> canonical domain -> persistent workflow engine -> immutable artifacts & provenance -> adapter/tool boundary -> layered QC -> archive/reproduction`

Creative intent never compiles directly into vendor-specific syntax. The domain path is:

`source -> rights/brief -> adaptation/story -> approved script -> canon -> director/previs -> ShotSpec -> strategy/references -> provider adapter -> take -> independent QC -> edit/post -> release gate -> archive`

## Bootstrap, install and validate

```bash
python scripts/bootstrap_bob.py
python scripts/bootstrap_bob.py --install
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m film_studio_os validate-bob
python -m film_studio_os validate-package
pytest -q
```

The installer adds the `dev`, `ingest` and `mcp` extras. It does not install/authenticate Higgsfield or authorize external work. See `AGENTS.md` for Bob mode/skill discovery and failure recovery.

## Start every project with a gap audit

```bash
film-studio diagnose-project \
  --project my-project \
  --source-type book \
  --project-type feature \
  --production-route hybrid
```

The report distinguishes blocking from nonblocking gaps, explains why each answer matters and produces an ordered question backlog. Supply approved answers in JSON with `--answers` and rerun before downstream development.

## Reproducible no-spend pilots

```bash
python -m film_studio_os pilot animated-short
python -m film_studio_os pilot dialogue-scene
python -m film_studio_os pilot action-sequence
python -m film_studio_os pilot documentary-segment
python -m film_studio_os pilot episodic-linked-scenes
```

These pilots use internally authored fixtures, explicit fixture rights, separate fixture reviewer identities and `mock-generation`; they do not authorize external actions.

## Master production routes

```bash
python -m film_studio_os validate-workflow workflows/v2/book_to_film_v2.json
python -m film_studio_os validate-workflow workflows/v2/script_to_film_v2.json
python -m film_studio_os validate-workflow workflows/v2/script_to_series_v2.json
python -m film_studio_os validate-workflow workflows/v2/script_to_animation_v2.json
python -m film_studio_os validate-workflow workflows/v2/script_to_documentary_v2.json
python -m film_studio_os validate-workflow workflows/v2/development_diagnostic_v2.json
python -m film_studio_os validate-workflow workflows/v2/casting_character_lookdev_v2.json
python -m film_studio_os validate-workflow workflows/v2/physical_preproduction_v2.json
python -m film_studio_os validate-workflow workflows/v2/production_day_v2.json
python -m film_studio_os validate-workflow workflows/v2/release_business_v2.json
python -m film_studio_os team-plan --project demo --project-type feature --production-route generative --summary-only
```

Workflow execution is restart-safe and pauses for required human approval and independent review. The team plan may be generated with blockers; production execution is not ready until its required human assignments are resolved.

## IBM Bob

Open the project only after reviewing `AGENTS.md` and `.bob/`. Project modes are in `.bob/custom_modes.yaml`, personas in `.bob/agents/`, active skills in `.bob/skills/`, and the local bounded MCP surface in `.bob/mcp.json`. The first-run contract tells Bob how to check/install packages, verify project skill discovery and recover from setup gaps. `film-studio validate-bob` checks structure/frontmatter; actual discovery in an installed Bob IDE remains an environment-level smoke test and is not claimed by this repository validator.

## Compatibility

The original v0.1 agents/skills remain preserved as historical/runtime compatibility material. All 178 legacy skill identifiers have migration metadata; Bob activation is intentionally limited to 51 deeper skills rather than activating generic shells. See `policies/skill_migration_v0_1_to_v0_2.json`, `policies/capability_aliases.json`, and `docs/audit/migration_map.json`.

## Provider boundary

No live paid provider adapter is enabled by default. `film_studio_os.adapters.HiggsfieldCLIAdapter` implements the current official CLI shape but fails closed unless all external-action gates pass. The local Bob MCP server intentionally exposes no live-submit or approval-decision tool. `adapters/higgsfield_cli.py` remains a corrected dry-run compatibility shim.

## Operations

See `docs/operations/INSTALL_AND_RUNBOOK.md`, `docs/operations/RELEASE_CHECKLIST.md`, `docs/research/`, `docs/audit/`, `docs/adr/`, and `docs/validation/`.
