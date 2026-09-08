# Provider Capability Matrix — 2026-08-15

The runtime enables only `mock-generation`. Runway, Google video, and Higgsfield are **research-only** entries; their policy fields deliberately remain `unknown` where this audit did not verify them. A live adapter must fail policy-sensitive routing on unknown privacy/training/retention/commercial-use constraints rather than infer them. See `provider_capability_matrix.json` for machine-readable status.

Provider research changed the architecture by making capability manifests dated and adapter-owned. Rapid model churn in the official Runway changelog and Google's 2026 video deprecations make stable domain-level vendor/model IDs unsafe.
