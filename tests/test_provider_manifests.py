from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def test_dated_provider_manifests_exist_and_live_is_disabled():
    files=sorted((ROOT/'adapters/provider_manifests').glob('*.json')); assert len(files)>=4
    for p in files:
        d=json.loads(p.read_text()); assert d['as_of']=='2026-08-15'; assert d['live_enabled'] is False
        for k in ['adapter_id','status','commercial_use','training_policy','retention_policy','evidence']: assert k in d
    research=[json.loads(p.read_text()) for p in files if json.loads(p.read_text())['research_only']]
    assert research and all(not d['live_enabled'] for d in research)
