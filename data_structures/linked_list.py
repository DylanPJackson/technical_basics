class LinkedList:
    """
    Represents a Linked List

    Supports basic insertion, deletion, and access either by index or value
    O(N) time for each.

    TODO
        Support for any type in LinkedList, not just int
        Support to perform operations in bulk

    Attributes
    ----------
    value : int
        value of current node
    head : None, LinkedList
        Pointer to next node
    root : boolean
        Flag indicating whether node is root node or not

    Methods
    -------

    """
    def __init__(self, value=0, root=True):
        """
        :param value: int, optional
            Value to use for node
        :param root: boolean, optional
            Indicator if root
        """
        self.value = value
        self.head = None
        self.root = root

    def __str__(self):
        if self.head is None:
            if self.root is True:
                return ''
            else:
                return '%d' % self.value
        else:
            if self.root is True:
                return 'Head -> ' + str(self.head)
            else:
                return ('%d -> ' % self.value) + str(self.head)

    @property
    def size(self):
        if self.head is None:
            return 0
        else:
            return self.head.size + 1

    def insert(self, val, ind=None):
        """
        Insert val at given index into Linked List

        :param val: int, LinkedList
            Value to be inserted
        :param ind: int, optional
            Index to insert value at
        :return: None
        """
        if ind is None:
            ind = self.size
        self.traverse(ind, "insert", val)

    def access_ind(self, ind: int):
        """
        Retrieve value at given index
        :param ind: int
            Index to retrieve value
        :return: int
        """
        return self.traverse(ind, "access")

    def delete_ind(self, ind):
        """
        Delete value at given index
        :param ind: int
            Index to delete value
        :return: None
        """
        self.traverse(ind, "delete")

    def delete_val(self, val):
        """
        Delete value if it exists in Linked list
        :param val: Any
            value to be deleted
        :return: None
        """
        self.traverse(ind=self.size - 1, action="delete", val=val)

    def traverse(self, ind, action, val=None):
        """
        Traverse Linked List and perform given action

        :param ind: int
            Index to perform action
        :param action: str
            Action to be performed
        :param val: int, LinkedList
            value to be inserted
        :return: None, int
        """
        if ind >= self.size and action != "insert":
            raise Exception("Index {ind} too large for LinkedList of size {size}".format(ind=ind, size=self.size))
        if action == "delete" and val is not None:
            if self.head.value == val:
                self.head = self.head.head
                return
            else:
                if self.head is None:
                    raise Exception("Delete failed. Value {val} not found in LinkedList".format(val=val))
                else:
                    return self.head.traverse(ind - 1, action, val)
        if ind == 0:
            if action == "access":
                return self.head.value
            elif action == "insert":
                if isinstance(val, LinkedList):
                    val.root = False
                    val.head = self.head
                    self.head = val
                else:
                    new_ll = LinkedList(val, root=False)
                    new_ll.head = self.head
                    self.head = new_ll
            elif action == "delete":
                self.head = self.head.head
            else:
                raise Exception("Action {action} unsupported".format(action=action))
        else:
            return self.head.traverse(ind - 1, action, val)
