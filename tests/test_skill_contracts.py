from pathlib import Path
import hashlib, json, re, yaml, pytest
ROOT=Path(__file__).resolve().parents[1]
SKILLS=sorted((ROOT/'.bob/skills').glob('*/SKILL.md'))
PARAM=[p.parent.name for p in SKILLS]

def sp(name): return ROOT/'.bob/skills'/name/'SKILL.md'
def contract(name): return ROOT/'.bob/skills'/name/'references/contract.md'

def proc(name):
    t=sp(name).read_text(); return re.search(r'## Procedure\n(.*?)(?:\n## |\Z)',t,re.S).group(1).strip()

@pytest.mark.parametrize('name',PARAM)
def test_skill_positive_trigger(name):
    assert '## Positive trigger example' in contract(name).read_text()

@pytest.mark.parametrize('name',PARAM)
def test_skill_negative_trigger(name):
    assert '## Negative trigger example' in contract(name).read_text()

@pytest.mark.parametrize('name',PARAM)
def test_skill_contract_and_missing_input_behavior(name):
    t=contract(name).read_text()
    for heading in ['## Authoritative inputs','## Missing-input behavior','## Output contract','## Failure taxonomy','## Recovery']:
        assert heading in t
    assert 'Fail closed' in t
    for heading in ['## Skill-specific decision rules','## Skill-specific output shape','## Skill-specific quality checks','## Handoff']:
        assert heading in t

@pytest.mark.parametrize('name',PARAM)
def test_skill_provenance_and_review_boundary(name):
    t=sp(name).read_text()+contract(name).read_text()
    assert 'provenance' in t.lower()
    assert 'independent' in t.lower()

@pytest.mark.parametrize('name',PARAM)
def test_skill_has_runtime_alias_or_new_capability(name):
    t=contract(name).read_text()
    assert '## Runtime capability aliases' in t
    aliases=[x[2:].strip('`') for x in t.splitlines() if x.startswith('- `')]
    assert aliases

@pytest.mark.parametrize('name',PARAM)
def test_skill_procedure_is_substantive(name):
    p=proc(name); steps=[x for x in p.splitlines() if re.match(r'\d+\.',x.strip())]
    assert len(steps)>=5
    assert len(p)>=300

def test_active_skill_procedures_are_not_shared_shells():
    hashes=[hashlib.sha256(proc(n).encode()).hexdigest() for n in PARAM]
    assert len(hashes)==len(set(hashes))==len(PARAM)==51

@pytest.mark.parametrize('name',PARAM)
def test_skill_has_specific_example_and_counterexample(name):
    t=contract(name).read_text()
    assert '## Example' in t and '## Counterexample' in t
    ex=t.split('## Example',1)[1].split('## Counterexample',1)[0].strip()
    cx=t.split('## Counterexample',1)[1].strip()
    assert len(ex)>80 and len(cx)>60
