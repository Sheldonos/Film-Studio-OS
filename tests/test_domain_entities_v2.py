import json,inspect
from pathlib import Path
import pytest
from pydantic import BaseModel,ValidationError
import film_studio_os.domain_entities as de
ROOT=Path(__file__).resolve().parents[1]

def test_canonical_domain_schema_catalog_is_strict_and_large_enough():
    idx=json.loads((ROOT/'schemas/v2/domain/index.json').read_text())
    assert len(idx['models'])>=50
    for name in idx['models']:
        schema=json.loads((ROOT/f'schemas/v2/domain/{name}.json').read_text())
        assert schema.get('additionalProperties') is False
        assert schema.get('$id','').endswith(f'/{name}.json')

def test_project_and_source_are_typed_and_reject_unknown_fields():
    p=de.Project(project_id='p',studio_id='s',title='Film',project_type='short')
    assert p.status=='development'
    with pytest.raises(ValidationError): de.Project(project_id='p',studio_id='s',title='Film',project_type='short',bogus=True)
    with pytest.raises(ValidationError): de.SourceAsset(source_asset_id='x',project_id='p',filename='a',media_type='text/plain',sha256='nope',source_kind='book')

def test_story_and_production_entities_encode_nonempty_craft_contracts():
    c=de.CharacterBible(character_bible_id='c',project_id='p',name='A',identity_invariants=['scar'],want='leave',contradiction='brave but evasive')
    sc=de.SceneCard(scene_card_id='sc',scene_id='s1',incoming_state='safe',objective='escape',obstacle='locked door',turn='ally betrays them',outgoing_state='trapped')
    gp=de.GenerationPlan(generation_plan_id='g',shot_id='sh',strategy='video',max_attempts=2)
    assert c.want and sc.turn and gp.max_attempts==2
