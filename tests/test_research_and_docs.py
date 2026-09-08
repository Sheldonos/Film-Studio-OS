from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def test_source_register_is_dated_and_primary_heavy():
    d=json.loads((ROOT/'docs/research/source_register.json').read_text()); assert d['access_date']=='2026-08-15'; assert len(d['sources'])>=12
    assert all(x['implementation_implication'] and x['uncertainty'] for x in d['sources'])

def test_provider_matrix_never_labels_research_provider_live():
    d=json.loads((ROOT/'docs/research/provider_capability_matrix.json').read_text())
    live=[x for x in d['providers'] if x['adapter_id']!='mock-generation' and x['live']]
    assert live==[]
