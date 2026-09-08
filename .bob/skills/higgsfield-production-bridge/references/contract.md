# Contract — higgsfield-production-bridge

## Runtime capability aliases
- `higgsfield_capability_discovery`
- `prompt_spec_v3_compile`
- `higgsfield_cost_preflight`
- `higgsfield_generation_submit`

## Authoritative inputs
- Approved ShotSpecV2/PromptSpecV3 with exact source version IDs and reference asset IDs.
- Cleared rights/consent records, live model schema, budget cap and provider terms suitable for the project.
- For live submission, a request-bound, unexpired human approval and explicit external authorization.

## Missing-input behavior
Fail closed for missing provenance, live model schema, rights, consent, cost preflight, approval, budget or authorization. Return a dry-run command only when no external side effect is authorized.

## Output contract
Return discovery evidence, canonical and provider request hashes, normalized cost estimate, safe argv command, approval binding, job lifecycle state, result artifact references and provenance.

## Failure taxonomy
- `cli_unavailable_or_unauthenticated`
- `live_schema_unavailable`
- `invalid_provider_parameter`
- `cost_preflight_unavailable`
- `budget_exceeded`
- `authorization_required`
- `approval_request_mismatch`
- `provider_temporary`
- `independent_qc_required`

## Recovery
Refresh CLI/schema state, repair only invalid parameters, re-run cost preflight, obtain a new request-bound approval when the hash or price changes, and resume by external job ID. Never blindly resubmit.

## Positive trigger example
Use this skill to discover the current Higgsfield video schema, compile an approved shot packet, estimate the exact job, and produce a no-side-effect command for producer review.

## Negative trigger example
Do not activate it to paste an unlicensed reference into a paid command, bypass a cost gate, or treat a successful submission as a quality-approved shot.

## Skill-specific decision rules
- The command shape is `higgsfield generate create <job-set-type>`; the job-set type is positional, not a `--model` flag.
- Live schema and cost discovery must use the same job-set type and provider parameter set as submission.
- A changed request hash invalidates prior approval; provider success still requires independent Film Studio QC.

## Skill-specific output shape
- Capability/schema discovery result
- PromptSpecV3 and compiled argv
- Cost preflight and approval binding
- Provider job state and output references
- QC/retry handoff

## Skill-specific quality checks
- No shell execution or secret material in argv/logs.
- Exact request hash, approved cap and normalized preflight cost agree.
- All returned media is registered with upstream prompt, model schema, job ID and rights provenance.

## Handoff
generative_supervisor for operation, line_producer for budget, rights_clearance_supervisor for scope and qc_supervisor for independent acceptance.

## Example
An approved shot compiles to the discovered video job set, receives a $4.20 preflight under a $5 cap, and is submitted only after a matching producer approval expires in one hour.

## Counterexample
The agent runs `higgsfield generate create --model ...` directly from chat without live discovery, a request hash, cost preflight or explicit approval.
