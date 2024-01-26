from typing import Any, Union


class SimpleNode:
    """
    Node class which maintains value and pointer to next

    Attributes
    ----------
    value : Any
        Value of node
    head : None, Node (optional, default None)
        Pointer to next node
    root : bool (optional, default True)
        Indicator of root node
    """

    def __init__(self, value: Any = None, head: Union[None, 'SimpleNode'] = None, root: bool = True):
        self.value = value
        self.head = head
        self.root = root

    def __str__(self):
        if self.root:
            if self.head is None:
                return ''
            else:
                return str(self.head)
        else:
            if self.head is not None and not self.head.root:
                return '{value} -> '.format(value=str(self.value)) + str(self.head)
            else:
                return str(self.value)
