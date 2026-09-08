# Source → Output Coverage

Coverage states reflect v0.2 dry-run/runtime support. Generated media delivery formats are not claimed live.

| Source type | Ingestion | Workflow families | Dry-run outputs | Status |
|---|---|---|---|---|
| plain_text_or_markdown | implemented | intake_rights_v2, adaptation_v2, story_script_v2 | CreativeBrief, AdaptationMandate, ScreenplayDraft, ShotSpecSet, ArchiveManifest | tested |
| fountain | implemented | intake_rights_v2, story_script_v2, direction_previs_v2 | LockedScript, DirectorBreakdown, ShotSpecSet | tested |
| fdx | implemented | intake_rights_v2, story_script_v2 | ScriptAudit, RevisionPlan, LockedScript | tested |
| docx | implemented | intake_rights_v2, adaptation_v2, documentary_v2 | SourceMap, EvidenceLedger, AdaptationMandate | tested |
| epub | implemented | intake_rights_v2, adaptation_v2 | SourceMap, AdaptationDecisionLedger | tested |
| pdf | optional_pypdf | intake_rights_v2, adaptation_v2, documentary_v2 | SourceMap, EvidenceLedger | optional_dependency_tested_with_parser_contract |
| srt_or_vtt | implemented | documentary_v2, localization_archive_v2 | EvidenceLedger, LocalizationPackage | tested_parser; alignment/media integration partial |
| csv_research | implemented | documentary_v2 | EvidenceLedger, ClaimMap, FactCheckReport | tested_parser; semantic fact checking requires review |
| image_reference | metadata/path only | art_animation_v2, shot_production_v2 | ReferenceBinding, KeyframePlan | workflow modeled; image inspection adapter future |
| existing_video_or_audio | deterministic_media_probe_and_extraction | documentary_v2, post_finish_v2 | probe/checksum/frame/audio extraction, basic technical QC | local tool implemented/tested; semantic alignment and full delivery QC partial |
