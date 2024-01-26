from simple_node import SimpleNode


class BasicQueue:
    """
    Implementation of a queue

    Support for enqueue, dequeue, and peek in O(1)

    Attributes
    ----------
    front: SimpleNode, None
        Pointer to front of queue, for dequeue and peek purposes
    tail : SimpleNode, None
        Pointer to end of queue, for enqueue purposes

    Methods
    -------
    enqueue : Add item to back of queue
    dequeue : Remove and return item from front of queue
    peek : Return value of first element
    """
    def __init__(self):
        root = SimpleNode()
        self.front = root
        self.tail = root

    def __str__(self):
        if self.front.head is None:
            return ''
        else:
            return 'Head -> ' + str(self.front)

    def enqueue(self, val):
        """
        Add val to the end of the queue
        :param val: int
            Value to add to queue
        :return: None
        """
        self.tail.head = SimpleNode(val, head=None, root=False)
        self.tail = self.tail.head

    def dequeue(self):
        """
        Remove and return the first item in the queue
        :return: int, value of dequeued item
        """
        if self.front.head is None:
            raise Exception("Queue is empty, can not dequeue")
        else:
            val = self.front.head.value
            self.front.head = self.front.head.head
            if self.front.head is None:
                self.tail = self.front
            return val

    def peek(self):
        """
        Return the value of the first item in the queue
        :return: int, value of first item
        """
        if self.front.head is None:
            raise Exception("Queue is empty, can not peek")
        else:
            return self.front.head.value
