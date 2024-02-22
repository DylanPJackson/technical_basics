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

    def test_delete(self):
        # Delete root node with no children
        self.bst.insert(self.arr_1[0])
        self.bst.delete(self.arr_1[0])
        self.assertEqual("", self.bst.traverse())

        # Delete leaf node right side, not root
        self.bst.empty()
        self.bst.insert(self.arr_1[0])
        self.bst.insert(self.arr_1[1])
        self.bst.delete(self.arr_1[1])
        self.assertEqual(" 8 ", self.bst.traverse())

        # Delete leaf left side, not root
        self.bst.empty()
        self.bst.insert(self.arr_1[0])
        self.bst.insert(self.arr_1[2])
        self.bst.delete(self.arr_1[2])
        self.assertEqual(" 8 ", self.bst.traverse())


if __name__ == "__main__":
    unittest.main()
