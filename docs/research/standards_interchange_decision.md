# Standards & Interchange Decision

## Implemented now
- Strict Pydantic v2 domain models plus generated JSON Schema 2020-12 for public interchange.
- SHA-256 content hashes for immutable artifact versions and reproduction manifests.
- UTF-8 text/Markdown/Fountain/SRT/VTT/CSV, DOCX, EPUB and FDX source normalization; PDF is optional through `pypdf`.

## Selected extension points, not yet claimed as implemented
- **OpenTimelineIO** for editorial cut/timeline interchange because it is an API and interchange format specifically for editorial information.
- **C2PA 2.4 Content Credentials** for signed external provenance/export. v0.2's hashes and event ledger are internal provenance, not C2PA credentials.
- **OpenColorIO/ACES-aware integration** for deterministic color-management/finishing once test media fixtures and transforms are added.
- OpenUSD, IMF/DCP and deeper AAF/OMF/FCPXML paths remain later integrations subject to real use cases and fixtures.

Principle: implement only a standard that can be validated in the current repository; otherwise expose a typed extension point and state the gap.
