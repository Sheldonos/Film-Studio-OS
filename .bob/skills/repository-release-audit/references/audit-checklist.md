# Technical Audit Checklist

## Architecture and contracts
- Inventory entry points, manifests, package manager, commands, schemas, workflows, state and external boundaries.
- Verify each documented layer and command against source; flag misleading legacy files.
- Check cross-layer references among Bob modes, personas, skills, capabilities, handlers and workflows.

## Security, privacy and authority
- Trace untrusted input, path containment, command construction, secret handling and log redaction.
- Verify rights, consent, human approval, independent review and paid/external action gates fail closed.
- Test direct-provider commands as well as wrapper commands; ensure no shell interpolation.

## Data, state and recovery
- Check strict validation, version lineage, idempotency, retries, timeouts, resume, stale propagation and append-only evidence.
- Confirm rejected outputs cannot be released and budget totals cannot exceed approved limits.

## Product workflows
- Trace book-to-film and script-to-feature/series/animation/documentary routes end to end.
- Verify role/team contributions, revision collaboration, department handoffs, generation, post, localization, archive and release.
- Confirm provider-specific workflows query live schema and cost before authorized submission.

## Quality and operations
- Inspect independent reviewer boundaries, objective metrics, QC gates, reproduction manifests and release packaging.
- Run unit, integration, smoke, type, lint and build commands where configured; report every skip.

## Required finding fields
Use exactly: severity label, source location, reproducible steps, exact root cause, smallest safe fix and effort. Merge symptoms sharing one root cause.
