from pathlib import Path
import uuid, pytest
from film_studio_os.workflow import WorkflowDefinition,StepDefinition,WorkflowValidationError,WorkflowExecutor,load_workflow
from film_studio_os.state import StateStore
from film_studio_os.typed_models import Approval
ROOT=Path(__file__).resolve().parents[1]

def test_all_v2_workflow_families_load_and_are_acyclic():
    files=sorted((ROOT/'workflows/v2').glob('*.json')); assert len(files)==23
    for p in files:
        wf=load_workflow(p); assert wf.topological_order(); assert wf.version.startswith('2')

def test_unknown_dependency_and_cycle_rejected():
    with pytest.raises(WorkflowValidationError): WorkflowDefinition('x','2','', (StepDefinition('a','a','owner',('missing',)),)).topological_order()
    with pytest.raises(WorkflowValidationError): WorkflowDefinition('x','2','', (StepDefinition('a','a','o',('b',)),StepDefinition('b','b','o',('a',)))).topological_order()

def test_same_author_and_reviewer_rejected():
    with pytest.raises(WorkflowValidationError): WorkflowDefinition('x','2','', (StepDefinition('a','a','o',reviewer_agent='o'),)).topological_order()

def _review(store,project,wf,step,decider):
    store.grant_authorization(project,decider,step.reviewer_agent,'test-harness')
    wo=store.get_work_order_by_step(project,wf.workflow_id,step.id)
    a=Approval(approval_id=f'a-{uuid.uuid4().hex}',project_id=project,subject_type='work_order',subject_id=wo['work_order_id'],gate_id=f'review:{step.id}',status='approved',requested_from_role=step.reviewer_agent,decided_by=decider,rationale='test')
    store.put_approval(a.model_dump(mode='json'))

def test_independent_review_pauses_and_resume_does_not_rerun_author(tmp_path):
    wf=WorkflowDefinition('review-wf','2.0.0','',(StepDefinition('draft','write','writer',reviewer_agent='editor'),StepDefinition('next','use','director',('draft',))),)
    store=StateStore(tmp_path/'s.db'); ex=WorkflowExecutor(store)
    r=ex.run('p',wf); assert r['status']=='paused'; wo=store.get_work_order_by_step('p',wf.workflow_id,'draft'); assert wo['status']=='review'; assert wo['attempt_count']==1
    output=wo['output_version_ids'][0]
    # Author cannot satisfy the independent-review check even if a malformed approval record exists.
    _review(store,'p',wf,wf.steps[0],'writer'); r=ex.run('p',wf); assert store.get_work_order_by_step('p',wf.workflow_id,'draft')['status']=='review'
    _review(store,'p',wf,wf.steps[0],'fixture-editor'); r=ex.run('p',wf); assert r['status']=='complete'
    wo2=store.get_work_order_by_step('p',wf.workflow_id,'draft'); assert wo2['attempt_count']==1; assert wo2['output_version_ids']==[output]
    assert store.get_artifact(output)['status']=='approved'

def test_human_approval_pause(tmp_path):
    wf=WorkflowDefinition('approve','2.0.0','',(StepDefinition('release','release','producer',approval_required=True,gate_id='release'),))
    store=StateStore(tmp_path/'s.db'); ex=WorkflowExecutor(store); r=ex.run('p',wf); assert r['status']=='paused'; assert r['waiting_approval']==['release']

def test_retry_budget_then_success(tmp_path):
    wf=WorkflowDefinition('retry','2.0.0','',(StepDefinition('x','x','o',attempt_budget=3,handler='flaky'),))
    store=StateStore(tmp_path/'s.db'); ex=WorkflowExecutor(store); calls={'n':0}
    def flaky(ctx,step,wo):
        calls['n']+=1
        if calls['n']<2: raise RuntimeError('temporary')
        return {'output_version_ids':[],'actual_cost_usd':0}
    ex.register_handler('flaky',flaky)
    r=ex.run('p',wf); assert r['status']=='partial' or r['status']=='complete'
    if r['status']!='complete': r=ex.run('p',wf)
    assert r['status']=='complete'; assert store.get_work_order_by_step('p',wf.workflow_id,'x')['attempt_count']==2

def test_resume_after_store_reopen(tmp_path):
    db=tmp_path/'s.db'; wf=WorkflowDefinition('resume','2.0.0','',(StepDefinition('a','a','o'),StepDefinition('b','b','o',('a',))))
    s=StateStore(db); ex=WorkflowExecutor(s); r=ex.run('p',wf,max_steps=1); assert r['status']=='partial'; s.close()
    s2=StateStore(db); r2=WorkflowExecutor(s2).run('p',wf); assert r2['status']=='complete'; assert [w['attempt_count'] for w in r2['work_orders']]==[1,1]

def _decision(store,project,wf,step,decider,status='approved',gate=None):
    store.grant_authorization(project,decider,step.reviewer_agent or step.approval_role,'test-harness')
    wo=store.get_work_order_by_step(project,wf.workflow_id,step.id)
    a=Approval(approval_id=f'a-{uuid.uuid4().hex}',project_id=project,subject_type='work_order',subject_id=wo['work_order_id'],gate_id=gate or f'review:{step.id}',status=status,requested_from_role=step.reviewer_agent or step.approval_role,decided_by=decider,rationale='test decision')
    store.put_approval(a.model_dump(mode='json'))

def test_reviewer_rejection_fails_closed_and_marks_artifact_rejected(tmp_path):
    wf=WorkflowDefinition('reject-review','2.0.0','',(StepDefinition('draft','write','writer',reviewer_agent='editor'),))
    store=StateStore(tmp_path/'s.db'); ex=WorkflowExecutor(store); ex.run('p',wf)
    _decision(store,'p',wf,wf.steps[0],'fixture-editor','rejected')
    r=ex.run('p',wf); assert r['status']=='failed'
    wo=store.get_work_order_by_step('p',wf.workflow_id,'draft'); assert wo['failure_code']=='review_rejected'
    assert store.get_artifact(wo['output_version_ids'][0])['status']=='rejected'

def test_human_rejection_fails_closed_and_approval_status_persists(tmp_path):
    wf=WorkflowDefinition('reject-human','2.0.0','',(StepDefinition('release','release','producer',approval_required=True,gate_id='release'),))
    store=StateStore(tmp_path/'s.db'); ex=WorkflowExecutor(store); ex.run('p',wf)
    _decision(store,'p',wf,wf.steps[0],'fixture-producer','rejected',gate='release')
    r=ex.run('p',wf); assert r['status']=='failed'
    wo=store.get_work_order_by_step('p',wf.workflow_id,'release'); assert wo['approval_status']=='rejected'

def test_workflow_metrics_and_critical_path(tmp_path):
    wf=WorkflowDefinition('metrics','2.0.0','',(
        StepDefinition('a','a','o',estimated_duration_seconds=2),
        StepDefinition('b','b','o',('a',),estimated_duration_seconds=5),
        StepDefinition('c','c','o',('a',),estimated_duration_seconds=1),
    ))
    assert wf.critical_path()==(7.0,['a','b'])
    store=StateStore(tmp_path/'s.db'); r=WorkflowExecutor(store).run('p',wf); assert r['status']=='complete'
    names={m['metric'] for m in r['metrics']}; assert {'latency_ms','attempt_count','actual_cost_usd','acceptance'} <= names

def test_forged_unregistered_approver_cannot_release(tmp_path):
    wf=WorkflowDefinition('authz','2.0.0','',(StepDefinition('release','release','producer',approval_required=True,approval_role='release_authority',gate_id='release'),))
    store=StateStore(tmp_path/'s.db'); ex=WorkflowExecutor(store); ex.run('p',wf)
    wo=store.get_work_order_by_step('p',wf.workflow_id,'release')
    a=Approval(approval_id='forged',project_id='p',subject_type='work_order',subject_id=wo['work_order_id'],gate_id='release',status='approved',requested_from_role='release_authority',decided_by='unknown-user',rationale='not authorized')
    store.put_approval(a.model_dump(mode='json'))
    r=ex.run('p',wf); assert r['status']=='paused'; assert store.get_work_order_by_step('p',wf.workflow_id,'release')['status']=='waiting_approval'
    store.grant_authorization('p','known-user','release_authority','test-harness')
    a2=Approval(approval_id='valid',project_id='p',subject_type='work_order',subject_id=wo['work_order_id'],gate_id='release',status='approved',requested_from_role='release_authority',decided_by='known-user',rationale='authorized')
    store.put_approval(a2.model_dump(mode='json'))
    assert ex.run('p',wf)['status']=='complete'

def test_rights_blocker_is_nonretryable(tmp_path):
    wf=WorkflowDefinition('rights-block','2.0.0','',(StepDefinition('rights','rights','rights_clearance_supervisor',attempt_budget=3,handler='rights_gate'),))
    store=StateStore(tmp_path/'s.db'); ex=WorkflowExecutor(store)
    with pytest.raises(Exception) as e: ex.run('p',wf,inputs={'rights_records':[],'consent_records':[],'require_ai_processing':True})
    wo=store.get_work_order_by_step('p',wf.workflow_id,'rights'); assert wo['status']=='failed'; assert wo['attempt_count']==1
    assert not any(ev['event_type']=='work_order_retry' for ev in store.events('p'))

def test_post_execution_timeout_is_classified_and_retried(tmp_path,monkeypatch):
    import film_studio_os.workflow as mod
    wf=WorkflowDefinition('timeout','2.0.0','',(StepDefinition('x','x','o',attempt_budget=2,timeout_seconds=1,handler='ok'),))
    store=StateStore(tmp_path/'s.db'); ex=WorkflowExecutor(store); ex.register_handler('ok',lambda *a,**k:{'output_version_ids':[],'actual_cost_usd':0})
    values=iter([0.0,2.0,3.0,4.0,6.0,7.0]); monkeypatch.setattr(mod.time,'perf_counter',lambda:next(values))
    r=ex.run('p',wf); assert r['status']=='partial'; assert store.get_work_order_by_step('p',wf.workflow_id,'x')['failure_code']=='TimeoutError'
    with pytest.raises(TimeoutError): ex.run('p',wf)
    assert store.get_work_order_by_step('p',wf.workflow_id,'x')['attempt_count']==2
