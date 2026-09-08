import unittest
from film_studio_os.orchestrator import ProductionGraph, TaskNode, Orchestrator

class TestGraph(unittest.TestCase):
    def test_topology_and_stale(self):
        g=ProductionGraph(); g.add(TaskNode('script','scene_writing','showrunner')); g.add(TaskNode('shots','shot_spec_compilation','cinematographer',['script'])); g.add(TaskNode('gen','video_generation_plan','generative_supervisor',['shots'])); g.finalize()
        self.assertEqual(g.topological_order(),['script','shots','gen'])
        self.assertEqual(g.mark_stale_downstream('script'),{'shots','gen'})
    def test_cycle_rejected(self):
        g=ProductionGraph(); g.add(TaskNode('a','x','a',['b'])); g.add(TaskNode('b','y','b',['a']))
        with self.assertRaises(ValueError): g.finalize()
    def test_critical_path(self):
        g=ProductionGraph(); g.add(TaskNode('a','x','a')); g.add(TaskNode('b','y','b',['a'])); g.add(TaskNode('c','z','c',['b'])); g.finalize()
        self.assertEqual(Orchestrator(g).critical_path(),['a','b','c'])
if __name__=='__main__': unittest.main()
