from graph_node import Node
import json


class Graph:
    """
    Implementation of a weighted directed graph

    Maintains a dictionary of connections between Nodes and their weights.
    Allows for labeled nodes with weighted connections.

    Attributes
    ----------
    adj_map: Dict[Node: Dict[Node: int]]
    @is_empty: boolean

    Methods
    -------
    insert : Add new node to graph
    delete : Delete a node, if it exists
    search : Search for a node
    update_relation : Update relation between two nodes, either adding a new connection or removing an existing one
    update_weight : Update the weight of a connection between two nodes

    find_path : Find if a path exists between two nodes. Option to return path.
    bfs : Perform Breadth First Search to search for a path between two nodes
    dfs : Perform Depth First Search to search for a path between two nodes
    find_shortest_path : Find the shortest path between two nodes if it exists. Option to return path.
    find_cheapest_path : Find the cheapest path between two nodes if it exists. Option to return path.
    find_cheapest_shortest_path : Find cheapest and shortest path between two nodes if exists. Option to return path.
    find_path_in_k : Find if a path exists with max k connections if exists . Option to return path.
    find_cheapest_path_in_k : Find the cheapest path with max k connections if exists. Option to return path.
    """

    def __init__(self):
        self.adj_map = {}

    @property
    def is_empty(self):
        if self.adj_map == {}:
            return True
        else:
            return False

    def load_from_json(self, path: str):
        """
        Create graph from given json.

        JSON must be in the following format
        label: {val, {connection: weight, connection: weight...}}
        Example :
        {
            'node_1' : {
                'val': 10,
                'connections': {
                    'node_2': 2,
                    'node_3': 1
                }
            },
            'node_2' : {
                'val': 20,
                'connections': {
                    'node_1': 4
                }
            }
        }

        :param path: path to read in csv
        :return: None
        """
        if path:
            if path[-4:] != 'json':
                raise Exception("Can not read file : {}. Must be in csv format".format(path))
            else:
                with open(path) as f:
                    graph_dct = json.load(f)
                    node_dct = {}
                    for label in list(graph_dct.keys()):
                        node_dct[label] = graph_dct[label]['val']

                    for src_label in list(graph_dct.keys()):
                        dst_keys = list(graph_dct[src_label]['connections'].keys())
                        if dst_keys is not []:
                            for dst_label in dst_keys:
                                src_node = Node(src_label, node_dct[src_label])
                                dst_node = Node(dst_label, node_dct[dst_label])
                                weight = graph_dct[src_label]['connections'][dst_label]
                                self.adj_map[src_node] = {}
                                self.adj_map[src_node][dst_node] = weight
                        else:
                            self.adj_map[src_node] = {}
        else:
            raise Exception("You must provide a path to load from json")
