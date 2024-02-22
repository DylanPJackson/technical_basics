import unittest
from bst import BST


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.arr_1 = [8, 11, 4, 12, 7, 1, 10]
        self.arr_1_in = ' 1  4  7  8  10  11  12 '
        self.arr_1_pre = ' 8  4  1  7  11  10  12 '
        self.arr_1_post = ' 1  7  4  10  12  11  8 '
        self.arr_2 = [12, 6, 18, 9, 14]
        self.arr_2_in = ' 6  9  12  14  18 '
        self.arr_3 = [6, 4, 10, 5, 3, 12, 8, 11, 13, 7, 9]
        self.arr_3_in = ' 3  4  5  6  7  8  9  10  11  12  13 '

    def test_insert(self):
        for key in self.arr_1:
            self.bst.insert(key)
        trav_str = self.bst.traverse('in')
        self.assertEqual(trav_str, self.arr_1_in)

        self.bst.empty()

        for key in self.arr_2:
            self.bst.insert(key)
        trav_str = self.bst.traverse('in')
        self.assertEqual(trav_str, self.arr_2_in)

    @unittest.expectedFailure
    def test_insert_duplicate(self):
        self.bst.insert(self.arr_1[0])
        self.bst.insert(self.arr_1[0])

    def test_traverse(self):
        for key in self.arr_1:
            self.bst.insert(key)
        in_str = self.bst.traverse('in')
        self.assertEqual(in_str, self.arr_1_in)
        pre_str = self.bst.traverse('pre')
        self.assertEqual(pre_str, self.arr_1_pre)
        post_str = self.bst.traverse('post')
        self.assertEqual(post_str, self.arr_1_post)

    def test_search_empty(self):
        search_key = 10
        search_result = self.bst.search(search_key)
        self.assertEqual(search_result, None)

    def test_search_missing(self):
        for key in self.arr_1:
            self.bst.insert(key)

        search_key = 13
        search_result = self.bst.search(search_key)
        self.assertEqual(search_result, None)

        search_key = 0
        search_result = self.bst.search(search_key)
        self.assertEqual(search_result, None)

    def test_search(self):
        for key in self.arr_1:
            self.bst.insert(key)
        for search_key in self.arr_1:
            search_result = self.bst.search(search_key)
            self.assertEqual(search_result, search_key)

    @unittest.expectedFailure
    def test_delete_empty(self):
        self.bst.delete(self.arr_1[0])

    def test_delete_leaf_root(self):
        # Delete root node with no children
        self.bst.insert(self.arr_1[0])
        self.bst.delete(self.arr_1[0])
        self.assertEqual("", self.bst.traverse())

    def test_delete_leaf_left(self):
        # Delete leaf node left side, not root
        self.bst.insert(self.arr_1[0])
        self.bst.insert(self.arr_1[1])
        self.bst.delete(self.arr_1[1])
        self.assertEqual(" 8 ", self.bst.traverse())

    def test_delete_leaf_right(self):
        # Delete leaf right side, not root
        self.bst.insert(self.arr_1[0])
        self.bst.insert(self.arr_1[2])
        self.bst.delete(self.arr_1[2])
        self.assertEqual(" 8 ", self.bst.traverse())

    def test_delete_one_child_left_root(self):
        # Delete root node with one left child
        self.bst.insert(self.arr_1[0])
        self.bst.insert(self.arr_1[2])
        self.bst.delete(self.arr_1[0])
        self.assertEqual(" 4 ", self.bst.traverse())

    def test_delete_one_child_right_root(self):
        # Delete root node with one left child
        self.bst.insert(self.arr_1[0])
        self.bst.insert(self.arr_1[1])
        self.bst.delete(self.arr_1[0])
        self.assertEqual(" 11 ", self.bst.traverse())

    def test_delete_one_child_left(self):
        # Delete a node with a left child
        self.bst.insert(self.arr_1[0])
        self.bst.insert(self.arr_1[1])
        self.bst.insert(self.arr_1[2])
        self.bst.insert(self.arr_1[5])
        self.bst.delete(self.arr_1[2])
        self.assertEqual(" 1  8  11 ", self.bst.traverse())

    def test_delete_one_child_right(self):
        # Delete a node with a right child
        self.bst.insert(self.arr_1[0])
        self.bst.insert(self.arr_1[1])
        self.bst.insert(self.arr_1[2])
        self.bst.insert(self.arr_1[3])
        self.bst.delete(self.arr_1[1])
        self.assertEqual(" 4  8  12 ", self.bst.traverse())

    def test_delete_two_child_root_simple(self):
        # Delete a root node with two children, both children leaves
        self.bst.insert(self.arr_1[0])
        self.bst.insert(self.arr_1[1])
        self.bst.insert(self.arr_1[2])
        self.bst.delete(self.arr_1[0])
        self.assertEqual(" 4  11 ", self.bst.traverse())

    def test_delete_two_child_simple(self):
        # Delete a note with two children, both children leaves
        for key in self.arr_1:
            self.bst.insert(key)
        self.assertEqual(self.arr_1_in, self.bst.traverse())
        self.bst.delete(self.arr_1[1])
        self.assertEqual(" 1  4  7  8  10  12 ", self.bst.traverse())

    def test_delete_two_child_root(self):
        # Delete a root node with two children, both children non-trivial
        for key in self.arr_3:
            self.bst.insert(key)
        self.assertEqual(self.arr_3_in, self.bst.traverse())
        self.bst.delete(self.arr_3[0])
        self.assertEqual(" 3  4  5  7  8  9  10  11  12  13 ", self.bst.traverse())

    def test_delete_two_child(self):
        # Delete a node with two children, both non-trivial
        for key in self.arr_3:
            self.bst.insert(key)
        self.assertEqual(self.arr_3_in, self.bst.traverse())
        self.bst.delete(self.arr_3[2])
        self.assertEqual(" 3  4  5  6  7  8  9  11  12  13 ", self.bst.traverse())


if __name__ == "__main__":
    unittest.main()
