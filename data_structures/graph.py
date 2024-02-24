class Graph:
    """
    Implementation of a weighted directed graph

    Utilizes an adjacency matrix to at once store relation and weight in one data point.
    Sacrifices space for convenience.

    Attributes
    ----------
    adj_matrix: List[List[int]]
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
        self.adj_matrix = [[]]

    @property
    def is_empty(self):
        if self.adj_matrix == [[]]:
            return True
        else:
            return False
