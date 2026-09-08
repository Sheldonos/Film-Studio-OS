# Film Studio OS Architecture

## Design principle

The system is not a swarm of generic agents. It is a versioned production organization:

`creative intent -> structured artifacts -> accountable department -> bounded skill -> quality gate -> handoff -> downstream dependency`

Provider execution is downstream of film logic:

`ShotSpec -> prompt packet -> provider adapter -> generation -> QC -> selected take`

## Accountable personas and production roles

Twenty-six Bob personas retain durable department responsibility and independent review boundaries. The 227-role production registry is a coverage and human-authority matrix, not 227 autonomous agents. Micro-specialties such as banter, lens selection, Foley design, prompt compilation and repository audit are bounded skills, not personalities.

## Reusable skills

Thirty-nine active Bob skills include scope, prerequisites, substantive procedures, failure modes, recovery, quality checks and handoffs. A migration registry preserves the 178 legacy identifiers without activating shallow duplicate skills.

## Runtime and interfaces

- Python CLI and local stdio MCP are the operator interfaces; there is no web frontend or hosted API.
- Strict Pydantic models define provider-neutral intent. SQLite stores projects, work orders, approvals, immutable artifact lineage, metrics and events.
- JSON workflows map registered capabilities to accountable owners, independent reviewers, handlers, budgets, retries and human gates.
- Mock generation is the default executable provider. Higgsfield is an optional disabled-by-default adapter with dynamic schema discovery, cost preflight and request-bound approval.

## Master routes

Book and screenplay sources enter the same governed spine: intake/rights, adaptation or revision, format-specific story controls, complete team contribution planning, shot/prompt specifications, provider boundary, independent QC, post, release and archive. Feature, series, animation and documentary branches keep their distinct continuity, asset, evidence and ethics gates.

## Core state

- CreativeBrief / script lineage
- CharacterBible + CharacterState
- World/Location/Prop/Costume state
- SceneCard / SceneBeat
- ShotSpec
- ProductionWorkOrder
- QCResult
- provenance / decisions / rejections / lessons

## Quality gates

Ten production gates plus greenlight and script lock separate authorship from acceptance. Failing generations never silently enter the film.

## Memory

Every generated or edited artifact should append a provenance event containing upstream versions, prompt packet, provider/model, parameters, references, attempt number, cost, QC and decision status. The archive layer can reconstruct "how did we create this shot?" without relying on human memory.
