from pathlib import Path
from film_studio_os.release_validate import hygiene_issues,validate_release
ROOT=Path(__file__).resolve().parents[1]

def test_hygiene_detects_cache_database_and_env(tmp_path):
    (tmp_path/'__pycache__').mkdir(); (tmp_path/'__pycache__/x.pyc').write_bytes(b'x')
    (tmp_path/'.env').write_text('SECRET=x'); (tmp_path/'state.db').write_bytes(b'x')
    issues=hygiene_issues(tmp_path); text='\n'.join(issues)
    assert 'cache' in text and '.env' in text and 'state.db' in text

def test_release_contracts_are_valid_ignoring_test_runtime_caches():
    r=validate_release(ROOT,ignore_runtime_caches=True)
    # The repository may contain no local state DB in release paths; actual final validation reruns without ignore.
    assert r['valid'], r['errors']
