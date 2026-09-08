# Objective Use-Case, Feature and User-Story Audit — v0.4.0

**Audit date:** 2026-08-15  
**Baseline compared:** v0.3.0 master package  
**Evidence rule:** A name in the 227-role registry or a legacy alias is not counted as feature coverage. “Satisfied” requires a Bob skill with substantive instructions and failure behavior, a registered runtime capability, and an executable or explicitly human-gated workflow path.

## Rating scale

| Status | Meaning |
|---|---|
| Satisfied — local | The package can complete and validate the story locally with no paid/external action. |
| Satisfied — controlled | Bob prepares a complete decision/work package, but an accountable human or licensed specialist must decide or execute. |
| Partial | Useful coverage exists, but an important system integration, acceptance benchmark or recovery path is still absent. |
| External dependency | Completion depends on current third-party service access, licensed professionals or production facts the repository cannot provide. |
| Not covered | No substantive, reachable implementation exists. |

## Executive result

The v0.3.0 package was strong from licensed-source intake through dry-run generation, post, QC and archive, but it overstated breadth if the 227-role registry and 178 legacy skill aliases were treated as executable expertise. Twelve lifecycle areas were named but did not have deep active skills and runtime-backed workflow coverage. v0.4.0 closes those gaps with 12 substantive Bob skills, 24 registered capabilities, five workflow families, a first-run bootstrap and a deterministic project diagnostic.

The resulting package has **51 active skills, 105 registered capabilities, 23 v2 workflow families, five pilots, 26 Bob personas and 227 dispositioned production roles**. It is an enterprise production-orchestration foundation, not an autonomous studio: hiring, rights/legal opinions, physical safety, union/guild interpretation, public submissions, spending and release authority remain human/external.

## Use-case and user-story matrix

| Lifecycle | User story | v0.3 evidence/status | v0.4 evidence/status | Objective limitation |
|---|---|---|---|---|
| Bob onboarding | As a new operator, I can open a fresh clone and know what mode, skills, packages and validation steps are required. | **Not covered** — `AGENTS.md` listed validators but no install/discovery/recovery contract. | **Satisfied — local** — `AGENTS.md`; `scripts/bootstrap_bob.py`; session-start hint. | Actual Bob UI discovery remains an installed-IDE smoke test. |
| Bob skill discovery | As an operator, I can verify project skills rather than assuming they loaded. | **Partial** — project layout existed. | **Satisfied — controlled** — bootstrap checks the files/counts; AGENTS requires Advanced/Skill mode plus Skills Settings verification. | Repository code cannot inspect Bob's UI state. |
| New-project diagnosis | As a producer, I receive “what is missing, why it matters, and what must I answer?” before development. | **Not covered** as a deterministic artifact. | **Satisfied — local** — `project-intake-diagnostic`, `diagnose-project`, MCP `diagnose_production_project`, `development_diagnostic_v2`. | Completeness score measures declared inputs, not project quality or greenlight readiness. |
| Source ingestion | As a librarian, I can safely fingerprint and parse common source formats. | **Satisfied — local**. | **Satisfied — local** — unchanged, now a mandatory predecessor to diagnosis. | PDF requires optional dependency; OCR is not claimed. |
| Rights/consent triage | As a rights owner, I can see blockers before adaptation or AI processing. | **Satisfied — controlled**. | **Satisfied — controlled** — diagnostic adds earlier questions; rights gate still fails closed. | Legal clearance and contract interpretation remain human. |
| Book to film | As a producer, I can move a licensed book through adaptation, screenplay, production and release gates. | **Satisfied — controlled**, but intake could jump directly to rights. | **Satisfied — controlled** — master route now inserts diagnosis immediately after ingestion. | Actual rights evidence, creative approvals and live production remain external. |
| Script to feature | As a producer, I can audit/revise a script and orchestrate a film route. | **Satisfied — controlled**. | **Satisfied — controlled** — initial mandate/version/gap audit now precedes script audit. | Creative quality still needs human evaluation and real audience/production testing. |
| Script to series | As a showrunner, I can build a bible, season/episode engine and continuity controls. | **Satisfied — controlled**. | **Satisfied — controlled** — initial series-engine, episode and ownership questions are now explicit. | Writers-room labor, guild terms and commissioned delivery are external. |
| Script to animation | As an animation team, I can build world/character canon, boards, strategy, assets and generation plans. | **Satisfied — controlled**. | **Satisfied — controlled** — diagnostic asks technique/reuse questions; character-reference workflow expands identity testing. | DCC/renderer/asset-management integrations are not implemented. |
| Documentary | As an editorial team, I can map evidence, claims, fact-checks, ethics and release gates. | **Satisfied — controlled**. | **Satisfied — controlled** — diagnostic adds access, thesis, consent and editorial-ethics questions before evidence work. | Field access, participant welfare, counsel and independent verification remain human/external. |
| Script editing | As a writer/editor, I can receive deduplicated evidence-backed notes and controlled revisions. | **Satisfied — local/controlled**. | **Satisfied — local/controlled** — unchanged deep skill and independent review. | A simulated note is not guild-covered human authorship or a market guarantee. |
| Team simulation | As a producer, I can see how all production roles contribute and which require humans. | **Satisfied — local** — 227 roles across 18 departments. | **Satisfied — local** — unchanged; new skills turn 12 previously broad areas into executable work packages. | Role disposition is planning, not employment or staffing. |
| Casting | As a casting team, I can create role briefs, sides, accessible audition plans and evidence-based rubrics. | **Partial** — casting roles were dispositioned, but no deep active casting skill/workflow. | **Satisfied — controlled** — `casting-performance-development`; `casting_character_lookdev_v2`. | Humans control outreach, audition access, bias/legal review, deals and hiring. |
| Character reference | As a visual team, I can create testable identity, turnaround, expression, pose, scale and state references. | **Partial** — character bible/reference binding existed, but not a full multi-view profile. | **Satisfied — controlled** — `character-visual-development`; reference package and acceptance capabilities. | Image generation quality/provider behavior requires project tests and cleared references. |
| Costume/hair/makeup | As appearance teams, I can map looks, changes, duplicates, fittings and continuity to scenes. | **Partial** — legacy aliases and general continuity only. | **Satisfied — controlled** — `costume-hair-makeup`; look and appearance-continuity capabilities. | Fittings, allergies, prosthetics, dignity and performer-facing practice require qualified humans. |
| Location scouting | As a locations team, I can compare creative and logistical fit, tech-scout needs, permits and backups. | **Partial** — geography/location aliases, no substantive scout contract. | **Satisfied — controlled** — `location-scouting-logistics`; scout/feasibility capabilities. | Remote research never proves access, condition, permit or safety; in-person scouts remain mandatory. |
| Script breakdown | As production, I can extract scene elements with page/scene provenance. | **Partial** — feasibility audit and broad role coverage. | **Satisfied — controlled** — `script-breakdown-scheduling`; element-breakdown capability. | Human departments confirm implied elements and labor rules. |
| Scheduling/budget | As a line producer, I can compare transparent schedule and budget scenarios. | **Partial** — work-order budgets/critical path existed, not physical production scenarios. | **Satisfied — controlled** — schedule/budget scenario capability and physical-preproduction workflow. | It does not replace Movie Magic, payroll, current rates or an approved budget. |
| Production design | As the art department, I can turn world canon into sets, props, graphics and build/procurement handoffs. | **Partial** — world bible and production-designer persona existed. | **Satisfied — controlled** — `production-design-art-department`; design and execution capabilities. | Engineering, construction, rigging, fire and electrical approval remain qualified-human work. |
| Physical production | As production management, I can draft day plans, call-sheet data, change logs and daily reports. | **Partial** — team plan did not execute shoot-day operations. | **Satisfied — controlled** — `physical-production-operations`; `production_day_v2`. | Bob does not command a set, distribute personal data without authorization or issue emergency orders. |
| Safety coordination | As a producer, I can identify hazards and route them to the right specialists with stop conditions. | **Partial** — safety roles were marked human-required, but no deep handoff artifact. | **Satisfied — controlled** — `production-safety-coordination`; risk register and human safety gate. | Bob never declares work safe; jurisdiction-specific professionals and authorities decide. |
| Production sound | As sound/editorial, I can plan capture, timecode, metadata, room tone, wild lines and dailies QC. | **Partial** — post sound existed; location capture did not. | **Satisfied — controlled** — `production-sound-capture`; sound plan and capture-QC capabilities. | RF/equipment operation and set decisions remain with production sound professionals. |
| Direction/previs | As a director, I can derive performance, blocking, coverage, camera and boards from locked scenes. | **Satisfied — controlled**. | **Satisfied — controlled** — unchanged and now receives richer cast/look/location/design inputs. | Physical feasibility still needs tech scouts/tests. |
| Generative shot production | As a generative supervisor, I can compile provider-neutral shots, references and QC. | **Satisfied — local dry-run**. | **Satisfied — local dry-run** — unchanged. | No claim of deterministic provider output or live authorization. |
| Higgsfield | As a studio, I can discover current capability shape, compile PromptSpecV3, preflight cost and safely dry-run commands. | **Satisfied — controlled dry-run**. | **Satisfied — controlled dry-run** — bootstrap now clarifies optional installation and forbids auth/submission during setup. | Live, paid UAT requires a studio account, current CLI and explicit approval. |
| Editorial/post | As post, I can plan assembly, pickups, VFX, mix, score, grade, lock and master QC. | **Satisfied — controlled**. | **Satisfied — controlled** — unchanged. | No direct NLE/DAW/color/VFX application integration. |
| Localization/accessibility | As delivery, I can prepare localization, accessibility, validation and archive packages. | **Satisfied — controlled**. | **Satisfied — controlled** — unchanged and linked to distribution planning. | Native-speaker, accessibility and distributor review remain human/external. |
| Business affairs | As business affairs, I can track chain of title, package status, deal documents and jurisdiction questions. | **Partial** — rights registry only. | **Satisfied — controlled** — `business-affairs-packaging`; business-affairs checklist. | No legal/tax/labor advice, negotiation or contract signature. |
| Finance packaging | As a producer, I can compare sources/uses, cash-flow and greenlight dependencies without confusing assumptions with commitments. | **Partial** — per-work-order cost controls only. | **Satisfied — controlled** — production-finance package capability. | No banking, accounting, incentive or completion-bond integration. |
| Marketing/distribution | As a release team, I can form evidence-labeled audience, asset, festival, window and delivery scenarios. | **Partial** — delivery/archive but no market strategy. | **Satisfied — controlled** — `marketing-distribution-strategy`; release-business workflow. | Current festival/platform rules, public submissions, outreach and spend remain human/external. |
| Provenance/archive | As a studio, I can reproduce accepted artifacts and see exact upstream versions/decisions. | **Satisfied — local**. | **Satisfied — local** — unchanged; new diagnostic and lifecycle artifacts use the same provenance boundary. | External DCC/NLE assets need connector-specific manifests. |
| Multi-user enterprise operations | As a large studio, I can use SSO/RBAC, separate projects/tenants and audit human identities centrally. | **Partial** — logical role/approval checks and local SQLite only. | **Partial** — unchanged. | Enterprise identity, tenancy, secrets and system-of-record connectors require deployment architecture. |
| Objective creative benchmark | As an executive, I can compare output quality against approved human baselines and audience goals. | **Partial** — five fixtures validate mechanics, not market quality. | **Partial** — unchanged. | A studio-approved evaluation set and human score panels are still needed. |

## Findings and remediation

### HIGH-01 · Fresh-clone Bob setup was not executable [FIXED]
**Location:** `AGENTS.md`; `scripts/bootstrap_bob.py`  
**Root cause:** v0.3 documented validation commands but not skill-mode discovery, dependency installation, optional-tool boundaries or recovery.  
**Fix:** Added a side-effect-free readiness check, explicit permissioned installer, skill/mode verification and setup-failure contract.  
**Regression evidence:** `test_bootstrap_default_is_read_only_and_reports_actions`.

### HIGH-02 · New sources could enter development without a consolidated gap audit [FIXED]
**Location:** `film_studio_os/project_diagnostic.py`; five master workflows  
**Root cause:** Existing skills diagnosed their own departments, but no deterministic upstream artifact synthesized missing decisions and prioritized questions.  
**Fix:** Added CLI/MCP/workflow diagnostic and inserted it immediately after ingestion in every master route.  
**Regression evidence:** `test_empty_book_hybrid_diagnostic_prioritizes_real_blockers`; `test_all_master_routes_run_diagnostic_immediately_after_ingest`.

### HIGH-03 · Twelve lifecycle domains were labels, not deep executable skills [FIXED]
**Location:** `.bob/skills/`; `capabilities/registry_v2.json`; five new workflow files  
**Root cause:** The 227-role registry and legacy aliases dispositioned responsibilities but did not supply domain procedures, output contracts, failure behavior and reachable capabilities.  
**Fix:** Added 12 substantive skills, 24 capabilities and five workflow families with independent reviewers and reserved human authority.  
**Regression evidence:** skill-contract suite, repository referential-integrity validator and `test_expanded_lifecycle_workflows_and_capabilities_are_reachable`.

### MEDIUM-01 · Counts and onboarding copy could misstate active coverage [FIXED]
**Location:** `README.md`; Bob session-start hook; validation reports  
**Root cause:** v0.3 counts and route descriptions did not distinguish legacy labels from active deep skills.  
**Fix:** Versioned counts and explicitly documented the role-registry versus executable-skill boundary.

## Remaining open limitations

1. **Must resolve before a live enterprise deployment:** SSO/RBAC/tenancy, managed secrets, centralized audit storage, backups/retention and deployment threat model.
2. **Must resolve before physical production reliance:** select jurisdictions/unions, licensed specialist roster, call-sheet/payroll/scheduling systems of record and current local safety/permit sources.
3. **Must resolve before live Higgsfield production:** studio-authorized low-cap UAT against the then-current CLI/schema, account policy, data-processing terms and cost controls.
4. **Should resolve during beta:** build a studio-owned creative benchmark spanning adaptation fidelity, script quality, character consistency, editability, audience promise and reviewer agreement.
5. **Post-beta/integration roadmap:** NLE/DAW/DCC/asset-management, casting database, location/GIS, budgeting, rights-management, festival/submission and distributor delivery connectors.

## Recommended expansion sequence

1. Enterprise identity, tenant isolation, secrets and audit storage.
2. Studio-owned creative/technical evaluation set and acceptance dashboards.
3. Scheduling/budget/call-sheet and rights-management systems of record.
4. Casting/location/art-department connector adapters with read-only discovery first.
5. NLE/DCC/post connectors with immutable asset and color/metadata contracts.
6. One jurisdiction/union pack at a time, maintained by qualified counsel/production experts.

## Release conclusion

**Go With Conditions** for a governed, dry-run production beta. No unresolved Critical or High repository defect is known in the expanded scope, and the lifecycle additions validate structurally and through regression tests. It is **not** a Go for unattended live-provider, legal, hiring, physical-safety or public-release authority.
