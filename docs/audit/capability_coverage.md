# Capability / Use-Case Coverage

`workflows/v2/` contains executable repository-owned workflow families for intake/rights, adaptation, story/script, episodic, documentary, art/animation, direction/previs, shot production, post/finish, and localization/archive. These definitions are not claimed to be a public IBM Bob custom-workflow format. Bob reaches the runtime through project modes, skills, CLI and optional MCP.

The five pilot workflows under `workflows/pilots/` deliberately use internally-authored fixture text and `mock-generation`; they exercise rights, independent review, mock generation, QC artifact creation, approval and archive without third-party production assets or paid calls.

Coverage status categories:
- **Executable core:** workflow state, dependency readiness, review/approval pause, retry budgets, artifact lineage, stale propagation, mock job lifecycle, archive manifest.
- **Structured path:** adaptation/story/episodic/documentary/animation/post/localization workflow graphs and Bob skills exist but many craft decisions are still model/persona-executed rather than deterministic code.
- **Future integration:** real provider jobs, OTIO, C2PA signing, OCIO/ACES transforms, DCC/NLE/project-system adapters, full black/frozen-frame/subtitle/HDR technical QC, enterprise SSO/RBAC. Local ffprobe/ffmpeg probing, checksums, extraction, basic delivery checks, timecode and loudness/true-peak measurement are implemented and tested.
