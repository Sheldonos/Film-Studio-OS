# Skill Catalog

Implemented reusable skill definitions: **178**.

## archive_memory
- `asset_registration` — Assign stable IDs, hashes, type, ownership, version and dependency metadata to all production assets.
- `provenance_capture` — Record inputs, model/provider, parameters, references, agent, time, decisions and output hashes for each artifact.
- `prompt_versioning` — Version compiled prompts and preserve field-level provenance back to structured source specs.
- `generation_logging` — Record every generation attempt, cost, duration, result, rejection reason and selected status.
- `decision_logging` — Record proposals, reviewer findings, decision owner, chosen option and rejected alternatives.
- `lineage_reconstruction` — Answer how a final artifact was produced from exact upstream versions and decisions.
- `rejection_learning_ingest` — Convert rejected generations into failure patterns and future routing/prompt/shot-design lessons.
- `archive_packaging` — Create immutable project archive with manifests, masters, source artifacts and logs.
- `reproduction_manifest` — Emit exact recipe for regenerating an internally produced artifact where provider determinism permits.

## art_world
- `character_bible_creation` — Define canonical identity, want/need, contradictions, relationships, behavior, voice, wardrobe and reference requirements.
- `identity_state_separation` — Separate durable identity attributes from scene-specific mutable state.
- `voice_fingerprint_design` — Define diction, syntax, cadence, register, metaphor habits, evasions, status tactics and disallowed generic phrasing.
- `behavior_gesture_design` — Define repeatable physical behavior and pressure responses that can be directed visually.
- `wardrobe_canon` — Define canonical wardrobe sets and state changes with continuity identifiers.
- `expression_range_map` — Define recognizably character-specific emotional expressions and performance boundaries.
- `relationship_state_tracking` — Track trust, leverage, intimacy, resentment, debt and status changes scene by scene.
- `character_reference_plan` — Specify front/profile/three-quarter/body/emotion/lighting coverage required for generation consistency.
- `world_bible_creation` — Define world rules, history, social logic, visual principles and persistent environment facts.
- `location_bible_creation` — Create canonical geography, architecture, materials, lighting baselines, entrances and anchor views.
- `environment_state_design` — Model time, weather, damage, occupancy, atmosphere and evolving scene state.
- `prop_canon_design` — Define important prop appearance, function, ownership and state transitions.
- `costume_state_design` — Track outfit versions, condition, dirt/wetness/damage and scene continuity.
- `era_technology_consistency` — Validate signage, devices, vehicles, interfaces, materials and behavior against world period.
- `visual_motif_design` — Encode recurring shapes, materials, colors, objects and environmental themes with story purpose.
- `location_geography_map` — Represent rooms/streets/paths and screen-direction relationships for continuity and coverage.

## camera_lighting_previs
- `camera_language_design` — Define shot-size, lens, height, movement, stability, framing and visual-rhythm rules by story state.
- `shot_size_selection` — Choose shot size from information, intimacy, power, geography and performance needs.
- `lens_strategy` — Choose focal-length family and perspective behavior consistent with visual intent.
- `composition_design` — Specify subject placement, balance, leading lines, negative space and visual hierarchy.
- `camera_height_distance` — Use camera height/distance to shape status, intimacy, distortion and spatial read.
- `camera_motion_design` — Use static/pan/track/handheld/zoom/crane/orbit only when motivated by subject, reveal or emotion.
- `lighting_design` — Specify motivated key/fill/back, contrast, direction, quality, color temperature and practical sources.
- `depth_foreground_background` — Create layers, parallax, occlusion and environmental information.
- `screen_direction_axis_control` — Manage 180-degree axis, eyelines, entrances/exits and motion vectors for edit continuity.
- `shot_spec_compilation` — Compile narrative, performance, camera, art, continuity, audio and generation requirements into a provider-neutral spec.
- `storyboard_plan` — Translate shot specs into board frames emphasizing geography, pose, composition and transitions.
- `coverage_visualization` — Visualize how coverage cuts together and where reactions/inserts are missing.
- `shot_family_grouping` — Group shots sharing setup, location, character state or generation strategy to reduce drift/cost.
- `animatic_timing` — Estimate shot durations, reaction holds and sequence rhythm before generation.
- `transition_previs` — Design match cuts, action cuts, sound bridges, entrances/exits and continuity masks.
- `generation_risk_previs` — Identify hands, crowds, contact, fast motion, reflections, text, complex props and multi-character interaction risk before generation.

## continuity_state
- `continuity_extraction` — Extract expected persistent and mutable states from approved script/breakdown artifacts.
- `character_state_tracking` — Track identity, wardrobe, injury, dirt, wetness, emotion, position and action state.
- `prop_state_tracking` — Track possession, hand, position, damage, fill level and visibility of story-relevant objects.
- `wardrobe_state_tracking` — Track outfit version and condition across chronology.
- `geography_continuity` — Validate entrances, exits, room orientation, travel and spatial plausibility.
- `screen_direction_validation` — Check eyelines, camera axis, character look direction and movement vectors between shots.
- `lighting_time_state_tracking` — Track time-of-day, source direction, weather and scene-light continuity.
- `knowledge_state_tracking` — Track what each character knows, believes, hides and learns at every scene.
- `action_state_tracking` — Track continuous physical action so cuts preserve before/after state.
- `continuity_diff` — Compare expected and observed shot states and produce severity-tagged mismatches.

## direction_performance
- `scene_intention_breakdown` — Define what the audience should feel/understand and the dramatic change each beat must produce.
- `performance_objective_design` — Translate psychology into playable objective, tactic, pressure and adjustment.
- `blocking_plan` — Design movement around objective, status, geography and editability.
- `coverage_plan` — Choose masters, singles, reactions, inserts and transitions based on edit/narrative needs.
- `shot_priority_map` — Rank must-have, coverage, optional and pickup shots by narrative value.
- `dialogue_scene_direction` — Design eyelines, reaction strategy, overlap space, coverage and performance continuity for conversation.
- `action_sequence_direction` — Break action into readable objectives, geography, impacts, cause/effect and safe generative units.
- `reaction_shot_design` — Use reactions to control information, emotion, comedy and edit rhythm.
- `pickup_identification` — Identify the minimum new material required to fix clarity, continuity, pace or performance.

## editorial_post
- `dailies_review` — Review all generated takes against story intent, performance, continuity and edit utility.
- `edit_compatibility_scoring` — Score handles, motion vectors, eyelines, action match, entrance/exit and cut points.
- `assembly_edit` — Build a complete scene/sequence assembly before polishing individual moments.
- `scene_pacing_evaluation` — Measure information density, reaction space, shot duration and escalation rhythm.
- `continuity_edit` — Cut around or flag spatial/temporal/appearance discontinuities without hiding story problems.
- `reaction_timing` — Tune reaction duration and placement for emotion, comedy, suspense and dialogue rhythm.
- `transition_selection` — Choose visual/audio transitions based on causal, temporal and tonal function.
- `picture_lock_check` — Verify no unresolved pickups, placeholders, stale shots or unapproved structural changes remain.

## finishing
- `color_normalization` — Normalize heterogeneous generated sources into a stable working baseline.
- `shot_matching` — Match exposure, white balance, contrast, saturation and local color relationships across cuts.
- `look_grade` — Apply the approved visual language without erasing source texture or identity.
- `skin_tone_identity_check` — Ensure grade does not materially change identity or continuity-relevant appearance.
- `sequence_grade_continuity` — Validate look and lighting continuity across a full sequence.
- `delivery_color_check` — Verify color space, levels and export assumptions for target master.
- `visual_qc` — Score image defects, intentionality and cinematic coherence with evidence.
- `motion_physics_qc` — Detect temporal instability, impossible inertia, contact failures, background morphing and camera artifacts.
- `identity_qc` — Validate face/body/wardrobe/voice identity against canonical character state.
- `continuity_qc` — Validate selected media against authoritative continuity state and adjacent shots.
- `composition_lighting_qc` — Evaluate framing hierarchy, depth, exposure, light motivation and shot-purpose fit.
- `edit_qc` — Evaluate cut rhythm, geography, handles, action match, reaction timing and scene momentum.
- `audio_qc` — Evaluate intelligibility, sync, ambience continuity, mix priority and artifacts.
- `master_qc` — Run integrated visual/audio/subtitle/delivery and provenance checks before final approval.
- `benchmark_evaluation` — Run repeatable screenplay, shot and studio-orchestration regression fixtures.
- `failure_classification` — Map a rejected artifact to a normalized defect taxonomy and next-best recovery path.

## generative_vfx
- `reference_selection` — Choose the minimum sufficient canonical references for identity, location, prop, composition and style intent.
- `prompt_compilation` — Compile structured intent into provider-neutral prompt sections without losing source-field provenance.
- `negative_constraint_compilation` — Translate known failure risks and continuity invariants into explicit constraints supported by the target provider.
- `keyframe_generation_plan` — Plan still/keyframe creation before motion when composition/identity certainty is valuable.
- `keyframe_evaluation` — Score composition, identity, world state, continuity and motion-readiness before video spend.
- `model_routing` — Route by shot requirements, measured benchmark strengths, cost, latency, rights and feature support.
- `video_generation_plan` — Choose text-to-video, image-to-video, start/end frame, multi-shot or motion-transfer strategy per ShotSpec.
- `motion_strategy` — Control subject/camera motion complexity, duration and interaction topology to maximize usable output probability.
- `performance_prompting` — Translate objective, tactic, tempo, gaze, gesture and emotional state into playable generation direction.
- `lip_sync_strategy` — Choose native dialogue, post lipsync, ADR or cutaway/reaction strategies according to shot and provider capability.
- `generation_failure_classification` — Classify identity, motion, physics, anatomy, environment, prompt, continuity, audio and composition failures.
- `shot_repair_strategy` — Choose localized edit, extend, inpaint, recast, VFX, regenerate or editorial workaround based on defect topology.
- `upscale_interpolation_plan` — Apply finishing resolution/frame-rate enhancement only after creative acceptance and source-quality checks.
- `vfx_feasibility_triage` — Choose regenerate vs repair vs composite based on defect scope, cost and continuity risk.
- `compositing_plan` — Define layers, mattes, transforms, grain/light integration and merge order.
- `mask_rotoscope_plan` — Plan isolation of subjects/regions across time for targeted repairs.
- `artifact_cleanup` — Remove flicker, morphs, edge chatter, background warping and transient visual defects without changing intent.
- `interaction_repair` — Repair contact/collision/hand-object/multi-character defects locally where possible.
- `background_repair` — Stabilize environment geometry, signage, text and repeating structures.
- `face_hand_repair` — Repair local anatomy/identity defects with continuity safeguards.
- `vfx_review` — Validate repaired frames against source motion, lighting, grain, identity and continuity.

## sound_music
- `dialogue_edit` — Clean, select and align dialogue takes while preserving performance continuity.
- `adr_strategy` — Identify replacement dialogue and choose matching performance/acoustic approach.
- `voice_consistency` — Check timbre, accent/register, pace, emotional state and identity across synthesized/recorded lines.
- `foley_design` — Design sync-specific footsteps, cloth, props and body movement that make generated images feel physical.
- `ambience_design` — Build persistent environmental beds and perspective changes by location/shot.
- `sound_effects_design` — Create event-specific effects with scale, distance, material and story emphasis.
- `sound_motif_design` — Use recurring sonic ideas tied to character, threat, place or theme.
- `sync_validation` — Check dialogue, impact, Foley and environmental timing against picture.
- `mix_plan` — Balance dialogue, effects, ambience and music by narrative priority and dynamic range.
- `loudness_delivery_qc` — Validate final audio against target delivery specs and clipping/phase/channel requirements.
- `score_spotting` — Decide where music enters/exits, where silence is stronger, and what dramatic function each cue serves.
- `motif_design` — Create thematic musical identities that can develop with character/story state.
- `cue_brief` — Translate scene objective, tempo, palette, arc and hit points into a composer/generator-ready brief.
- `music_transition_design` — Plan cue joins, tails, prelaps, source-to-score transitions and editorial flexibility.
- `temp_track_risk_audit` — Prevent overfitting to protected/source-specific music or locking the edit to an unlicensable reference.

## studio_governance
- `creative_constraint_extraction` — Convert a user brief into explicit creative, runtime, audience, legal, schedule, budget and technical constraints.
- `production_strategy_selection` — Choose the workflow profile appropriate to genre, runtime, interaction complexity, dialogue density and risk.
- `task_graph_compilation` — Compile goals into dependency-aware work orders with one accountable owner per leaf operation.
- `critical_path_analysis` — Identify blocked work, parallel-safe branches and the current delivery-critical path.
- `budget_envelope` — Allocate generation, review and repair budgets by scene/shot risk instead of flat quotas.
- `handoff_validation` — Reject incomplete cross-department handoffs before downstream agents invent missing decisions.
- `staleness_propagation` — Mark downstream artifacts stale when a dependency changes and calculate invalidation scope.
- `production_status_report` — Summarize progress, blockers, approvals, cost, quality and next critical work.
- `rights_risk_triage` — Flag possible rights, likeness, trademark, music and source-material risks for human/legal review; never declares legal clearance.
- `greenlight_package` — Compile creative, production, budget, schedule, risk and approval inputs for human greenlight.

## writing_story
- `premise_stress_test` — Test protagonist, goal, opposition, stakes, irony, engine, novelty and feature/short sustainability.
- `dramatic_question_design` — Define the central audience-facing question that organizes pressure and resolution.
- `theme_countertheme_design` — Express thematic argument through competing character choices rather than speeches.
- `genre_contract_definition` — Define audience promises, conventions, novelty allowance and tonal boundaries.
- `audience_promise_mapping` — Track what the opening promises and where each promise is paid off or intentionally subverted.
- `structure_map` — Create act/sequence architecture linked to state changes rather than beat-label mimicry.
- `scene_card_generation` — Specify scene purpose, incoming state, wants, obstacles, tactics, turn, outgoing state and causal handoff.
- `scene_writing` — Convert an approved scene card into visual, playable screenplay pages with late entry, turns and an active exit.
- `revision_plan` — Rank revision work by root cause, severity, blast radius and expected improvement.
- `act_sequence_design` — Design macro dramatic progression and sequence objectives.
- `causal_chain_construction` — Ensure major events arise from prior choices, consequences or established forces.
- `progressive_complication` — Escalate pressure by removing options, increasing cost or changing information/power.
- `midpoint_reversal_design` — Create a meaningful reorientation of goal, information, stakes or power.
- `crisis_climax_design` — Force an irreversible dilemma and climax that pays off the central dramatic engine.
- `setup_payoff_tracking` — Track plants, promises, callbacks, reveals and payoff timing.
- `reveal_ordering` — Control information release for suspense, surprise, anticipation and dramatic irony.
- `suspense_dramatic_irony` — Model who knows what, when, and how that asymmetry creates pressure.
- `subplot_braiding` — Interleave secondary arcs so they pressure or refract the primary story instead of running independently.
- `runtime_budgeting` — Allocate screen time by narrative value and estimate scene runtime from dialogue, action and pauses.
- `scene_necessity_test` — Apply removal, merge, causality and information tests to identify redundant scenes.
- `dialogue_voice_construction` — Write character-specific lines from intention, tactic and voice fingerprint.
- `subtext_writing` — Make spoken language operate differently from literal private intention.
- `exposition_concealment` — Embed required information inside conflict, choice, behavior, misunderstanding or consequence.
- `interruption_overlap_design` — Use interruption, overlap and unfinished thought to model power, familiarity and pace.
- `silence_pause_design` — Use reaction space and silence as active dramatic beats.
- `banter_construction` — Build asymmetric volleys from relationship history, status and tactical play rather than interchangeable jokes.
- `wit_callback_design` — Create setup/turn/button/callback structures tied to character and situation.
- `joke_mechanics` — Diagnose premise, setup, turn, escalation, button and consequence of comic lines.
- `line_compression` — Remove redundant intent, duplicate image information and generic filler without erasing voice.
- `actor_speakability` — Check breath, rhythm, interruption timing, mouthfeel and performance plausibility.
- `dialogue_to_action_substitution` — Replace lines with visible behavior when the image can carry the meaning more powerfully.
- `cold_read_audit` — Record comprehension, engagement, emotional response and confusion before analytical passes.
- `premise_theme_audit` — Check whether draft behavior actually serves the central engine and thematic argument.
- `structure_causality_audit` — Find arbitrary turns, weak act transitions, non-progressive complications and unearned climax logic.
- `character_arc_audit` — Require evidence for psychological/relationship change and validate decision causality.
- `scene_function_audit` — Check objective, conflict, turn, outgoing state, removal test and momentum.
- `dialogue_voice_audit` — Detect equalized voices, on-the-nose intent, exposition dumps, generic AI phrasing and overwritten jokes.
- `continuity_logic_audit` — Check chronology, knowledge, geography, props, motivation and world rules.
- `genre_tone_audit` — Check promised audience experience and tonal boundary violations.
- `production_feasibility_audit` — Identify generative risk, costly interactions and alternate equivalent staging strategies.
- `table_read_simulation` — Test performance speed, pauses, overlap, exposition survival and voice differentiation.
- `revision_regression_audit` — Verify a fix improved its target metric without damaging frozen strengths.
- `imitation_risk_audit` — Flag suspiciously source-specific expression, derivative scene construction or protected-character mimicry.
- `filmable_action_writing` — Write visible/playable action and remove unfilmable interiority.
- `blocking_geography_writing` — Clarify entrances, exits, positions, movement paths and spatial relationships.
- `visual_reveal_writing` — Stage information so discovery occurs through image, action or composition.
- `action_paragraph_rhythm` — Control reading and screen pace with paragraph density, emphasis and white space.
- `screenplay_format_validation` — Validate scene headings, action/dialogue separation and human-readable export conventions.
