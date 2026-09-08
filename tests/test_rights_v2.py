from film_studio_os.rights import release_blockers
from film_studio_os.typed_models import RightsRecord,ConsentRecord

def test_unverified_rights_block():
    r=RightsRecord(rights_record_id='r',source_asset_id='s')
    b=release_blockers([r],[],require_ai_processing=True); assert b

def test_cleared_owned_ai_processing_can_pass_without_performer_consent_if_no_replica_requested():
    r=RightsRecord(rights_record_id='r',source_asset_id='s',status='cleared',basis='owned',adaptation_allowed=True,ai_processing_allowed=True,evidence_artifact_ids=['e'],approved_by='legal')
    assert release_blockers([r],[],require_ai_processing=True)==[]
