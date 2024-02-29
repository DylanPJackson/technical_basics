from simple_node import SimpleNode


class Stack:
    """
    Implementation of stack

    Support for pop, push, peek operations in O(1)

    Attributes
    ----------
    top : None, Node
        Pointer to top item in Stack
    """

    def __init__(self):
        self.top = SimpleNode()

    def __str__(self):
        if self.top.head is None:
            return ''
        else:
            return 'Top -> ' + str(self.top)

    @property
    def is_empty(self):
        if self.top.head is None:
            return True
        else:
            return False

    def push(self, value):
        """
        Add value to top of stack
        :param value: Any
            Value to add on to stack
        :return: None
        """
        next_node = SimpleNode(value=value, head=self.top, root=False)
        self.top = next_node

    def peek(self):
        """
        Return value on top of stack
        :return: Any
        """
        if self.top.head is None:
            raise Exception("Stack is empty, can not peek")
        else:
            return self.top.value

    def pop(self):
        """
        Remove item from top of stack
        :return: Any
        """
        if self.top.head is None:
            raise Exception("Stack is empty, can not pop")
        else:
            val = self.top.value
            self.top = self.top.head
            return val
