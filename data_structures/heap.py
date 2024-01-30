from heap_type import HeapType
from math import floor


class Heap:
    """
    Implementation of a heap

    Supports max / min binary heap.
    Given node at index i, children are at 2i+1 and 2i+2 with parent at floor((i-1)/2).

    Attributes
    ----------
    @size: int
        size of heap
    is_empty: boolean
        Returns whether heap is empty or not
    kind: HeapType
        Indication of what kind of heap, max or min
    _heap_arr: List[int]
        List representation of heap

    Methods
    -------
    ( BASE )
    Peek : Find root
    Push : Add new item (sift up)
    Pop : Return root value after removing from heap
    Delete Root : Remove root node
    Replace : Pop root and push new key (sift down)

    ( INTERNAL )
    Sift Up : Satisfy heap property with new node at bottom
    Sift Down : Satisfy heap property with new node at root

    ( EXTENSION )
    Heapify : Create heap out of given array of elements
    Merge : Merge two heaps into one
    """
    def __init__(self, kind: HeapType):
        self.is_empty = True
        self.kind = kind
        self._heap_arr = []

    @property
    def size(self):
        return len(self._heap_arr)

    def reset(self):
        self.is_empty = True
        self._heap_arr = []

    def _satisfied(self, child_node: int, par_node: int) -> bool:
        """
        Check if heap property is satisfied between two nodes given heap type, self.kind 
        :param child_node: int, child node
        :param par_node: int, parent node 
        :return: bool
        """
        if self.kind == HeapType.MIN:
            if par_node < child_node:
                return True
            else:
                return False
        elif self.kind == HeapType.MAX:
            if par_node > child_node:
                return True
            else:
                return False
        else:
            raise Exception("HeapType {kind} not supported".format(kind=self.kind))

    def peek(self):
        """
        Return root of heap
        :return: int, root
        """
        if self.is_empty:
            raise Exception("Heap is empty, can not peek")
        else:
            return self._heap_arr[0]

    def push(self, node: int):
        """
        Add node to heap. Utilizes _sift_up to satisfy heap property
        :param node: int, new node
        :return: None
        """
        self._heap_arr.append(node)
        if self.is_empty:
            self.is_empty = False
        self._sift_up()

    def _sift_up(self):
        """
        Satisfy heap property by sifting up the heap

        Repeatedly check, until satisfied or at root, that given node at index i, node at floor((i-1)/2) satisfies
        heap property
        :return: None
        """
        if self.is_empty:
            raise Exception("Heap is empty, can not sift up")
        else:
            child_ind = self.size - 1
            while child_ind > 0:
                par_ind = floor((child_ind - 1) / 2)
                child_node = self._heap_arr[child_ind]
                par_node = self._heap_arr[par_ind]
                if self._satisfied(child_node, par_node):
                    break
                else:
                    self._heap_arr[par_ind] = child_node 
                    self._heap_arr[child_ind] = par_node
                    child_ind = par_ind
