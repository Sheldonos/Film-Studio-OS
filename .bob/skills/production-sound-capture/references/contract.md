# Contract — production-sound-capture

## Runtime capability aliases
- `production_sound_plan`
- `sound_capture_qc`

## Authoritative inputs
- Versioned source and upstream artifacts required by the procedure.
- Locked creative invariants plus relevant rights, consent and approval records.
- Applicable budget, schedule, jurisdiction, provider-policy, safety and quality constraints.

## Missing-input behavior
Fail closed for missing rights, consent, required human approval, authoritative version, locked-invariant context or a decision that would make the output misleading. Record ordinary optional omissions and continue only when the result remains valid.

## Output contract
Return structured, versioned results with `schema_version`, project/artifact identifiers, exact upstream version IDs, decisions/findings, evidence versus assumption labels, confidence where uncertain, provenance, downstream consumers, acceptance state and escalation owner.

## Failure taxonomy
- `missing_authoritative_input`
- `stale_or_conflicting_input`
- `rights_or_consent_block`
- `locked_invariant_conflict`
- `human_authority_boundary`
- `schema_or_quality_failure`
- `safety_or_jurisdiction_escalation`
- `budget_schedule_or_provider_block`

## Recovery
Repair locally when evidence supports it, preserve the superseded version, rerun only invalidated descendants and route consequential uncertainty to the accountable human. Never turn an unresolved dependency into an invented fact.

## Positive trigger example
Use this skill when the user or work order explicitly requests: Plan dialogue, ambience, playback, timecode, microphone and sound-report workflows for physical or hybrid production.

## Negative trigger example
Do not activate it merely because the project is audiovisual; do not bypass the responsible department, independent reviewer, specialist or human approval gate.

## Skill-specific decision rules
- Bob prepares options and QC evidence; the production mixer and qualified crew control equipment, RF and on-set capture.
- Music playback, recorded voices and location recordings require applicable rights and consent.
- A waveform's presence does not prove intelligibility, sync, phase, channel mapping or editorial usability.

## Skill-specific output shape
- scene sound map
- capture strategy and equipment assumptions
- location noise/RF register
- metadata and sound-report contract
- dailies sound QC and pickup list

## Skill-specific quality checks
- Every dialogue scene has capture and contingency notes.
- Metadata/timecode handoff matches editorial.
- Noise and wardrobe/camera conflicts have owners.

## Handoff
sound_supervisor and production sound leadership for execution, director for performance/playback decisions, editor for sync/pickups, costume for mic interaction and production_librarian for media lineage.

## Example
A moving two-camera dialogue scene gets boom/radio options, wardrobe flags, traffic windows, timecode and track naming, room-tone/wild-line needs and a dailies reconciliation checklist.

## Counterexample
Bob says the camera microphone is sufficient, ignores playback rights and timecode, and marks clips approved because audio tracks exist.

