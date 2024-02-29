import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.sample_graph_1_path = "sample_graph_1.json"
        self.sample_graph_2_path = "sample_graph_2.json"

    @unittest.expectedFailure
    def test_load_from_json_bad_path(self):
        self.graph.load_from_json('loadmeeeee')

    def test_load_from_json(self):
        self.graph.load_from_json(self.sample_graph_2_path)
        print(self.graph)

    @unittest.expectedFailure
    def test_check_adjacency_fail_first(self):
        self.graph.load_from_json(self.sample_graph_1_path)
        self.graph.check_adjacency('dogs', 'PA')

    @unittest.expectedFailure
    def test_check_adjacency_fail_second(self):
        self.graph.load_from_json(self.sample_graph_1_path)
        self.graph.check_adjacency('PA', 'dogs')

    @unittest.expectedFailure
    def test_check_adjacency_fail_both(self):
        self.graph.load_from_json(self.sample_graph_1_path)
        self.graph.check_adjacency('dogs', 'cats')

    def test_check_adjacency(self):
        self.graph.load_from_json(self.sample_graph_1_path)
        # Not adjacent
        adjacent = self.graph.check_adjacency('OH', 'NJ')
        self.assertFalse(adjacent)
        # Adjacent
        adjacent = self.graph.check_adjacency('PA', 'NJ')
        self.assertTrue(adjacent)

    @unittest.expectedFailure
    def test_get_neighbors_fail(self):
        self.graph.load_from_json(self.sample_graph_1_path)
        self.graph.get_neighbors('dogs')

    def test_get_neighbors(self):
        self.graph.load_from_json(self.sample_graph_1_path)
        real_neighbors = ['NJ', 'OH']
        maybe_neighbors = self.graph.get_neighbors('PA')
        self.assertEqual(real_neighbors, maybe_neighbors)

    @unittest.expectedFailure
    def test_bfs_fail_both(self):
        self.graph.load_from_json(self.sample_graph_1_path)
        self.graph.bfs('dogs', 'cats')

    @unittest.expectedFailure
    def test_bfs_fail_src(self):
        self.graph.load_from_json(self.sample_graph_1_path)
        self.graph.bfs('dogs', 'PA')

    @unittest.expectedFailure
    def test_bfs_fail_dst(self):
        self.graph.load_from_json(self.sample_graph_1_path)
        self.graph.bfs('PA', 'dogs')

    def test_bfs(self):
        self.graph.load_from_json(self.sample_graph_2_path)
        path_exist = self.graph.bfs('A', 'B')[0]
        self.assertTrue(path_exist)

        path_exist = self.graph.bfs('A', 'G')[0]
        self.assertTrue(path_exist)

        path_exist = self.graph.bfs('A', 'E')[0]
        self.assertFalse(path_exist)

        path = self.graph.bfs('A', 'G', True)[1]
        self.assertEqual(path, ['G', 'C', 'B', 'A'])

    def test_dfs(self):
        self.graph.load_from_json(self.sample_graph_2_path)
        path_exist = self.graph.dfs('A', 'B')[0]
        self.assertTrue(path_exist)

        path_exist = self.graph.dfs('A', 'G')[0]
        self.assertTrue(path_exist)

        path_exist = self.graph.dfs('A', 'E')[0]
        self.assertFalse(path_exist)


if __name__ == "__main__":
    unittest.main()
