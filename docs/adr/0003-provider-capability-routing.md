# ADR 0003 — Provider capability routing

**Decision:** Canonical film intent and `ShotSpec` never contain provider syntax. Adapters compile canonical specs and own authentication, model identifiers, limits, idempotency, async lifecycle, normalized cost and policy metadata.

**Evidence:** Current provider model catalogs and deprecations change quickly; a dated capability manifest is safer than embedding model popularity into story logic.

**v0.2:** only `mock-generation` is implemented/tested. Other provider rows are research-only until contract tests and policy fields are complete.
