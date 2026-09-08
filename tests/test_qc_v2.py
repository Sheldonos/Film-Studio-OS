from film_studio_os.qc import evaluate_layered_gate

def test_high_average_cannot_override_rights_blocker():
    r=evaluate_layered_gate(gate_id='g',project_id='p',subject_id='s',reviewer='qc',required_metrics=['story','image'],metric_scores={'story':5,'image':5},threshold=4,findings=[{'category':'rights','severity':'critical','message':'missing rights'}])
    assert not r.passed; assert any(x.blocker for x in r.hard_blockers)

def test_missing_required_metric_is_blocker():
    r=evaluate_layered_gate(gate_id='g',project_id='p',subject_id='s',reviewer='qc',required_metrics=['story','image'],metric_scores={'story':5},threshold=4)
    assert not r.passed; assert any(x.category=='missing_evidence' for x in r.hard_blockers)

def test_weighted_preferences_can_pass_when_no_blockers():
    r=evaluate_layered_gate(gate_id='g',project_id='p',subject_id='s',reviewer='qc',required_metrics=['story','image'],metric_scores={'story':5,'image':4},threshold=4.2,weights={'story':2,'image':1})
    assert r.passed; assert r.weighted_score>4.2
