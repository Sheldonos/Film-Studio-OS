# Research Source Register

Access date: **2026-08-15**

This register records only research that materially affected the v0.2 implementation. Legal/labor entries are evidence for risk controls, not legal clearance.

## IBM-BOB-SKILLS — Skills
- Organization: IBM Bob
- URL: https://bob.ibm.com/docs/ide/features/skills
- Authority: primary / official product documentation
- Classification: verified
- Implementation implication: Created 36 curated Bob skills with activation-quality frontmatter and bounded supporting contracts; legacy catalog skills are non-activating.
- Uncertainty: The Skills page still contains an older statement that skills are only available in Advanced mode while the current changelog says default modes were simplified; package does not rely on that statement.

## IBM-BOB-PERSONAS — Agent personas
- Organization: IBM Bob
- URL: https://bob.ibm.com/docs/ide/configuration/agent-personas
- Authority: primary / official product documentation
- Classification: verified
- Implementation implication: Separated main task modes from 26 durable subagent personas; reviewers default to read-only tools.
- Uncertainty: Actual subagent execution is performed by IBM Bob, not by the repository's Python workflow engine.

## IBM-BOB-MODES — Custom modes
- Organization: IBM Bob
- URL: https://bob.ibm.com/docs/ide/configuration/custom-modes
- Authority: primary / official product documentation
- Classification: verified
- Implementation implication: Created eight whole-task production modes; independent QC receives no edit or execute group.
- Uncertainty: Repository workflows are intentionally not represented as an invented Bob custom-workflow package format.

## IBM-BOB-HOOKS — Lifecycle hooks
- Organization: IBM Bob
- URL: https://bob.ibm.com/docs/ide/configuration/lifecycle-hooks
- Authority: primary / official product documentation
- Classification: verified
- Implementation implication: Added narrow SessionStart and PreToolUse guard hooks only; no provider credentials or network actions are embedded.
- Uncertainty: Hook enforcement behavior depends on the installed Bob release; validator checks structure but cannot launch Bob in this environment.

## IBM-BOB-MCP — Using MCP in Bob
- Organization: IBM Bob
- URL: https://bob.ibm.com/docs/ide/configuration/mcp/mcp-in-bob
- Authority: primary / official product documentation
- Classification: verified
- Implementation implication: Added a local project MCP example that exposes bounded dry-run/read operations and contains no committed secrets.
- Uncertainty: The optional Python mcp package is not required for core CLI tests and may need installation in a Bob workspace.

## IBM-BOB-CHANGELOG — Changelog
- Organization: IBM Bob
- URL: https://bob.ibm.com/docs/ide/changelog
- Authority: primary / official product changelog
- Classification: verified
- Implementation implication: Avoided assuming legacy Advanced/Orchestrator semantics; package uses project modes and repository-owned runtime workflows.
- Uncertainty: Changelog page intermixes multiple releases; exact installed Bob build remains an environment check.

## OTIO — OpenTimelineIO documentation
- Organization: Academy Software Foundation / OpenTimelineIO
- URL: https://opentimelineio.readthedocs.io/en/latest/
- Authority: primary / official open-source documentation
- Classification: verified
- Implementation implication: Selected OTIO as the intended editorial interchange extension point; v0.2 does not claim an OTIO adapter until contract tests exist.
- Uncertainty: Not implemented in v0.2; remains P2 integration work.

## C2PA-2.4 — C2PA Specifications 2.4
- Organization: Coalition for Content Provenance and Authenticity
- URL: https://spec.c2pa.org/specifications/specifications/2.4/index.html
- Authority: primary / technical standard
- Classification: verified
- Implementation implication: v0.2 uses deterministic hashes and reproduction manifests now, with an explicit C2PA export/signing extension point rather than falsely claiming C2PA compliance.
- Uncertainty: No signing/validation implementation ships in v0.2.

## OCIO — OpenColorIO
- Organization: Academy Software Foundation / OpenColorIO
- URL: https://opencolorio.org/
- Authority: primary / official open-source documentation
- Classification: verified
- Implementation implication: Color metadata is represented as an extension boundary; actual OCIO/ACES transforms are deferred until media fixtures and deterministic technical QC are added.
- Uncertainty: No OCIO transform is executed in v0.2.

## USCO-AI — Copyright and Artificial Intelligence
- Organization: U.S. Copyright Office
- URL: https://www.copyright.gov/ai/
- Authority: primary / government report hub
- Classification: verified
- Implementation implication: Rights and consent are separate typed records; the software never declares legal clearance and escalates human/legal decisions.
- Uncertainty: Project-specific copyrightability and rights scope require counsel; software only records evidence and blockers.

## WGA-2026 — Summary of the 2026 WGA MBA
- Organization: Writers Guild of America
- URL: https://www.wga.org/contracts/contracts/mba/summary-of-the-2026-wga-mba
- Authority: primary / guild contract summary
- Classification: verified
- Implementation implication: Rights records include AI-processing/training distinctions and provenance; labor obligations remain human/legal review items.
- Uncertainty: The package does not determine whether a production is covered by the MBA.

## SAG-AFTRA-2026 — 2026 TV/Theatrical AI protections
- Organization: SAG-AFTRA
- URL: https://www.sagaftra.org/sag-aftra-members-approve-2026-tvtheatrical-contracts-tentative-agreement
- Authority: primary / guild announcement/explainer
- Classification: verified
- Implementation implication: ConsentRecord explicitly separates voice clone, likeness and digital-replica scope and requires evidence/intended use before approval.
- Uncertainty: The package does not interpret a collective bargaining agreement for a specific production.

## RUNWAY-API-2026 — API Changelog & Updates
- Organization: Runway
- URL: https://docs.dev.runwayml.com/api-details/api_changelog/
- Authority: primary / official provider API documentation
- Classification: verified
- Implementation implication: Provider capabilities are dated manifests and adapter-owned; model IDs are never embedded in story/shot domain logic.
- Uncertainty: Privacy, retention, regional terms and per-account limits must be checked at authorization time; no Runway adapter is enabled in v0.2.

## GOOGLE-VIDEO-2026 — Video generation in the Gemini API
- Organization: Google AI for Developers
- URL: https://ai.google.dev/gemini-api/docs/video
- Authority: primary / official provider API documentation
- Classification: verified
- Implementation implication: Capability-based routing must query dated features rather than assume a single best model.
- Uncertainty: No Google adapter is enabled in v0.2; availability and model identifiers must be reverified before live use.

## HIGGSFIELD-MCP-2026 — How to connect Higgsfield to Claude via MCP
- Organization: Higgsfield
- URL: https://higgsfield.ai/creator-hub/help-center/mcp-cli/how-do-i-connect-higgsfield-to-claude
- Authority: primary / official provider help center
- Classification: verified
- Implementation implication: Retained Higgsfield only as a replaceable boundary and did not auto-connect or execute paid MCP calls; project MCP server is local and provider-neutral.
- Uncertainty: Higgsfield account terms, privacy, retention and per-model policy must be verified before authorized integration.

