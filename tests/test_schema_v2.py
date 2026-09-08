from pathlib import Path
import json, pytest
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
SCHEMAS=sorted((ROOT/'schemas/v2').glob('*.schema.json'))

def test_schema_index_and_count():
    idx=json.loads((ROOT/'schemas/v2/index.json').read_text())
    assert idx['schema_version']=='2.0'; assert len(idx['models'])==9

def test_generated_schemas_are_draft202012_and_closed():
    for p in SCHEMAS:
        d=json.loads(p.read_text()); Draft202012Validator.check_schema(d)
        assert d['$schema'].endswith('2020-12/schema')
        assert d.get('additionalProperties') is False

def test_rights_schema_rejects_unknown_property():
    d=json.loads((ROOT/'schemas/v2/RightsRecord.schema.json').read_text())
    v=Draft202012Validator(d)
    errors=list(v.iter_errors({'schema_version':'2.0','rights_record_id':'r','source_asset_id':'s','unexpected':1}))
    assert any('Additional properties' in e.message for e in errors)
