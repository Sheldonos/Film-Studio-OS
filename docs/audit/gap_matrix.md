# Requirement / Gap / Action Matrix

| Requirement | Baseline evidence | v0.2 action | Status | Priority |
|---|---|---|---|---|
| Bob project discovery | no `.bob/` | modes, personas, skills, rules, settings/hooks, MCP config + validator | implemented/tested structurally | P0 |
| Deep skill activation | 178 generic shells, no descriptions | 36 curated Bob skills; legacy IDs aliased/non-activating | implemented; behavior depth varies by skill | P1 |
| Executable workflows | JSON disconnected | typed loader + persistent executor + 10 workflow families + 5 pilots | implemented/tested in dry-run | P1 |
| Independent review | reviewer metadata only | author output pauses in `review`; separate decision required before downstream | implemented/tested | P0 |
| Rights/consent blockers | absent/informal | strict records + fail-closed rights gate | implemented/tested | P0 |
| Strict schemas | permissive JSON schemas | Pydantic strict models + generated v2 schemas | implemented/tested | P0 |
| Resume/restart | in-memory/basic | SQLite WAL state + work-order/event persistence | implemented/tested locally | P1 |
| Invalidation | primitive graph | immutable artifact versions + targeted transitive staleness | implemented/tested | P1 |
| Provider lifecycle | thin Higgsfield dry-run | capability adapter interface + idempotent mock submit/poll/cancel; research manifests | mock implemented; live adapters future | P1 |
| Source ingestion | none | safe text/Markdown/Fountain/SRT/VTT/CSV/DOCX/EPUB/FDX; optional PDF | implemented/tested | P1 |
| Documentary/episodic/localization/etc. | absent | typed workflow families and deep skills | orchestration path implemented; real media integration partial | P1/P2 |
| Technical media QC | average scores only | hard-blocker-aware gates + ffprobe/ffmpeg probe/checksum/extraction/basic delivery QC/timecode/loudness | foundational deterministic QC implemented; black/frozen-frame, HDR/color/subtitle conformance remain | P1 |
| Production economics | minimal | budgets, actual cost, attempts, latency, acceptance/rework/staleness metrics + critical path | core measured locally; live provider reconciliation/forecast calibration partial | P1 |
| Enterprise security/RBAC | absent | safe local defaults, project paths, input guards | P0 local controls implemented; enterprise auth future | P1 |
| Editorial/provenance standards | absent | OTIO/C2PA/OCIO selected extension points | not yet integrated | P2 |
