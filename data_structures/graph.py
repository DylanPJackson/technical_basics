import json


class Graph:
    """
    Implementation of a weighted directed graph

    Utilizes an adjacency matrix to track connection and weight, and table to track node labels.

    Attributes
    ----------
    adj_matrix: List[List[int, int]]
    label_table: Dict[str, int]
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
        self.adj_matrix = []
        self.label_table = {}

    @property
    def is_empty(self):
        if self.adj_matrix == [] and self.label_table == {}:
            return True
        else:
            return False

    def __str__(self):
        return "label_table : {}\nadj_matrix : {}".format(self.label_table, self.adj_matrix)

    def load_from_json(self, path: str):
        """
        Create graph from given json.

        JSON must be in the following format : {'labels' : Dict[str, int], 'adj_matrix': List[List[int]]}

        Example :
        {
            'labels' : {
                'PA': 0,
                'NJ': 1,
                'OH': 2
            },
            'adj_matrix' : {
                [-1, 4, 3],
                [2, -1, -1],
                [-1, -1, -1]
            }
        }

        :param path: path to read in JSON
        :return: None
        """
        if path:
            if path[-4:] != 'json':
                raise Exception("Can not read file : {}. Must be in csv format".format(path))
            else:
                with open(path) as f:
                    graph_dct = json.load(f)
                    self.label_table = graph_dct['labels']
                    self.adj_matrix = graph_dct['adj_matrix']
                    for label in list(self.label_table.keys()):
                        reverse_key = self.label_table[label]
                        self.label_table[reverse_key] = label
        else:
            raise Exception("You must provide a path to load from json")

    def check_adjacency(self, label_x: str, label_y: str):
        """
        Check if there is adjacency between two nodes with given labels

        Direction is accounted for, with label_x pointing to label_y.

        :param label_x: the label of first node
        :param label_y: label of second node
        :return: boolean
        """
        if label_x not in self.label_table and label_y not in self.label_table:
            raise Exception("Error checking adjacency between {} and {} as neither exist in graph".format(
                label_x, label_y))
        if label_x not in self.label_table:
            raise Exception("Error checking adjacency for {}, as it does not exist in graph.".format(label_x))
        if label_y not in self.label_table:
            raise Exception("Error checking adjacency for {}, as it does not exist in graph.".format(label_y))

        index_x = self.label_table[label_x]
        index_y = self.label_table[label_y]
        if self.adj_matrix[index_x][index_y] != -1:
            return True
        else:
            return False

    def get_neighbors(self, label: str):
        """
        Return list of neighbors of node with given label

        :param label:
        :return: List
        """
        if label not in self.label_table:
            raise Exception("Error searching for neighbors of {} as it does not exist in graph".format(label))
        else:
            index = self.label_table[label]
            relations = self.adj_matrix[index]
            # Unnecessary list comprehension for fun
            return [self.label_table[relation_ind] for relation_ind in range(len(relations))
                    if relations[relation_ind] is not -1]
