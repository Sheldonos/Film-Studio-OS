# ADR 0001 — IBM Bob interaction boundary

**Decision:** Use `.bob/custom_modes.yaml` for main-task operating postures, `.bob/agents/` for spawned subagent personas, and `.bob/skills/` for focused activation units. Keep film workflows in the repository-owned typed runtime and expose them through CLI/MCP/skills.

**Evidence:** Current Bob documentation distinguishes modes (main task), personas (subagents), and skills (reusable activation units). Public documentation documents a `workflow` tool group and nested workflows but does not provide enough evidence here to invent a third-party workflow package schema.

**Migration:** 178 legacy skill IDs remain in `policies/capability_aliases.json`; 51 deep skills activate in Bob, including diagnostic, production-lifecycle, role coverage, Higgsfield integration and release audit. Top-level legacy agents remain compatibility/reference artifacts while `.bob/agents` is authoritative for Bob personas.
