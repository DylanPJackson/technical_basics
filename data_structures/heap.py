from heap_type import HeapType
from math import floor
from typing import Any


class Heap:
    """
    Implementation of a heap

    Supports max / min binary heap.
    Given node at index i, children are at 2i+1 and 2i+2 with parent at floor((i-1)/2).

    Attributes
    ----------
    @size: int
        size of heap
    @is_empty: boolean
        Returns whether heap is empty or not
    kind: HeapType
        Indication of what kind of heap, max or min
    _heap_arr: List[Any]
        List representation of heap.

    Methods
    -------
    ( BASE )
    Peek : Find root
    Push : Add new item (sift up)
    Pop : Return root value after removing from heap (sift down)
    Delete Root : Remove root node (sift down)
    Replace : Pop root and push new key (sift down)

    ( INTERNAL )
    Sift Up : Satisfy heap property with new node at bottom
    Sift Down : Satisfy heap property with new node at root

    ( EXTENSION )
    Heapify : Create heap out of given array of elements
    Merge : Merge two heaps into one
    """
    def __init__(self, kind: HeapType = None):
        self.kind = kind
        self._heap_arr = []

    @property
    def size(self):
        return len(self._heap_arr)

    @property
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def empty(self):
        self._heap_arr = []

    def _satisfied(self, child_node: Any, par_node: Any) -> bool:
        """
        Check if heap property is satisfied between two nodes given heap type, self.kind 
        :param child_node: int, child node
        :param par_node: int, parent node 
        :return: bool
        """
        if child_node is None:
            return True
        if self.kind == HeapType.MIN:
            if par_node <= child_node:
                return True
            else:
                return False
        elif self.kind == HeapType.MAX:
            if par_node >= child_node:
                return True
            else:
                return False
        else:
            raise Exception("HeapType {kind} not supported".format(kind=self.kind))

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

    def _sift_down(self):
        """
        Satisfy heap property by sifting down the heap

        Repeatedly check, until satisfied or at leaf, that given index i, nodes at 2i+1 and 2i+2 satisfy heap property
        :return: None
        """
        if self.is_empty:
            raise Exception("Heap is empty, can not sift down")
        else:
            par_ind = 0
            while par_ind < (self.size - 1):
                child_1_ind = (2 * par_ind) + 1
                child_2_ind = (2 * par_ind) + 2
                par_node = self._heap_arr[par_ind]
                if child_1_ind < self.size:
                    child_1_node = self._heap_arr[child_1_ind]
                else:
                    child_1_node = None

                if child_2_ind < self.size:
                    child_2_node = self._heap_arr[child_2_ind]
                else:
                    child_2_node = None
                if self._satisfied(child_1_node, par_node) and self._satisfied(child_2_node, par_node):
                    # If satisfied with both children, break
                    break
                elif self._satisfied(child_1_node, par_node):
                    # If satisfied with only child 1, swap with child 2
                    self._heap_arr[child_2_ind] = par_node
                    self._heap_arr[par_ind] = child_2_node
                    par_ind = child_2_ind
                elif self._satisfied(child_2_node, par_node):
                    # If satisfied with only child 2, swap with child 1
                    self._heap_arr[child_1_ind] = par_node
                    self._heap_arr[par_ind] = child_1_node
                    par_ind = child_1_ind
                else:
                    # If not satisfied with either, swap with appropriate child
                    if self.kind == HeapType.MAX:
                        if child_1_node > child_2_node:
                            self._heap_arr[child_1_ind] = par_node
                            self._heap_arr[par_ind] = child_1_node
                            par_ind = child_1_ind
                        else:
                            self._heap_arr[child_2_ind] = par_node
                            self._heap_arr[par_ind] = child_2_node
                            par_ind = child_2_ind
                    elif self.kind == HeapType.MIN:
                        if child_1_node < child_2_node:
                            self._heap_arr[child_1_ind] = par_node
                            self._heap_arr[par_ind] = child_1_node
                            par_ind = child_1_ind
                        else:
                            self._heap_arr[child_2_ind] = par_node
                            self._heap_arr[par_ind] = child_2_node
                            par_ind = child_2_ind
                    else:
                        raise Exception("Heap type: {kind} not support".format(kind=self.kind))

    def peek(self):
        """
        Return root of heap
        :return: Any, root
        """
        if self.is_empty:
            raise Exception("Heap is empty, can not peek")
        else:
            return self._heap_arr[0]

    def push(self, node: Any):
        """
        Add node to heap. Utilizes _sift_up to satisfy heap property
        :param node: Any, new node
        :return: None
        """
        self._heap_arr.append(node)
        self._sift_up()

    def pop(self):
        """
        Remove root node and return it.

        Replaces root with most recently added node. Sift down with new root node.
        :return: Any, root node
        """
        if self.is_empty:
            raise Exception("Can not pop, heap is empty")
        else:
            old_root = self._heap_arr[0]
            new_root = self._heap_arr.pop()
            if not self.is_empty:
                self._heap_arr[0] = new_root
                self._sift_down()
            return old_root
