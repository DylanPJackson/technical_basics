import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.sample_graph_1_path = "sample_graph_1.json"
        self.graph.load_from_json(self.sample_graph_1_path)

    @unittest.expectedFailure
    def test_load_from_json_bad_path(self):
        self.graph.load_from_json('loadmeeeee')

    def test_load_from_json(self):
        self.graph.load_from_json(self.sample_graph_1_path)
        print(self.graph)

    @unittest.expectedFailure
    def test_check_adjacency_fail_first(self):
        self.graph.check_adjacency('dogs', 'PA')

    @unittest.expectedFailure
    def test_check_adjacency_fail_second(self):
        self.graph.check_adjacency('PA', 'dogs')

    @unittest.expectedFailure
    def test_check_adjacency_fail_both(self):
        self.graph.check_adjacency('dogs', 'cats')

    def test_check_adjacency(self):
        # Not adjacent
        adjacent = self.graph.check_adjacency('OH', 'NJ')
        self.assertFalse(adjacent)
        # Adjacent
        adjacent = self.graph.check_adjacency('PA', 'NJ')
        self.assertTrue(adjacent)

    @unittest.expectedFailure
    def test_get_neighbors_fail(self):
        self.graph.get_neighbors('dogs')

    def test_get_neighbors(self):
        real_neighbors = ['NJ', 'OH']
        maybe_neighbors = self.graph.get_neighbors('PA')
        self.assertEqual(real_neighbors, maybe_neighbors)


if __name__ == "__main__":
    unittest.main()
