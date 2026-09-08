import unittest
from film_studio_os.continuity import ContinuityLedger
class TestContinuity(unittest.TestCase):
    def test_diff(self):
        l=ContinuityLedger(); l.set_state('s1',{'wardrobe':'red coat','prop_hand':'left','knowledge':'secret_unknown'})
        f=l.validate('s1',{'wardrobe':'blue coat','prop_hand':'right','knowledge':'secret_unknown'})
        self.assertEqual(len(f),2); self.assertTrue(any(x['field']=='wardrobe' for x in f))
    def test_inherit(self):
        l=ContinuityLedger(); l.set_state('s1',{'wardrobe':'red','wet':False}); l.inherit('s1','s2',{'wet':True}); self.assertTrue(l.states['s2']['wet'])
if __name__=='__main__': unittest.main()
