from pathlib import Path
from film_studio_os.state import StateStore
from film_studio_os.domain_entities import Project
from film_studio_os.mcp_server import tool_manifest

def test_project_registry_persists_and_lists(tmp_path):
    s=StateStore(tmp_path/'s.db'); p=Project(project_id='p1',studio_id='s1',title='Short',project_type='short')
    s.put_project(p.model_dump(mode='json'))
    assert s.get_project('p1')['title']=='Short'; assert [x['project_id'] for x in s.list_projects()]==['p1']

def test_mcp_surface_is_bounded_and_never_exposes_live_submit_or_approval_decision():
    m=tool_manifest(); assert len(m['tools'])>=10
    assert not m['live_provider_submission_exposed']; assert not m['approval_decision_exposed']
    assert 'run_dry_run_pilot' in m['tools'] and 'pending_approvals' in m['tools']
