---
name: security-threat-review
description: Review source ingestion, archives, URLs, subprocesses, secrets, project
  isolation, hooks and external-job authorization for P0 threats.
---

# Security Threat Review

## When to use
Review source ingestion, archives, URLs, subprocesses, secrets, project isolation, hooks and external-job authorization for P0 threats.

## Procedure
1. Map trust boundaries: source files/archives, Bob workspace/hooks, MCP, local subprocesses, provider/network endpoints, secrets, project storage and human approvals.
2. Test hostile paths/archives, malformed XML/ZIP, oversized files, prompt-injection text, secret patterns, URL SSRF literals/credentials and cross-project path traversal.
3. Review external side-effect surfaces for explicit authorization, budget, allowlisted typed fields, idempotency and audit logging.
4. Review hooks/MCP for least privilege and remember hooks run with user permissions; keep commands static, fast and deterministic.
5. Scan package for credentials, caches, local DBs and generated media before release.
6. Document residual risks such as DNS rebinding, malware scanning, enterprise RBAC and dependency supply chain rather than claiming controls that do not exist.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
