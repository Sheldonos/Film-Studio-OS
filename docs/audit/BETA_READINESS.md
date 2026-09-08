# Beta Readiness Triage — v0.3.0

## Must Fix Before Beta

None. All source-confirmed Critical/High issues are fixed, the production wheel builds, contract validation passes and no-spend core journeys complete.

## Should Fix During Beta

1. **Run standard pytest in connected release CI** — User impact: maintainers need conventional test-runner evidence. Effort: 1 hour. Technical risk: low. Dependency: install `.[dev]`. Mitigation: the offline audit harness ran 384 cases with 0 failures, but is not represented as pytest.
2. **Run authorized Higgsfield UAT** — User impact: studios using Higgsfield need account-specific schema, billing, job and output evidence. Effort: 4 hours. Technical risk: medium. Dependencies: studio-owned fixture, legal/security/provider account approval and a low cost cap. Mitigation: live disabled by default; mock and dry-run paths are complete.
3. **Add CI lint/static typing policy** — User impact: maintainers lack automatic style/type regression gates. Effort: 6–10 hours. Technical risk: low. Dependency: tool selection and baseline configuration.

## Post-Beta

1. Hosted collaboration/UI, SSO and centralized secrets are outside this local IBM Bob package; add only if the studio chooses a managed deployment.
2. Add provider-specific cancellation when Higgsfield documents a supported cancellation command.
3. Expand authorized provider benchmarks across the studio's approved model/job-set portfolio; never freeze undocumented flags.

## False Positive

- Suspected missing pytest imports in three test files was disproved by source inspection.

## External Dependency

- Live Higgsfield authentication, terms, prices, schemas and service outputs.

## Recommended fix sequence

1. Install dev dependencies in release CI and run `pytest -q`.
2. Obtain approved low-cap Higgsfield UAT request and record schema/cost/job/QC evidence.
3. Tag the beta candidate.
4. Add lint/type policy during beta without delaying the governed dry-run package.
