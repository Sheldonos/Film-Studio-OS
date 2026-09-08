import unittest
from film_studio_os.qc import evaluate_gate
class TestQC(unittest.TestCase):
    def test_gate(self):
        spec={'checks':['identity','continuity'],'minimum_score':4.0,'reviewer':'qc'}
        r=evaluate_gate('g',{'identity':4.5,'continuity':4.0},spec); self.assertTrue(r.passed)
        r2=evaluate_gate('g',{'identity':5.0},spec); self.assertFalse(r2.passed)
if __name__=='__main__': unittest.main()
