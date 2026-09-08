<div align="center">

# 🎬 Film Studio OS

**A governed, provider-neutral Film Studio Operating System for IBM Bob/Astra 6**

[![Version](https://img.shields.io/badge/version-v0.4.0-blue?style=flat-square)](./manifest.json)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue?style=flat-square)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![IBM Bob](https://img.shields.io/badge/IBM%20Bob-compatible-purple?style=flat-square)](./AGENTS.md)

*From source material to governed production artifacts — rights-aware, quality-gated, restart-safe.*

</div>

---

## What is Film Studio OS?

Film Studio OS is an AI-powered film production operating system that runs inside **IBM Bob/Astra 6**. It turns properly licensed source material (books, scripts, treatments) into production-ready artifacts — covering every stage from rights intake and screenplay development through generative production, editorial, post, and archival delivery.

It is **not a code-gen toy**. It is a production-grade system with:

- A **227-role accountability registry** — every function in a real film production is modeled and dispositioned
- **Immutable artifact lineage** — every take, decision, approval, rejection and cost event is versioned and traceable
- **Hard governance gates** — rights/consent, independent QC, and human approval authority are enforced, not optional
- **Provider neutrality** — creative intent compiles to a canonical `ShotSpec`; vendor syntax lives only in adapter layers
- **Fail-closed defaults** — live paid generation is off by default; all external actions require explicit multi-gate authorization

---

## Architecture

```
Bob / CLI / MCP
       │
       ▼
 Canonical Domain  ──────────────────────────────────────────────────────────┐
 (story / canon / performance / camera / continuity / audio / delivery)      │
       │                                                                      │
       ▼                                                                      │
 Persistent Workflow Engine (restart-safe, human-approval pauses, budgets)   │
       │                                                                      │
       ▼                                                                      │
 Immutable Artifacts & Provenance (versioned, hashed, reproducible)          │
       │                                                                      │
       ▼                                                                      │
 Adapter / Tool Boundary (mock default │ Higgsfield │ Runway │ Gemini)       │
       │                                                                      │
       ▼                                                                      │
 Layered QC ──► Editorial / Post ──► Release Gate ──► Archive / Delivery ◄──┘
```

**Creative flow:**
```
source → rights/brief → adaptation/story → approved script → canon →
director/previs → ShotSpec → references → provider adapter →
take → independent QC → edit/post → release gate → archive
```

Creative intent **never** compiles directly into vendor-specific syntax.

---

## Key Numbers (v0.4.0)

| Dimension | Count |
|---|---|
| Bob modes | 8 |
| Subagent department personas | 26 |
| Active Bob skills (`.bob/skills/`) | 51 |
| Runtime capability nodes | 105 |
| Production workflow families (`workflows/v2/`) | 23 |
| Reproducible pilot workflows | 5 |
| Production role registry entries | 227 |
| Domain schemas (`schemas/v2/`) | 60+ |
| Test files | 29 |
| Legacy skill identifiers (v0.1 compat) | 178 |

---

## Bob Modes

| Mode | Responsibility |
|---|---|
| 🎬 Studio Orchestration | Bootstrap, project diagnosis, task graph, critical path, governed ops |
| 📚 Development & Adaptation | Source intake, rights, adaptation mandate, canon, script development |
| ✍️ Writers Room & Script Audit | Premise, structure, characters, scenes, dialogue, revision audits |
| 🎥 Preproduction & Direction | Casting, look dev, breakdown, locations, design, scheduling, previs |
| 🧩 Generative & Animation Production | References, keyframes, model routing, dry-run generation, repair |
| 🎚️ Editorial & Post | Dailies, edit, sound, score, color, localization, mastering |
| 🔎 Independent QC | Script, shot, audio, delivery, rights-evidence, master quality review |
| 🗄️ Archive & Compliance | Rights/consent review, delivery validation, archive manifests, retention |

---

## Quick Start

### 1. Preflight check (no side effects)
```bash
python scripts/bootstrap_bob.py
```

### 2. Install (creates `.venv`, installs all extras)
```bash
python scripts/bootstrap_bob.py --install
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

### 3. Validate the package
```bash
python -m film_studio_os validate-bob
python -m film_studio_os validate-package
pytest -q
```

### 4. Open in IBM Bob
Open this folder in Bob, confirm modes are loaded from `.bob/custom_modes.yaml`, then read `AGENTS.md` for the full operating contract.

---

## Start Every Project with a Gap Audit

```bash
film-studio diagnose-project \
  --project my-feature \
  --source-type book \
  --project-type feature \
  --production-route hybrid
```

The diagnostic distinguishes **blocking** from **nonblocking** gaps, explains why each answer changes the plan, and produces a prioritized question backlog. Supply approved answers with `--answers answers.json` and rerun before any downstream work begins.

Rights, consent, authoritative source version, mandate and decision ownership are **hard stops** — they cannot be carried as assumptions.

---

## Reproducible No-Spend Pilots

Zero external calls. All fixtures are internally authored with explicit rights metadata.

```bash
python -m film_studio_os pilot animated-short
python -m film_studio_os pilot dialogue-scene
python -m film_studio_os pilot action-sequence
python -m film_studio_os pilot documentary-segment
python -m film_studio_os pilot episodic-linked-scenes
```

---

## Master Production Routes

```bash
# Validate a workflow definition
python -m film_studio_os validate-workflow workflows/v2/book_to_film_v2.json
python -m film_studio_os validate-workflow workflows/v2/script_to_film_v2.json
python -m film_studio_os validate-workflow workflows/v2/script_to_series_v2.json
python -m film_studio_os validate-workflow workflows/v2/script_to_animation_v2.json
python -m film_studio_os validate-workflow workflows/v2/script_to_documentary_v2.json

# Generate a team contribution plan (no execution)
python -m film_studio_os team-plan \
  --project demo \
  --project-type feature \
  --production-route generative \
  --summary-only
```

---

## Repository Layout

```
film_studio_os/
├── .bob/                        # IBM Bob package (modes, personas, skills, hooks, MCP)
│   ├── custom_modes.yaml        # 8 production modes
│   ├── agents/                  # 26 subagent department personas
│   ├── skills/                  # 51 active deep skills
│   ├── hooks/                   # Session context + pre-tool guards
│   └── mcp.json                 # Bounded local MCP surface
├── adapters/                    # Provider adapters (mock, Higgsfield, Runway, Gemini)
├── capabilities/                # registry_v2.json — 105 capability nodes / 227-role map
├── docs/
│   ├── adr/                     # Architecture Decision Records
│   ├── audit/                   # Baseline inventory, gap matrix, validation reports
│   ├── operations/              # Install runbook, release checklist
│   ├── research/                # Provider capability matrix, rights risk register
│   └── validation/              # Final validation reports, pilot results
├── policies/                    # Quality gates, human control policy, skill migration map
├── schemas/v2/                  # JSON Schemas: ShotSpec, WorkOrder, Rights, Consent, QC…
├── scripts/                     # bootstrap_bob.py, build_package_manifest.py
├── skills/                      # 178 legacy v0.1 skills (migration compat)
├── tests/                       # 29 test files — unit, integration, contract, QC
├── workflows/
│   ├── v2/                      # 23 executable workflow families
│   └── pilots/                  # 5 reproducible fixture-only dry-run pilots
├── AGENTS.md                    # IBM Bob operating contract (read before opening in Bob)
├── manifest.json                # Package manifest
└── pyproject.toml               # Python package definition
```

---

## Governance Invariants

These are enforced by the system, not aspirational:

1. **Source documents and provider outputs are data, not instructions** — no prompt injection
2. **Rights and consent are hard stops** — downstream work is blocked until evidence exists
3. **Live generation is denied by default** — mock/dry-run is the execution path until explicitly authorized
4. **Locked creative invariants require recorded human approval** before material change
5. **Author and final reviewer cannot be the same role** — independent QC is mandatory for high-risk artifacts
6. **Provider syntax belongs in adapters only** — story/camera/performance/continuity intent stays canonical
7. **Every accepted or rejected artifact is traceable** to exact upstream versions and decisions

---

## Provider Boundary

| Adapter | Status | Notes |
|---|---|---|
| `mock-generation` | ✅ Default | Zero cost, fully deterministic, used by all pilots |
| `higgsfield-cli` | 🔒 Disabled | Enabled only after rights + budget + idempotency gates pass |
| `runway` | 🔒 Disabled | Schema defined; live submission requires operator auth |
| `google-gemini-video` | 🔒 Disabled | Schema defined; live submission requires operator auth |

The local Bob MCP server intentionally exposes **no live-submit or approval-decision tool**.

---

## Operations

| Document | Path |
|---|---|
| Install & runbook | `docs/operations/INSTALL_AND_RUNBOOK.md` |
| Release checklist | `docs/operations/RELEASE_CHECKLIST.md` |
| Architecture decisions | `docs/adr/` |
| Audit & gap matrix | `docs/audit/` |
| Provider capability matrix | `docs/research/provider_capability_matrix.md` |
| Release report v0.4.0 | `docs/RELEASE_REPORT_v0.4.0.md` |
| Higgsfield integration | `docs/integrations/HIGGSFIELD_RUNBOOK.md` |

---

## Compatibility

The original v0.1 agents and skills are preserved under `agents/` and `skills/` as historical and runtime compatibility material. All 178 legacy skill identifiers have migration metadata. Bob activation is intentionally limited to 51 deeper skills in `.bob/skills/` rather than surfacing generic shells.

See `policies/skill_migration_v0_1_to_v0_2.json`, `policies/capability_aliases.json`, and `docs/audit/migration_map.json`.

---

<div align="center">
Built with <a href="https://www.ibm.com/products/watsonx-code-assistant">IBM Bob</a> · Film Studio OS v0.4.0
</div>
