from pathlib import Path
import pytest
from film_studio_os.pilots import PILOTS,run_pilot
ROOT=Path(__file__).resolve().parents[1]

@pytest.mark.parametrize('name',list(PILOTS))
def test_required_pilot_completes_with_mock_only_and_independent_review(name,tmp_path):
    r=run_pilot(name,ROOT,tmp_path/f'{name}.db')
    assert r['status']=='complete'; assert len(r['work_orders'])==7
    assert all(w['status']=='done' for w in r['work_orders'])
    assert all(float(w.get('actual_cost_usd',0))==0 for w in r['work_orders'])
    assert r['review_rounds']>=1
    assert r['reproduction_manifest']['artifact_count']>=len(r['work_orders'])
    assert r['reproduction_manifest']['final_version_id'] in r['work_orders'][-1]['output_version_ids']

@pytest.mark.parametrize('name',list(PILOTS))
def test_pilot_event_log_contains_review_and_provider_provenance(name,tmp_path):
    from film_studio_os.state import StateStore
    db=tmp_path/f'{name}.db'; r=run_pilot(name,ROOT,db); s=StateStore(db); events=s.events(f'pilot-{name}')
    types={e['event_type'] for e in events}; assert 'independent_review_requested' in types; assert 'independent_review_accepted' in types; assert 'provider_job_recorded' in types
