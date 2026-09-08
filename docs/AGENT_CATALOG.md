# Agent Catalog

Implemented stateful agents: **18**.

## Executive Producer / Studio Orchestrator (`studio_orchestrator`)
Turn an approved creative mandate into a dependency-aware, budget-aware, reviewable production graph and drive it to delivery without overriding specialist creative authority.
**Owns:** production graph, critical path, work-order lifecycle, budget/attempt envelopes, cross-department scheduling, approval pauses, staleness propagation
**Final escalation:** `human_producer`

## Showrunner / Head Writer (`showrunner`)
Protect the story promise and authorial intent from concept through production script while arbitrating narrative proposals.
**Owns:** premise, theme argument, story engine, screenplay narrative coherence, character/story priorities, script creative invariants
**Final escalation:** `human_showrunner`

## Story Architect (`story_architect`)
Engineer structure, causality, escalation, reveals, setups/payoffs, and scene-to-scene momentum without flattening voice.
**Owns:** structure map, beat architecture, causal graph, setup/payoff ledger, reveal order, runtime allocation
**Final escalation:** `showrunner`

## Script Editor / Independent Narrative Auditor (`script_editor`)
Diagnose screenplay problems through independent multi-pass audits and produce ranked, evidence-backed revision notes without silently rewriting the author.
**Owns:** script audit findings, note deduplication, revision risk map, regression verification
**Final escalation:** `showrunner`

## Director (`director`)
Translate dramatic intention into performance, blocking, coverage, shot priorities, rhythm, and creative decisions that serve the audience experience.
**Owns:** scene intention, performance direction, blocking intent, coverage strategy, shot selection priority, pickup decisions, directorial visual logic
**Final escalation:** `studio_orchestrator`

## Cinematographer (`cinematographer`)
Convert directorial intention into coherent camera, lens, composition, lighting, depth and movement specifications across the film.
**Owns:** camera grammar, lens strategy, lighting logic, composition rules, movement motivation, technical visual continuity
**Final escalation:** `director`

## Production Designer (`production_designer`)
Own the visual world, locations, props, costume logic, environmental storytelling, era and motif consistency.
**Owns:** world bible, location bible, prop canon, costume logic, environment states, visual motifs
**Final escalation:** `director`

## Casting / Character Director (`character_director`)
Maintain stable character identity, appearance, behavior, voice markers and performance range while separating identity from scene state.
**Owns:** character bibles, identity anchors, wardrobe canon, voice fingerprints, behavior/gesture anchors, character state transitions
**Final escalation:** `director`

## Continuity Supervisor (`continuity_supervisor`)
Maintain the authoritative cross-scene state graph and reject contradictions in character, object, geography, action, lighting, knowledge and chronology.
**Owns:** continuity ledger, state inheritance, screen direction state, object/wardrobe/injury states, knowledge state, stale-state detection
**Final escalation:** `director`

## Storyboard / Previsualization Supervisor (`storyboard_previs`)
Convert scene intentions and camera plans into coverage boards, animatic-ready shot families and generation-feasibility previews.
**Owns:** storyboards, coverage boards, previs shot families, transition visualization
**Final escalation:** `director`

## Generative Production Supervisor (`generative_supervisor`)
Route each approved ShotSpec through references, keyframes, model/provider selection, generation, repair and take selection while preserving intent and provenance.
**Owns:** generation strategy, provider/model routing, prompt compilation, reference binding, attempt plan, generation telemetry, take candidate set
**Final escalation:** `studio_orchestrator`

## VFX / Repair Supervisor (`vfx_supervisor`)
Own compositing, cleanup, masking, difficult interaction repair and invisible fixes that preserve continuity and shot intent.
**Owns:** repair plan, compositing decisions, mask/roto plan, artifact cleanup, VFX shot status
**Final escalation:** `director`

## Picture Editor (`editor`)
Construct narrative rhythm and emotional continuity from approved takes, identify missing coverage, and drive picture toward lock.
**Owns:** assembly, rough cut, scene/sequence pacing, cut decisions, pickup list, picture lock candidate
**Final escalation:** `director`

## Supervising Sound Editor / Sound Designer (`sound_supervisor`)
Build the auditory world, dialogue clarity, Foley, ambience, effects, ADR/lipsync strategy and mix requirements around picture intent.
**Owns:** dialogue edit, ADR plan, Foley plan, ambience, sound effects, sound design motifs, mix prep, sync QC
**Final escalation:** `director`

## Composer / Music Supervisor (`composer`)
Design score strategy, thematic motifs, spotting, transitions and music editorial support without masking story problems.
**Owns:** score map, motif map, spotting notes, music cue requirements
**Final escalation:** `director`

## Colorist / Finishing Supervisor (`colorist`)
Normalize and creatively grade approved picture while preserving skin, identity, environment and visual-story continuity.
**Owns:** color pipeline, shot matching, look application, finish consistency
**Final escalation:** `cinematographer`

## Independent QC Supervisor / Film Critic (`qc_supervisor`)
Independently reject weak artifacts and score narrative, visual, continuity, motion, edit, audio and master quality against explicit gates.
**Owns:** QC scores, gate decisions, failure taxonomy, benchmark results
**Final escalation:** `studio_orchestrator`

## Production Librarian / Archivist (`production_librarian`)
Preserve every artifact, version, prompt, reference, decision, attempt, rejection, approval and dependency needed to reproduce or audit the production.
**Owns:** asset registry, provenance ledger, lineage graph, version history, rejection lessons, archival package
**Final escalation:** `studio_orchestrator`
