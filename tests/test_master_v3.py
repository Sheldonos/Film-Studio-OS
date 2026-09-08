from datetime import datetime, timedelta, timezone
from pathlib import Path
import json, os, subprocess, sys
import pytest

from film_studio_os.adapters import HiggsfieldCLIAdapter, AuthorizationRequired
from film_studio_os.prompt_compiler import compile_prompt_spec_v3, PROMPT_SPEC_V3_HEADINGS
from film_studio_os.team_simulation import build_team_contribution_plan, load_role_registry
from film_studio_os.typed_models import CameraSpec, PerformanceSpec, ShotSpecV2
from film_studio_os.workflow import load_workflow

ROOT=Path(__file__).resolve().parents[1]

def test_role_registry_and_plan_cover_every_role_once():
    registry=load_role_registry(ROOT); assert registry['role_count']==227
    plan=build_team_contribution_plan('p',root=ROOT,project_type='animation',production_route='generative')
    assert plan['coverage_complete'] and plan['role_count']==227
    assert len({x['role_id'] for x in plan['contributions']})==227
    assert all(x['disposition'] in registry['dispositions'] for x in plan['contributions'])
    assert any(x['department']=='Animation-Specific Roles' and x['disposition']!='not_applicable' for x in plan['contributions'])
    assert any(x['department']=='Documentary-Specific Roles' and x['disposition']=='not_applicable' for x in plan['contributions'])
    assert plan['human_blockers']

@pytest.mark.parametrize('command',[
    'higgsfield generate create kling3_0 --prompt x',
    'higgsfield generate workflow wf-1 --json',
    'film-studio provider-submit approval.json',
])
def test_pre_tool_guard_blocks_direct_external_side_effects(command):
    payload=json.dumps({'input':{'command':command}})
    env={k:v for k,v in os.environ.items() if k!='FILM_STUDIO_EXTERNAL_AUTHORIZED'}
    run=subprocess.run([sys.executable,str(ROOT/'.bob/hooks/pre_tool_guard.py')],input=payload,text=True,capture_output=True,env=env)
    assert run.returncode==2 and 'matching approval record' in run.stderr

def test_pre_tool_guard_allows_read_only_discovery_and_explicit_environment_boundary():
    payload=json.dumps({'input':{'command':'higgsfield model list --json'}})
    assert subprocess.run([sys.executable,str(ROOT/'.bob/hooks/pre_tool_guard.py')],input=payload,text=True).returncode==0
    env={**os.environ,'FILM_STUDIO_EXTERNAL_AUTHORIZED':'1'}
    side=json.dumps({'input':{'command':'higgsfield generate create kling3_0 --prompt x'}})
    assert subprocess.run([sys.executable,str(ROOT/'.bob/hooks/pre_tool_guard.py')],input=side,text=True,env=env).returncode==0

def test_higgsfield_adapter_uses_positional_model_and_enforces_bound_approval():
    commands=[]
    def runner(argv):
        commands.append(argv)
        if argv[1:3]==['model','get']: return {'id':argv[3],'parameters':{'prompt':'string'}}
        if argv[1:3]==['generate','cost']: return {'estimated_cost_usd':3.25}
        if argv[1:3]==['generate','create']: return {'job_id':'job-1','status':'submitted'}
        raise AssertionError(argv)
    adapter=HiggsfieldCLIAdapter(runner=runner,live_enabled=True)
    compiled=adapter.compile({'job_set_type':'kling3_0','prompt':'A governed shot','parameters':{'duration':5}})
    dry=adapter.submit(compiled,project_id='p',idempotency_key='k',dry_run=True)
    assert dry['command'][2:4]==['create','kling3_0'] and '--model' not in dry['command']
    with pytest.raises(AuthorizationRequired): adapter.submit(compiled,project_id='p',idempotency_key='k',authorized=True,dry_run=False)
    approval={'status':'approved','project_id':'p','provider':'higgsfield-cli','operation':'generate.create','request_hash':compiled['request_hash'],'decided_by':'producer-1','expires_at':(datetime.now(timezone.utc)+timedelta(hours=1)).isoformat(),'max_cost_usd':4.0}
    result=adapter.submit(compiled,project_id='p',idempotency_key='k',authorized=True,dry_run=False,approval=approval)
    assert result['external_job_id']=='job-1' and result['estimated_cost_usd']==3.25
    assert any(c[1:3]==['model','get'] for c in commands) and any(c[1:3]==['generate','cost'] for c in commands)

def test_prompt_spec_v3_contains_exact_fifteen_sections_and_provenance():
    shot=ShotSpecV2(shot_id='sh1',project_id='p',scene_id='sc1',story_function='reveal',emotional_objective='dread',duration_seconds=4,camera=CameraSpec(shot_size='CU',lens_mm=50,movement='push'),performance=PerformanceSpec(objective='hide fear',tactic='deflect'),continuity_constraints=['same red coat'],reference_artifact_ids=['ref-1'])
    packet=compile_prompt_spec_v3(shot,source_version_ids=['v1'])
    assert tuple(packet.sections.model_fields)==PROMPT_SPEC_V3_HEADINGS
    assert packet.source_version_ids==['v1'] and packet.sections.positive_locks==['same red coat']

@pytest.mark.parametrize('name',[
    'book_to_film_v2','script_to_film_v2','script_to_series_v2','script_to_animation_v2','script_to_documentary_v2','team_contribution_v2','higgsfield_shot_batch_v2','repository_release_audit_v2'
])
def test_master_workflows_are_executable(name):
    workflow=load_workflow(ROOT/'workflows/v2'/f'{name}.json')
    assert workflow.topological_order() and workflow.version=='2.0.0'
