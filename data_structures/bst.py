class BST:
    """
    Implementation of a binary search tree using adjacency list

    Attributes
    ----------
    neighbors : dict
        adjacency list of nodes and children
    root : int / None
        root node
    @is_empty : bool
        Denotes whether bst is empty or not

    Methods
    -------
    search : Search for key in tree
    insert : Add node to tree in appropriate space per bst rules
    delete : Remove node from tree
    traverse (internal) : traverse tree in given order
    """
    def __init__(self):
        self.neighbors = {}  # {'par_key': [left_child, right_child], ...}
        self.root = None

    @property
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def search(self, search_key: int):
        root_key = self.root
        while root_key is not None:
            if root_key == search_key:
                return root_key
            elif search_key < root_key:
                root_key = self._get_child(root_key, 'left')
            elif search_key > root_key:
                root_key = self._get_child(root_key, 'right')
            else:
                raise Exception("Issue searching with search_key: {search_key} and root_key: {root_key}"
                                .format(search_key=search_key, root_key=root_key))
        return None

    def _get_child(self, parent: int, side: str):
        """
        Get the child from given side from given parent
        :param parent: int
        :param side: 'left' or 'right'
        :return: int if child exist, None otherwise
        """
        if parent in self.neighbors:
            nbr_list = self.neighbors[parent]
            if side == "left":
                return nbr_list[0]
            elif side == "right":
                return nbr_list[1]
            else:
                raise Exception("Side {side} not supported".format(side=side))
        else:
            raise Exception("Parent key : {parent} does not exist in tree".format(parent=parent))
