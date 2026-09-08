import pytest
from adapters.higgsfield_cli import HiggsfieldCLIAdapter

def packet(): return {'sections':[{'field':'action','value':'walk'}]}

def test_legacy_higgsfield_is_dry_run_only():
    a=HiggsfieldCLIAdapter(); r=a.submit(packet(),'any-model','out',dry_run=True); assert r['dry_run'] is True
    with pytest.raises(RuntimeError,match='live execution disabled'): a.submit(packet(),'any-model','out',dry_run=False,authorized=True)
