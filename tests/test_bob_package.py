from pathlib import Path
import re, yaml
from film_studio_os.bob_validate import validate_bob_package

ROOT=Path(__file__).resolve().parents[1]
SKILLS=sorted((ROOT/'.bob/skills').glob('*/SKILL.md'))
PERSONAS=sorted((ROOT/'.bob/agents').glob('*.md'))

def fm(path):
    t=path.read_text(); return yaml.safe_load(t.split('---',2)[1])

def test_bob_package_valid():
    r=validate_bob_package(ROOT)
    assert r['valid'], r
    assert r['stats']=={'modes':8,'personas':26,'active_skills':51}

def test_qc_mode_is_read_only():
    modes=yaml.safe_load((ROOT/'.bob/custom_modes.yaml').read_text())['customModes']
    qc=next(x for x in modes if x['slug']=='independent-qc')
    assert 'read' in qc['groups']
    assert 'edit' not in qc['groups'] and 'execute' not in qc['groups']

def test_mcp_has_no_secret_and_is_local_stdio():
    import json
    d=json.loads((ROOT/'.bob/mcp.json').read_text())['mcpServers']['film-studio-os']
    assert d['command']=='python'
    assert d['args']==['-m','film_studio_os.mcp_server']
    assert all('TOKEN' not in str(v).upper() and 'KEY' not in str(v).upper() for v in d.get('env',{}).values())

def test_personas_have_matching_frontmatter_and_least_privilege():
    for p in PERSONAS:
        d=fm(p); assert d['name']==p.stem; assert len(d['description'])>=20
        assert set(d.get('tools',[])) <= {'read','edit','command','browser','mcp'}

def test_every_active_skill_has_activation_contract():
    for p in SKILLS:
        d=fm(p); assert d['name']==p.parent.name; assert len(d['description'])>=20
        t=p.read_text(); assert '## Procedure' in t and '`references/contract.md`' in t
        assert (p.parent/'references/contract.md').is_file()
