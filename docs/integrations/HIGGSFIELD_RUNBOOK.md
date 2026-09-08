# IBM Bob + Higgsfield Runbook

## Safety model

Bob owns film logic, structured artifacts, rights/consent state, approvals, budgets, lineage and independent QC. Higgsfield is an optional execution provider. Provider success means a job was accepted or completed; it never means the shot passed Film Studio QC.

The local MCP surface cannot submit live jobs or decide approvals. Direct Higgsfield creation/upload commands and `film-studio provider-submit` are blocked by the Bob hook unless `FILM_STUDIO_EXTERNAL_AUTHORIZED=1` is present. The adapter then independently requires live schema discovery, cost preflight and a matching unexpired approval.

## Install and discover

```bash
npm install -g @higgsfield/cli
higgsfield login
higgsfield model list --json
higgsfield model get <job-set-type> --json
higgsfield workflow list --json
```

Use the installed CLI's returned schema. Do not copy flags from a different model or freeze a catalog in the repository.

## Prepare the governed request

1. Approve ShotSpecV2 and its reference hierarchy.
2. Compile PromptSpecV3: scene context, active references, location map, first frame/blocking, format mode, cut-by-cut action, optics, camera, action, performance, physics, lighting, audio, style and positive locks.
3. Confirm every local media path or provider UUID is owned/cleared for the intended operation.
4. Copy `examples/higgsfield/request.example.json`, select a live-discovered job-set type and add only parameters returned by its schema.

## Dry run

```bash
film-studio higgsfield-dry-run examples/higgsfield/request.example.json \
  --project PROJECT_ID --idempotency-key SHOT_VERSION_KEY
```

The output contains a canonical `request_hash` and an argv list but does not call Higgsfield. Record that hash in a separate approval file. A modified request produces a new hash and invalidates the old approval.

## Cost and live submission

The live adapter runs these checks in order: model schema discovery, `higgsfield generate cost`, approval binding/cap, then `higgsfield generate create`. Set a short expiry and a cost cap at or above the returned preflight only after a human producer reviews the exact request.

```bash
export FILM_STUDIO_EXTERNAL_AUTHORIZED=1
film-studio provider-submit examples/higgsfield/request.example.json \
  --approval /secure/project/approved-operation.json \
  --project PROJECT_ID --idempotency-key SHOT_VERSION_KEY
```

Never commit approval records, credentials or generated media. The approval must contain `status=approved`, `provider=higgsfield-cli`, `operation=generate.create`, exact project and request hash, `decided_by`, a timezone-aware future `expires_at`, and `max_cost_usd`.

## Monitor, ingest and QC

```bash
higgsfield generate get JOB_ID --json
higgsfield generate wait JOB_ID --json
```

Register results against job ID, PromptSpec version, live model schema and source versions. Then run identity/continuity, motion/physics, composition/lighting, audio/sync, edit compatibility and rights/consent gates. Rejection creates a new repair request and hash; do not overwrite the failed attempt or blindly resubmit.

## Recovery

- Schema/flag error: refresh `model get`, repair only invalid parameters, recompile and reapprove if the hash changes.
- Cost increase: stop and obtain a new cap-bound approval.
- Authentication/provider failure: retain the local work order and resume by job ID; never assume the first call failed before checking.
- Quality failure: classify the failure, preserve the rejected artifact, revise the smallest upstream specification and rerun only invalidated descendants.
- Rights/consent change: revoke pending approvals and block downstream release until clearance is restored.
