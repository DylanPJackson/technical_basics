from linked_list import LinkedList
from typing import Any


class HashTable:
    """
    Implementation of a hash table, using a trivial hash function.

    Rather than
    """
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.table = [LinkedList() for i in range(self.capacity)]

    def __str__(self):
        string_rep = ""
        for ind in range(self.capacity):
            add_string = "{} : {}\n".format(ind, self.table[0])
            string_rep += add_string
        return string_rep

    def insert(self, val: Any):
        """
        Insert val into hash table
        :param val: Any
        :return: None
        """
        try:
            hash_val = hash(val)
        except TypeError:
            print("Can not hash {} with type {}".format(val, type(val)))
            return
        index = int((hash_val % self.capacity) // 1)
        self.table[index].insert(val)
        self.size += 1
