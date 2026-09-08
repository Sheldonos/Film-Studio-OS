from pathlib import Path
import json, subprocess, sys

from film_studio_os.mcp_server import tool_manifest
from film_studio_os.project_diagnostic import diagnose_project
from film_studio_os.state import StateStore
from film_studio_os.workflow import load_workflow, WorkflowDefinition, StepDefinition, WorkflowExecutor

ROOT=Path(__file__).resolve().parents[1]


def test_empty_book_hybrid_diagnostic_prioritizes_real_blockers():
    out=diagnose_project("novel-1","book","feature","hybrid",{})
    keys=[x["key"] for x in out["blocking_gaps"]]
    assert keys[:4]==["project_mandate","format_runtime","rights_status","decision_owners"]
    assert {"source_edition","adaptation_scope","physical_digital_boundary","digital_replica_consent","safety_scope"} <= set(keys)
    assert out["readiness_score"]==0
    assert "not a greenlight" in out["score_interpretation"]
    assert "rights clearance" in out["human_authority_required"]
    assert out["recommended_workflow"]=="development_diagnostic_v2"


def test_answered_requirements_disappear_without_inference():
    answers={"project_mandate":"Preserve the sister relationship","format_runtime":"100-minute feature","rights_status":{"option":"verified"},"decision_owners":["producer"],"draft_version":"2026-08-15 blue","revision_mandate":"diagnosis only"}
    out=diagnose_project("script-1","script","feature","physical",answers)
    open_keys={x["key"] for x in out["blocking_gaps"]+out["nonblocking_gaps"]}
    assert not set(answers) & open_keys
    assert "locked_elements" in open_keys
    assert out["readiness_score"]>0
    assert out["provenance"]["method"]=="deterministic_requirement_catalog"


def test_documentary_and_generative_routes_ask_domain_questions():
    out=diagnose_project("doc-1","research","documentary","generative",{})
    keys={x["key"] for x in out["blocking_gaps"]+out["nonblocking_gaps"]}
    assert {"evidence_ledger","documentary_thesis","access_and_consent","provider_policy","likeness_voice_consent"} <= keys
    assert "documentary-evidence-ethics" in out["recommended_skills"]
    assert "higgsfield-production-bridge" in out["recommended_skills"]


def test_undecided_route_is_a_blocker_not_an_invented_default():
    out=diagnose_project("p","script","feature","undecided",{})
    assert "production_route_decision" in {x["key"] for x in out["blocking_gaps"]}


def test_invalid_diagnostic_enums_fail_closed():
    import pytest
    with pytest.raises(ValueError): diagnose_project("p","novel","feature","hybrid",{})
    with pytest.raises(ValueError): diagnose_project("p","book","short","hybrid",{})
    with pytest.raises(ValueError): diagnose_project("p","book","feature","magic",{})


def test_all_master_routes_run_diagnostic_immediately_after_ingest():
    names=["book_to_film_v2","script_to_film_v2","script_to_series_v2","script_to_animation_v2","script_to_documentary_v2"]
    for name in names:
        wf=load_workflow(ROOT/"workflows/v2"/f"{name}.json")
        step=wf.step_map()["diagnose"]
        assert step.capability_id=="production_readiness_diagnostic"
        assert step.handler=="project_diagnostic"
        assert step.depends_on==("ingest",)
        children=[x for x in wf.steps if "diagnose" in x.depends_on]
        assert children


def test_workflow_diagnostic_infers_only_route_proven_facts(tmp_path):
    wf=WorkflowDefinition("book_to_film_v2","2.0.0","",(
        StepDefinition("diagnose","production_readiness_diagnostic","studio_orchestrator",handler="project_diagnostic"),
    ))
    store=StateStore(tmp_path/"state.db")
    result=WorkflowExecutor(store).run("book-1",wf)
    version_id=result["work_orders"][0]["output_version_ids"][0]
    report=store.get_artifact(version_id)["content"]
    assert report["source_type"]=="book" and report["project_type"]=="feature"
    assert report["production_route"]=="undecided"
    assert "production_route_decision" in {x["key"] for x in report["blocking_gaps"]}


def test_expanded_lifecycle_workflows_and_capabilities_are_reachable():
    registry=json.loads((ROOT/"capabilities/registry_v2.json").read_text())
    ids={x["capability_id"] for x in registry["capabilities"]}
    expected={
        "production_readiness_diagnostic","script_element_breakdown","casting_breakdown",
        "character_reference_package","costume_look_plan","location_scout_matrix",
        "production_design_package","production_operations_plan","production_risk_register",
        "production_sound_plan","business_affairs_checklist","audience_release_strategy",
    }
    assert expected <= ids
    for name in ["development_diagnostic_v2","casting_character_lookdev_v2","physical_preproduction_v2","production_day_v2","release_business_v2"]:
        assert load_workflow(ROOT/"workflows/v2"/f"{name}.json").topological_order()


def test_bootstrap_default_is_read_only_and_reports_actions():
    env=ROOT/".venv"; existed=env.exists()
    proc=subprocess.run([sys.executable,str(ROOT/"scripts/bootstrap_bob.py"),"--check","--root",str(ROOT)],text=True,capture_output=True)
    assert proc.returncode in {0,2}
    report=json.loads(proc.stdout)
    assert report["bob"]=={"skills":51,"workflows":28}
    assert set(report["repository_files"])=={"AGENTS.md","pyproject.toml",".bob/settings.json",".bob/custom_modes.yaml","capabilities/registry_v2.json"}
    assert env.exists()==existed


def test_mcp_manifest_exposes_diagnostic_but_not_live_submission():
    manifest=tool_manifest()
    assert "diagnose_production_project" in manifest["tools"]
    assert manifest["live_provider_submission_exposed"] is False
