# Rights, Governance, Labor, Privacy & Security Risk Register

| Risk | Detection / control in v0.2 | Human-only decision | Residual gap | Priority |
|---|---|---|---|---|
| Missing source/adaptation rights | strict `RightsRecord`; cleared state requires evidence + approver; `rights_gate` fails closed | legal/authorized rights approval | jurisdiction/project-specific analysis | P0 |
| Digital replica / voice / likeness | `ConsentRecord` requires intended use + evidence for approved replica/voice/likeness scope | performer/authorized representative/legal approval | agreement-specific compensation/revocation workflows | P0 |
| Unauthorized paid provider action | mock-only default; live side effects require explicit adapter authorization; MCP exposes no live submit | budget/production authorization | live adapters not yet implemented | P0 |
| Prompt injection from source documents | ingestion flags injection patterns and treats documents as data, not instructions | override/quarantine decision | richer malware scanning/sandboxing | P0 |
| Archive traversal / malicious ZIP | safe member-path and uncompressed-size validation | exception approval | antivirus/content-disarm integration | P0 |
| Secret leakage | repository validator scans config plus secret-pattern helper; no committed tokens | secret rotation | full secret-scanning CI integration | P0 |
| Cross-project access | project-root scoping, cross-project artifact dependency/manifest rejection, project-role authorization for approvals | enterprise RBAC assignment | tenant/SSO/RBAC not implemented | P1 |
| Tampered provenance/approval | immutable artifact hashes + append-only event history conventions | release approval | SQLite is local, not tamper-evident enterprise storage | P1 |
| Guild/union obligations | evidence register documents WGA/SAG-AFTRA AI concerns; consent/training fields preserve needed facts | counsel/labor relations | automatic applicability determination intentionally prohibited | P0 |
| C2PA disclosure | extension point documented | release/disclosure policy | C2PA signing not implemented | P2 |

The system triages evidence and blocks missing required state; it never declares legal clearance.
