import unittest
from bst import BST


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_search(self):
        # Test empty search
        search_key = 10
        search_result = self.bst.search(search_key)
        self.assertEqual(search_result, None)


if __name__ == "__main__":
    unittest.main()
