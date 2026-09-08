# ADR 0004 — Hard blockers are not weighted scores

**Decision:** Rights/consent/required approvals/required evidence and critical structural failures are hard blockers. They cannot be offset by a high average creative score.

**Implementation:** `GateResultV2` rejects `passed=true` when blocker findings exist; `evaluate_layered_gate` separately reports blockers and weighted preferences; rights gates validate typed evidence before downstream execution.
