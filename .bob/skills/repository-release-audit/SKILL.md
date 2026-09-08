---
name: repository-release-audit
description: Audit the Film Studio OS repository through discovery, classified findings, gated remediation, verification and release triage.
---

# Repository Release Audit

## When to use
Use for architecture discovery, source-backed technical audits, beta readiness reviews, controlled remediation or release certification of this package.

## Procedure
1. Inventory paths and manifests before opening implementation files; identify frontend, runtime/API, storage, authentication, integrations, tests, build, deployment and documentation layers.
2. Read the README and architecture documents, then execute every applicable item in `references/audit-checklist.md`, citing actual source locations and reproducible evidence.
3. Classify each unique root cause with the required severity labels. Stop and obtain an explicit product decision whenever code alone cannot determine intended behavior.
4. For approved remediation, state the root cause and file list, make the smallest safe change, add regression coverage and mark the finding fixed without refactoring unrelated code.
5. Re-open original locations with an independent-auditor mindset, apply `references/verification-checklist.md`, quote source evidence and record a verification verdict for every fixed finding.
6. Run all configured validation, execute `references/user-journey-checklist.md`, triage remaining beta risks and populate every section of `references/release-report-template.md` before recommending Go, Go With Conditions or No-Go.

## Required behavior
- Never speculate when source or command evidence is available; preserve evidence provenance.
- Report skipped checks and missing infrastructure explicitly.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
