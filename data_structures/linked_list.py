"""
Linked List

A list comprised of nodes, where each node maintains its own value, and a
pointer to the next node, if any. The linked list should have a pointer
for the head and a pointer for the tail.

Let's start with just pointer for head, then expand.

Space
    N, number of nodes
Time
    Access : O(N)
    Delete : O(N)
    Insert : O(N)
"""


class LinkedList:
    def __init__(self, value=0, root=True):
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
        if ind is None:
            ind = self.size
        self.traverse(ind, "insert", val)

    def access_ind(self, ind: int):
        return self.traverse(ind, "access")

    def delete_ind(self, ind):
        self.traverse(ind, "delete")

    def traverse(self, ind, action, val=None):
        if ind >= self.size and action != "insert":
            raise Exception("Index {ind} too large for LinkedList of size {size}".format(ind=ind, size=self.size))
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
