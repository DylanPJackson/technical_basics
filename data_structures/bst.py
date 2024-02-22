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
        self.neighbors = {}  # {'par_key': [parent, left_child, right_child], ...}
        self.root = None

    @property
    def is_empty(self):
        if self.root is None and self.neighbors == {}:
            return True
        else:
            return False

    def empty(self):
        self.neighbors = {}
        self.root = None

    def _get_nbr(self, key: int, rel: str, side: str = None):
        """
        Get the node with given relation
        :param key: int
        :param side: 'left' or 'right'
        :param rel: Relation to key, either 'parent' or 'child'
        :return: int if relative exists, None otherwise
        """
        if key in self.neighbors:
            nbr_list = self.neighbors[key]
            if rel == 'child':
                if side == "left":
                    return nbr_list[1]
                elif side == "right":
                    return nbr_list[2]
                else:
                    raise Exception("Side : {side} not supported".format(side=side))
            elif rel == 'parent':
                return nbr_list[0]
            else:
                raise Exception("Relation: {rel} not supported".format(rel=rel))

        else:
            raise Exception("Key : {key} does not exist in tree".format(key=key))

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
                        self._rec_traverse(order, self.neighbors[curr_key][1]) +
                        self._rec_traverse(order, self.neighbors[curr_key][2]))
            elif order == 'post':
                return (self._rec_traverse(order, self.neighbors[curr_key][1]) +
                        self._rec_traverse(order, self.neighbors[curr_key][2]) +
                        ' {curr_key} '.format(curr_key=curr_key))
            elif order == 'in':
                return (self._rec_traverse(order, self.neighbors[curr_key][1]) +
                        ' {curr_key} '.format(curr_key=curr_key) +
                        self._rec_traverse(order, self.neighbors[curr_key][2]))
            else:
                raise Exception("Can not perform traverse with order : {order}".format(order=order))

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
                root_key = self._get_nbr(root_key, 'child', 'left')
            elif search_key > root_key:
                root_key = self._get_nbr(root_key, 'child', 'right')
            else:
                raise Exception("Issue searching with search_key: {search_key} and root_key: {root_key}"
                                .format(search_key=search_key, root_key=root_key))
        return root_key

    def insert(self, ins_key: int):
        """
        Add key to BST

        :param ins_key: key to insert
        :return: None
        """
        if self.is_empty:
            self.root = ins_key
            self.neighbors[ins_key] = [None, None, None]
        else:
            curr_key = self.root
            while curr_key is not None:
                if ins_key <= curr_key:
                    if self.neighbors[curr_key][1] is None:
                        self.neighbors[curr_key][1] = ins_key
                        self.neighbors[ins_key] = [curr_key, None, None]
                        break
                    else:
                        curr_key = self.neighbors[curr_key][1]
                else:
                    if self.neighbors[curr_key][2] is None:
                        self.neighbors[curr_key][2] = ins_key
                        self.neighbors[ins_key] = [curr_key, None, None]
                        break
                    else:
                        curr_key = self.neighbors[curr_key][2]

    def traverse(self, order: str = 'in'):
        """
        Return a string representation of the tree in the given traverse order
        :param order: str, [pre, post, in]
        :return: string representation of tree
        """
        curr_key = self.root
        return self._rec_traverse(order, curr_key)

    def delete(self, key: int):
        """
        Remove given key from tree. Replace with in-order successor.
        :param key: key to remove
        :return: None
        """
        if self.is_empty:
            raise Exception("Cannot delete from empty tree")
        else:
            if key in self.neighbors:
                left_c = self._get_nbr(key, 'child', 'left')
                right_c = self._get_nbr(key, 'child', 'right')
                parent = self._get_nbr(key, 'parent')
                # Case 1 : No children
                if left_c is None and right_c is None:
                    if parent is not None:
                        if self.neighbors[parent][1] == key:
                            self.neighbors[parent][1] = None
                        elif self.neighbors[parent][2] == key:
                            self.neighbors[parent][2] = None
                        else:
                            raise Exception("Issue deleting key: {key} from parent: {parent}".format(key=key,
                                                                                                     parent=parent))
                    else:
                        self.root = None
                    del self.neighbors[key]
                # Case 2 : One child
                elif left_c is None or right_c is None:
                    if left_c is None:
                        child = right_c
                    else:
                        child = left_c
                    if parent is not None:
                        if self.neighbors[parent][1] == key:
                            self.neighbors[parent][1] = child
                        elif self.neighbors[parent][2] == key:
                            self.neighbors[parent][2] = child
                        else:
                            raise Exception("Issue deleting key: {key} from parent: {parent}".format(key=key,
                                                                                                     parent=parent))
                    else:
                        self.root = child
            else:
                raise Exception("Cannot delete key: {key} as it does not exist in bst")
        # Case 2 : One child
        # Case 3 : Two children
