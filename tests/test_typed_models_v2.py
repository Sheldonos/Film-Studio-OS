import pytest
from pydantic import ValidationError
from film_studio_os.typed_models import RightsRecord, ConsentRecord, Approval, WorkOrderV2, GateResultV2, Finding

def test_strict_extra_fields_rejected():
    with pytest.raises(ValidationError): RightsRecord(rights_record_id='r',source_asset_id='s',surprise=True)

def test_cleared_rights_require_evidence_and_adaptation_scope():
    with pytest.raises(ValidationError): RightsRecord(rights_record_id='r',source_asset_id='s',status='cleared',basis='owned',approved_by='legal')
    r=RightsRecord(rights_record_id='r',source_asset_id='s',status='cleared',basis='owned',adaptation_allowed=True,evidence_artifact_ids=['e'],approved_by='legal')
    assert r.status.value=='cleared'

def test_replica_consent_requires_specific_intended_use_and_evidence():
    with pytest.raises(ValidationError): ConsentRecord(consent_id='c',person_or_entity='P',scope=['voice'],status='approved',voice_clone=True)
    c=ConsentRecord(consent_id='c',person_or_entity='P',scope=['voice'],status='approved',voice_clone=True,intended_use_description='Named character in project X only',evidence_artifact_ids=['release'])
    assert c.voice_clone

def test_decided_approval_requires_decider():
    with pytest.raises(ValidationError): Approval(approval_id='a',project_id='p',subject_type='work_order',subject_id='w',gate_id='g',status='approved',requested_from_role='producer')

def test_author_cannot_be_independent_reviewer():
    base=dict(work_order_id='w',project_id='p',workflow_id='f',step_id='s',capability_id='c',owner_agent='writer',idempotency_key='id')
    with pytest.raises(ValidationError): WorkOrderV2(**base,reviewer_agent='writer')

def test_gate_with_hard_blocker_cannot_pass():
    f=Finding(finding_id='f',category='rights',severity='critical',message='missing',blocker=True)
    with pytest.raises(ValidationError): GateResultV2(gate_id='g',project_id='p',subject_id='x',passed=True,hard_blockers=[f],reviewer='qc')
