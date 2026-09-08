---
name: archive-reproduction
description: Create immutable archive and reproduction manifests that trace final
  artifacts to exact sources, versions, decisions, attempts, QC and approvals.
---

# Archive Reproduction

## When to use
Create immutable archive and reproduction manifests that trace final artifacts to exact sources, versions, decisions, attempts, QC and approvals.

## Procedure
1. Freeze the released/candidate artifact ID and collect its full dependency ancestry, version genealogy, source hashes, decisions, prompts/specs, adapters/tools/models/parameters, attempts, QC, approvals and cost events.
2. Verify every manifest reference resolves and every file/artifact hash matches stored metadata; missing lineage is a release/archive finding.
3. Include rejected attempts and repair decisions when needed to explain why the selected result was accepted; do not archive only the “happy path.”
4. Create reproduction instructions that distinguish deterministic steps from external model calls that may not reproduce bit-for-bit.
5. Record environment/tool/compiler/schema versions and unresolved proprietary/provider dependencies.
6. Package checksums and retention/deletion constraints; do not copy secrets into the archive.

## Required behavior
- Preserve approved creative intent and exact upstream version lineage.
- Separate verified evidence, inference and unknowns.
- Never let authoring stand in for independent final review.
- Never initiate a paid/external action without explicit authorization.

## Contract, examples, failures, recovery and handoff
Read `references/contract.md` before execution.
