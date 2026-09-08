# Independent Verification — v0.3.0

Each fixed finding was re-opened at its original control boundary after remediation.

## High-01 — ✅ Verified Fixed

Evidence from `.bob/hooks/pre_tool_guard.py:11-17`:

```python
side_effect_patterns = (
    r"\bfilm-studio\b[^\n]*(?:provider-submit|--live)\b",
    r"\b(?:higgsfield|higgs|hf)\b\s+generate\s+(?:create|workflow)\b",
    r"\b(?:higgsfield|higgs|hf)\b\s+(?:upload|soul-id\s+create)\b",
)
if is_external_action and os.environ.get("FILM_STUDIO_EXTERNAL_AUTHORIZED") != "1":
```

Focused regression proves direct create/workflow and wrapper submit return code 2; model-list discovery returns 0; the explicit environment boundary returns 0 and leaves approval/cost validation to the adapter.

## High-02 — ✅ Verified Fixed

Evidence from `film_studio_os/adapters/higgsfield.py:68-77,113-121`:

```python
argv=[self.binary,'generate','create',compiled_request['job_set_type'],'--prompt',compiled_request['prompt']]
if not self.live_enabled or not authorized:
    raise AuthorizationRequired(...)
self.discover_model_schema(compiled_request['job_set_type'])
estimate=self.cost_preflight(compiled_request)
self._validate_approval(approval, ...)
payload=self.runner(command)
```

The fake-provider regression confirms positional job-set syntax, schema-before-cost-before-create order, a $3.25 preflight under a $4 cap, and rejection without a matching approval. `shell=False` is present at line 32.

## High-03 — ✅ Verified Fixed

Evidence from `workflows/v2/book_to_film_v2.json:17-28,53-61,75-97`:

```json
{"id":"rights","handler":"rights_gate","approval_required":true,"approval_role":"human_rights_owner"}
{"id":"team","capability_id":"production_role_coverage","handler":"team_plan"}
{"id":"generate","capability_id":"video_generation_plan","handler":"mock_generation"}
```

All five master route files and the corrected compatibility `workflows/script_to_film.json` load as v2 acyclic DAGs. Package validation resolves every capability, skill, owner, reviewer and handler reference.

## High-04 — ✅ Verified Fixed

Evidence from `film_studio_os/team_simulation.py:98-108`:

```python
ids=[x['role_id'] for x in contributions]
if len(contributions)!=227 or len(ids)!=len(set(ids)):
    raise AssertionError('team plan failed exact role-coverage invariant')
return {'role_count':len(contributions), 'coverage_complete':..., 'human_blockers':blockers, ...}
```

Regression output contains 227 unique roles across 18 departments. Animation activates its specialty roles while documentary-only roles are explicitly not applicable. Required-human authority remains visible and blocks production readiness.

## Medium-05 — ✅ Verified Fixed

Evidence from `film_studio_os/pilots.py:43-59`:

```python
review_rounds=0; total_executed_steps=0
while True:
    result=ex.run(...)
    total_executed_steps += int(result.get('executed_steps',0))
...
result['executed_steps']=total_executed_steps
```

All five pilots now return cumulative counts (12–13 execution/review transitions), seven completed work orders, independent-review events and seven-artifact final lineage.

## Low-06 — ✅ Verified Fixed

The active audit skill contains `audit-checklist.md`, `verification-checklist.md`, `user-journey-checklist.md`, `release-report-template.md` and `example-invocations.md`. Bob validation reports 39 complete skills and the skill-contract tests confirm triggers, failures, recovery, provenance and independent review.

## False Positive-07 — 🔵 False Positive

`test_adapter_contract_v2.py` imports pytest inside the only function that uses it. The other two cited files have no `pytest.` call. No source change was made.

## Known External Dependency-08 — 🔗 Known Dependency

The adapter and dry-run boundary are source-verified. Live provider acceptance, billing and output behavior remain blocked by missing authorized account state and must be verified in studio UAT.
