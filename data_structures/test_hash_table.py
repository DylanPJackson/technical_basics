import unittest
from hash_table import HashTable


class TestHashtable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_insert(self):
        print(self.hash_table)


if __name__ == "__main__":
    unittest.main()
