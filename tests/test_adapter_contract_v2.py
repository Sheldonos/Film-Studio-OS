from film_studio_os.adapters import AdapterRegistry,MockGenerationAdapter

def test_registry_rejects_duplicate():
    import pytest
    r=AdapterRegistry(); r.register(MockGenerationAdapter())
    with pytest.raises(ValueError): r.register(MockGenerationAdapter())

def test_mock_is_zero_cost_idempotent_async_lifecycle():
    a=MockGenerationAdapter(); req=a.compile({'shot_id':'s'}); est=a.estimate(req); assert est.amount_usd==0
    j1=a.submit(req,project_id='p',idempotency_key='same',dry_run=True); j2=a.submit(req,project_id='p',idempotency_key='same',dry_run=True)
    assert j1['external_job_id']==j2['external_job_id']; assert j1['status']=='succeeded'; assert j1['actual_cost_usd']==0

def test_mock_cancel():
    a=MockGenerationAdapter(); req=a.compile({'shot_id':'s'}); j=a.submit(req,project_id='p',idempotency_key='x',dry_run=False)
    assert j['status']=='running'; assert a.cancel(j['external_job_id'])['status']=='cancelled'

def test_mock_capability_manifest_has_policy_metadata():
    for c in MockGenerationAdapter().capabilities():
        for k in ['adapter_id','model_id','modality','inputs','outputs','dry_run_supported','commercial_use','training_policy','retention_policy','verified_at']:
            assert k in c
