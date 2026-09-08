from concurrent.futures import ThreadPoolExecutor
from film_studio_os.state import StateStore
from film_studio_os.artifacts import ArtifactRegistry

def test_revision_marks_only_descendants_stale(tmp_path):
    s=StateStore(tmp_path/'s.db'); a=ArtifactRegistry(s)
    root=a.create('p','script','Script',{'v':1},'writer',status='approved')
    child=a.create('p','shot','Shot',{'v':1},'director',parents=[root['version_id']],status='approved')
    grand=a.create('p','take','Take',{'v':1},'gen',parents=[child['version_id']],status='approved')
    unrelated=a.create('p','poster','Image',{'v':1},'art',status='approved')
    new,stale=a.revise(root['version_id'],{'v':2},'writer')
    assert stale=={child['version_id'],grand['version_id']}
    assert s.get_artifact(child['version_id'])['status']=='stale'; assert s.get_artifact(unrelated['version_id'])['status']=='approved'
    assert s.get_artifact(root['version_id'])['status']=='superseded'; assert new['parent_version_ids']==[root['version_id']]

def test_state_survives_restart_and_events_are_append_only(tmp_path):
    db=tmp_path/'s.db'; s=StateStore(db); s.event('p','one','x',{'n':1}); s.close()
    s2=StateStore(db); assert [e['event_type'] for e in s2.events('p')]==['one']; s2.event('p','two','x',{'n':2}); assert len(s2.events('p'))==2

def test_event_writes_are_thread_safe(tmp_path):
    s=StateStore(tmp_path/'s.db')
    def put(i): s.event('p','concurrent',str(i),{'i':i})
    with ThreadPoolExecutor(max_workers=8) as ex: list(ex.map(put,range(100)))
    assert len(s.events('p'))==100

def test_reproduction_manifest_walks_only_ancestors(tmp_path):
    s=StateStore(tmp_path/'s.db'); a=ArtifactRegistry(s)
    x=a.create('p','x','A',{'x':1},'a'); y=a.create('p','y','B',{'y':1},'b',parents=[x['version_id']]); a.create('p','z','C',{'z':1},'c')
    m=a.reproduction_manifest('p',y['version_id']); ids={v['version_id'] for v in m['artifacts']}
    assert ids=={x['version_id'],y['version_id']}

def test_staleness_metric_is_recorded(tmp_path):
    from film_studio_os.state import StateStore
    from film_studio_os.artifacts import ArtifactRegistry
    s=StateStore(tmp_path/'s.db'); r=ArtifactRegistry(s)
    a=r.create('p','a','Script',{'x':1},'writer')
    b=r.create('p','b','Shot',{'x':2},'director',parents=[a['version_id']])
    s.stale_downstream('p',a['version_id'])
    ms=s.metrics('p'); assert any(m['metric']=='stale_artifact_count' and m['value']==1 for m in ms)

def test_cross_project_artifact_dependency_and_manifest_access_are_blocked(tmp_path):
    import pytest
    s=StateStore(tmp_path/'s.db'); a=ArtifactRegistry(s)
    x=a.create('p1','x','A',{'x':1},'a')
    with pytest.raises(PermissionError): a.create('p2','y','B',{'y':1},'b',parents=[x['version_id']])
    with pytest.raises(PermissionError): a.reproduction_manifest('p2',x['version_id'])
