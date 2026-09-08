from film_studio_os.model_router import route_with_reasons

def candidate(a,m,q,**kw):
    base={'adapter_id':a,'model_id':m,'capabilities':{'identity':q,'motion':q},'commercial_use':'yes','training_policy':'none','retention_policy':'ephemeral','regions':['US'],'live_enabled':False,'normalized_cost':.2,'normalized_latency':.2,'reliability':.9,'evidence_confidence':.9}
    base.update(kw); return base

def test_policy_constraints_filter_before_quality():
    high=candidate('unsafe','m',5,training_policy='unknown')
    lower=candidate('safe','m',4)
    r=route_with_reasons(requirements={'identity':3,'motion':3},candidates=[high,lower],allowed_regions=['US'])
    assert r[0]['adapter_id']=='safe' and r[0]['eligible']
    bad=[x for x in r if x['adapter_id']=='unsafe'][0]; assert not bad['eligible']; assert any('training policy' in b for b in bad['blockers'])

def test_live_requirement_blocks_dry_run_candidate():
    r=route_with_reasons(requirements={'identity':1},candidates=[candidate('mock','m',5)],live_required=True)
    assert not r[0]['eligible'] and 'live execution is not enabled' in r[0]['blockers']

def test_route_returns_auditable_reason_and_confidence():
    r=route_with_reasons(requirements={'identity':3},candidates=[candidate('a','m',4)],allowed_regions=['US'])
    assert r[0]['eligible'] and r[0]['score'] is not None and r[0]['reasons'] and r[0]['confidence']==.9
