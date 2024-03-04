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
            add_string = "{} : {}\n".format(ind, str(self.table[ind]))
            string_rep += add_string
        return string_rep

    def _get_hash_index(self, key: Any):
        hash_val = hash(key)  # OK with possible TypeError here because we can't use a non-hashable object anyway
        index = int((hash_val % self.capacity) // 1)
        return index

    def _traverse_ll_for_key(self, ll: LinkedList, key: Any):
        """
        Traverse linked list in search of key
        :param ll:
        :param key:
        :return: HashKeyPair, None
        """
        for ll_ind in range(ll.size):
            node = ll.access_ind(ll_ind)
            if isinstance(node, HashKeyPair):
                if node.key == key:
                    return node
            else:
                raise Exception("Item in linked list is not HashKeyPair. Please ensure all items added to the"
                                "HashTable are converted to HashKeyPair. Item : {}".format(node))
        return None

    def empty(self):
        self.size = 0
        self.capacity = 10
        self.table = [LinkedList() for i in range(self.capacity)]

    def insert(self, key: Any, val: Any):
        """
        Insert key with val into hash table
        :param key: Any
        :param val: Any
        :return: None
        """
        index = self._get_hash_index(key)
        keypair = HashKeyPair(key, val)
        self.table[index].insert(keypair)
        self.size += 1

    def exists(self, key: Any):
        """
        Returns boolean of if key exists in hash table or not
        :param key: Any
        :return: boolean
        """
        for table_ind in range(self.capacity):
            ll = self.table[table_ind]
            node = self._traverse_ll_for_key(ll, key)
            if node is not None:
                return True
        return False

    def access(self, key: Any):
        """
        Return value of key in table if it exists
        :param key: any
        :return: value of key, Any
        """
        if self.exists(key):
            index = self._get_hash_index(key)
            ll = self.table[index]
            node = self._traverse_ll_for_key(ll, key)
            if node is not None:
                return node.val
        else:
            raise Exception("Key : {} does not exist in table".format(key))


class HashKeyPair:
    def __init__(self, key: Any, val: Any):
        self.key = key
        self.val = val

    def __repr__(self):
        return "HashKeyPair(key: {}, val: {})".format(self.key, self.val)
