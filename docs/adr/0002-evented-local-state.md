# ADR 0002 — Auditable local state first

**Decision:** Use SQLite WAL behind `StateStore` for v0.2 work orders, events, immutable artifact metadata, dependencies, approvals, provider jobs and metrics.

**Why:** It gives restart-safe local dry runs, transactional persistence and an explicit interface without requiring cloud credentials.

**Tradeoff:** Local SQLite is not enterprise multi-tenant storage or tamper-evident archival infrastructure. The interface must be replaced/extended for enterprise concurrency, SSO/RBAC and durable object storage.
