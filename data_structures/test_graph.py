import unittest
from graph import Graph
from graph_node import Node


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.sample_graph_1_path = "sample_graph_1.json"
        self.node_1 = Node('node_1', 10)
        self.node_2 = Node('node_2', 20)
        self.node_3 = Node('node_3', 15)
        self.sample_graph_1 = {self.node_1: {self.node_2: 2, self.node_3: 1},
                               self.node_2: {self.node_1: 4},
                               self.node_3: {}}

    @unittest.expectedFailure
    def test_load_from_json_bad_path(self):
        self.graph.load_from_json('loadmeeeee')

    def test_load_from_json(self):
        self.graph.load_from_json(self.sample_graph_1_path)


if __name__ == "__main__":
    unittest.main()
