# Baseline Checkpoint

Reproduced from the preserved v0.1.0 archive before broad modification.

- 419 material files before test-generated caches.
- Manifest: 18 agents, 178 skills, 3 workflows, 12 quality gates.
- Existing test suite: 7 tests passing.
- 178 legacy skill definitions: one shared six-step procedure; 534 declared skill tests with no matching executable suite; empty `handoff_to` arrays.
- No valid project `.bob/` package; legacy SKILL.md files lacked activation descriptions and agent Markdown lacked persona frontmatter.
- Legacy workflow JSON was not executed end-to-end by the Python orchestrator.
- Baseline schemas were permissive and generation integration was a thin Higgsfield dry-run boundary.

Evidence: `baseline_inventory.json` stores path, size and SHA-256 hashes; `migration_map.json` classifies each original artifact before cleanup. The untouched source copy remains outside this work tree.
