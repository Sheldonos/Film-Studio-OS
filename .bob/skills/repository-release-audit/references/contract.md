# Contract — repository-release-audit

## Runtime capability aliases
- `repository_release_audit`

## Authoritative inputs
- Repository tree, README, architecture documents, manifests, source, tests and command output.
- Audit, verification, journey and release-report references in this skill directory.
- Confirmed product decisions and current working-tree scope.

## Missing-input behavior
Fail closed when the repository or required source is inaccessible, a product decision remains unresolved, or destructive remediation lacks authorization. Record missing tools as explicit validation skips.

## Output contract
Return an architecture map, uniquely rooted classified findings, decision record, remediation ledger, source-evidenced verification, explicit validation results, journey audit, beta triage and populated release report.

## Failure taxonomy
- `repository_unavailable`
- `required_evidence_missing`
- `duplicate_finding`
- `product_decision_pending`
- `validation_failure`
- `verification_incomplete`
- `journey_blocker`
- `release_no_go`

## Recovery
Acquire the missing evidence or decision, reopen the cited source, apply the smallest authorized correction and rerun the affected validation from a clean mental model. Independent verification cannot be replaced by the implementer's assertion.

## Positive trigger example
Use this skill to assess a candidate master package, fix source-confirmed high-severity issues, verify each change and determine beta readiness.

## Negative trigger example
Do not use it to declare a release safe after reading only documentation or after skipping a failing build without reporting it.

## Skill-specific decision rules
- One finding represents one root cause even when several user-facing symptoms share it.
- Product Decision Required findings block remediation until explicit confirmation; external constraints remain Known External Dependency.
- Any unresolved Critical issue, failing build or must-fix blocker produces No-Go.

## Skill-specific output shape
- Architecture Map
- Classified finding and decision ledger
- Remediation and independent-verification evidence
- Validation command matrix and journey results
- Beta triage, release sequence and final release report

## Skill-specific quality checks
- Every finding cites code and concrete reproduction steps.
- Every fixed finding includes a source excerpt and verification verdict.
- Skips, limitations and open risks remain visible in the release recommendation.

## Handoff
studio_orchestrator and human release owner; security_data_governance or qc_supervisor for independent specialist review.

## Example
The audit inventories the Python/Bob package, proves a provider-command guard bypass, fixes it with a regression test, reopens the hook, runs all configured checks and conditions release on provider credentials.

## Counterexample
The report says “all tests pass” even though the test runner was unavailable and no substitute validation or skip explanation appears.
