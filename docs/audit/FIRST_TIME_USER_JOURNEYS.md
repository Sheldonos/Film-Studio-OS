# First-Time User Journey Audit — v0.3.0

### Install and validate Bob package
**Status:** ✅ Complete  
**Issue:** Wheel builds and local validators provide actionable counts. The standard pytest command requires the declared dev extra and must run in release CI.  
**Severity:** Low

### Ingest a book and begin adaptation
**Status:** ✅ Complete  
**Issue:** The route ingests, independently reviews, stops at rights approval, creates an adaptation mandate and carries lineage into screenplay, team, shots, mock production and release gate. Missing rights fail closed.  
**Severity:** None

### Revise a screenplay with team contributions
**Status:** ✅ Complete  
**Issue:** The script-to-film route includes independent audit/revision and a deterministic 227-role plan. Required humans are blockers rather than simulated approvals.  
**Severity:** None

### Convert scripts to series, animation or documentary
**Status:** ✅ Complete  
**Issue:** Each validated route preserves format-specific controls: series bible/episode continuity, animation world/assets/boards, or documentary evidence/fact/ethics. Final creative/release actions pause for humans.  
**Severity:** None

### Generate a complete production-role plan
**Status:** ✅ Complete  
**Issue:** CLI and MCP return all 227 roles exactly once with responsibilities, owners, applicability, provenance and blockers. The `dry_run_only` state is truthful when assignments are missing.  
**Severity:** None

### Run no-spend production pilots
**Status:** ✅ Complete  
**Issue:** Five pilots complete with mock generation, independent reviewer identities, persistent metrics/events and reproduction manifests. Success messages report real completion and zero external spend.  
**Severity:** None

### Prepare a Higgsfield job
**Status:** ✅ Complete  
**Issue:** The runbook leads from live discovery to 15-section request and dry-run hash. The example produces the correct positional CLI command without contacting Higgsfield.  
**Severity:** None

### Submit and monitor a live Higgsfield job
**Status:** ⚠️ Incomplete  
**Issue:** Code includes schema, cost, request approval and polling controls, but live UAT was not authorized in this environment. Errors are fail-closed; recovery is documented.  
**Severity:** Medium

### Finish, localize, archive and reproduce
**Status:** ✅ Complete  
**Issue:** Existing v2 post/finish/localization/archive workflows and pilot reproduction manifests provide a complete dry-run path. Commercial mastering remains a human release responsibility.  
**Severity:** None

## Trust-breaking UX review

No core dry-run flow falsely claims payment, external generation, rights clearance, staffing or human approval. The remaining trust risk is operational: a studio could skip the dev-extra pytest run or live provider UAT. The release report makes both conditions visible.
