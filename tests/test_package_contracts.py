from pathlib import Path
from film_studio_os.package_validate import validate_repository_contracts
ROOT=Path(__file__).resolve().parents[1]

def test_cross_layer_repository_contracts_resolve():
    r=validate_repository_contracts(ROOT)
    assert r['valid'], r['errors']
    assert r['stats']['registered_capabilities']>=70
    assert r['stats']['workflow_files']==28
    assert r['stats']['workflow_step_references']>=90
