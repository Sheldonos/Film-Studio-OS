---
name: bob-package-validation
description: Validate Film Studio OS Bob modes, personas, skills, MCP config, hooks
  and references against current project conventions.
---

# Bob Package Validation

## When to use
Validate Film Studio OS Bob modes, personas, skills, MCP config, hooks and references against current project conventions.

## Procedure
1. Validate root AGENTS.md and `.bob/` presence before checking individual components.
2. Parse `.bob/custom_modes.yaml`; enforce unique valid slugs, documented tool groups and read-only boundaries for audit/QC postures.
3. Parse every `.bob/agents/*.md` frontmatter; filename must match name, description must be activation-quality and tool groups must be within Bob-supported persona ceilings.
4. Parse every active `.bob/skills/*/SKILL.md`; folder/name/description must match, referenced supporting files must exist and no legacy shell may masquerade as active.
5. Validate `.bob/settings.json` and `.bob/mcp.json` syntax and scan MCP config for committed secret material; inspect hooks for narrow/static behavior.
6. Report structural conformance separately from actual IDE discovery; only a real installed Bob workspace can prove activation at runtime.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
