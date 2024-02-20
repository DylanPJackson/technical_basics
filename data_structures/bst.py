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

    def empty(self):
        self.neighbors = {}
        self.root = None

    def search(self, search_key: int):
        """
        Return search_key if exists, otherwise none

        :param search_key: key to search for
        :return: int, None
        """
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
        return root_key

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
                raise Exception("Side : {side} not supported".format(side=side))
        else:
            raise Exception("Key : {parent} does not exist in tree".format(parent=parent))

    def insert(self, ins_key: int):
        """
        Add key to BST

        :param ins_key: key to insert
        :return: None
        """
        if self.is_empty:
            self.root = ins_key
            self.neighbors[ins_key] = [None, None]
        else:
            curr_key = self.root
            while curr_key is not None:
                if ins_key <= curr_key:
                    if self.neighbors[curr_key][0] is None:
                        self.neighbors[curr_key][0] = ins_key
                        self.neighbors[ins_key] = [None, None]
                        break
                    else:
                        curr_key = self.neighbors[curr_key][0]
                else:
                    if self.neighbors[curr_key][1] is None:
                        self.neighbors[curr_key][1] = ins_key
                        self.neighbors[ins_key] = [None, None]
                        break
                    else:
                        curr_key = self.neighbors[curr_key][1]

    def _rec_traverse(self, order: str, curr_key: int):
        """
        Recursively traverse tree to return string representation of tree with given order

        :param order:
        :param curr_key:
        :return: string representation of tree
        """
        if curr_key is None:
            return ""
        else:
            if order == 'pre':
                return (' {curr_key} '.format(curr_key=curr_key) +
                        self._rec_traverse(order, self.neighbors[curr_key][0]) +
                        self._rec_traverse(order, self.neighbors[curr_key][1]))
            elif order == 'post':
                return (self._rec_traverse(order, self.neighbors[curr_key][0]) +
                        self._rec_traverse(order, self.neighbors[curr_key][1]) +
                        ' {curr_key} '.format(curr_key=curr_key))
            elif order == 'in':
                return (self._rec_traverse(order, self.neighbors[curr_key][0]) +
                        ' {curr_key} '.format(curr_key=curr_key) +
                        self._rec_traverse(order, self.neighbors[curr_key][1]))
            else:
                raise Exception("Can not perform traverse with order : {order}".format(order=order))

    def traverse(self, order: str):
        """
        Return a string representation of the tree in the given traverse order
        :param order: str, [pre, post, in]
        :return: string representation of tree
        """
        curr_key = self.root
        return self._rec_traverse(order, curr_key)

    def delete(self, key: int):
        """
        Remove given key from tree
        :param key: key to remove
        :return: None
        """
        pass
