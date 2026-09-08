from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def test_every_baseline_material_file_has_migration_classification():
    inv=json.loads((ROOT/'docs/audit/baseline_inventory.json').read_text())
    mig=json.loads((ROOT/'docs/audit/migration_map.json').read_text())
    # tolerate either list envelope or raw list produced by migration script
    inv_items=(inv.get('items') or inv.get('files')) if isinstance(inv,dict) else inv
    mig_items=(mig.get('items') or mig.get('files')) if isinstance(mig,dict) else mig
    assert len(inv_items)>=419; assert len(mig_items)>=419
    by={x['path']:x for x in mig_items}
    for f in inv_items: assert f['path'] in by and by[f['path']]['classification'] in {'keep','enhance','merge','replace','deprecate','remove'}

def test_all_178_legacy_skills_are_nonactivating_mapped_and_have_real_handoffs():
    files=sorted((ROOT/'skills').glob('*/skill.json')); assert len(files)==178
    for p in files:
        d=json.loads(p.read_text()); assert d['version']=='0.2.0'; assert d['bob_activation'] is False; assert d['handoff_to']; assert d['tests']==[]
        assert d['migration']['classification'] in {'keep_and_deepen','merge_as_subprocedure'}

def test_no_phantom_declared_legacy_tests_remain():
    total=0
    for p in (ROOT/'skills').glob('*/skill.json'): total+=len(json.loads(p.read_text()).get('tests',[]))
    assert total==0
