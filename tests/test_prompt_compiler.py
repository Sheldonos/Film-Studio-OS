import unittest
from film_studio_os.models import ShotSpec
from film_studio_os.prompt_compiler import compile_shot_prompt
class TestPrompt(unittest.TestCase):
    def test_structured(self):
        s=ShotSpec('sh1','sc1','reveal threat','unease',location='station',camera_motion='slow track',negative_constraints=['no identity drift'])
        p=compile_shot_prompt(s); self.assertTrue(p['provider_neutral']); self.assertIn('location',p['provenance'])
if __name__=='__main__': unittest.main()
