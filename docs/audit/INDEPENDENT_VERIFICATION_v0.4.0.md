# Independent Verification — v0.4.0 Expansion

Verification was performed by reopening each changed control boundary after implementation and rerunning focused plus repository-wide checks.

## HIGH-01 — ✅ Verified Fixed: fresh-clone bootstrap

Evidence from `AGENTS.md`:

```markdown
3. Run the side-effect-free check:
   python scripts/bootstrap_bob.py
4. If core dependencies are missing ... obtain the user's permission before running:
   python scripts/bootstrap_bob.py --install
```

Evidence from `scripts/bootstrap_bob.py`:

```python
if not all(modules[n] for n in CORE):
    actions.append("Run: python scripts/bootstrap_bob.py --install")
if args.install:
    return install(root)
report=readiness(root)
```

Verdict: the default path is read-only, reports exact missing modules/tools and does not create `.venv`; installation is a separate explicit action. The focused regression passed.

## HIGH-02 — ✅ Verified Fixed: first-project gap diagnostic

Evidence from `film_studio_os/project_diagnostic.py`:

```python
if _answered(answers.get(req.key)):
    resolved.append(...)
else:
    gaps.append({"key": req.key, "blocking": req.blocking,
                 "question": req.question, "why_it_matters": req.why})
```

Evidence from `workflows/v2/book_to_film_v2.json`:

```json
{
  "id": "diagnose",
  "capability_id": "production_readiness_diagnostic",
  "depends_on": ["ingest"],
  "handler": "project_diagnostic"
}
```

Verdict: the catalog never fills an unanswered requirement, separates blockers from ordinary gaps, and is the immediate post-ingest dependency in all five master routes. CLI, MCP and workflow handler tests passed.

## HIGH-03 — ✅ Verified Fixed: lifecycle domains were not executable

Evidence from `capabilities/registry_v2.json`:

```json
{
  "capability_id": "character_reference_package",
  "bob_skill": "character-visual-development",
  "handlers": ["artifact"],
  "output_types": ["CharacterReferencePackage"]
}
```

Evidence from `.bob/skills/production-safety-coordination/SKILL.md`:

```markdown
1. Inspect the locked script, breakdown, locations, effects, vehicles, animals,
   performers, equipment and production route for hazard signals while treating
   absence of detail as unknown, not safe.
```

Verdict: 12 new skills have unique substantive procedures, runtime aliases, missing-input behavior, output/failure/recovery contracts, examples and human handoffs. All 24 capabilities are reachable from five valid DAGs. Repository validation reports 51 skills, 105 capabilities and 28 workflow files with zero referential errors.

## MEDIUM-01 — ✅ Verified Fixed: coverage counts and onboarding copy

Evidence from `README.md`:

```markdown
- IBM Bob project package: 8 modes, 26 least-privilege department personas,
  51 deep active skills ...
- 105 registered runtime capabilities used by 23 v2 workflow families plus
  5 reproducible pilot workflows.
```

Verdict: README, AGENTS, release/audit documents, tests and session-start text agree on the v0.4.0 inventory. Legacy aliases remain explicitly non-activating.

## Nearby regression review

- Bob validator: 8 modes, 26 personas, 51 skills, zero errors.
- Repository validator: 105 capabilities, 28 workflows, 178 step references, zero errors.
- Every master route and all five new lifecycle workflows parse as acyclic v2 definitions.
- MCP remains local/read-dry-run and still excludes provider submission and approval decisions.
- Five existing pilots remain complete with zero external cost.
- Offline compatibility harness: 478 passed, 0 failed.

No changed area weakens the existing rights, independent-review, provider authorization, provenance or human-approval boundaries.
