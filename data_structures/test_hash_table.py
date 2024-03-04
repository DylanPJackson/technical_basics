import unittest
from hash_table import HashTable


class TestHashtable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()
        self.key_1 = 'dogs'
        self.key_2 = 'cats'
        self.val_1 = 1
        self.val_2 = 0

    def tearDown(self):
        self.hash_table.empty()

    def test_insert(self):
        self.hash_table.insert(self.key_1, self.val_1)
        self.hash_table.insert(self.key_2, self.val_2)
        print(self.hash_table)

    @unittest.expectedFailure
    def test_access_no_exist(self):
        self.hash_table.access('aquarius')

    def test_access(self):
        self.hash_table.insert(self.key_1, self.val_1)
        val_1 = self.hash_table.access(self.key_1)
        self.assertEqual(self.val_1, val_1)

        self.hash_table.insert(self.key_2, self.val_2)
        val_2 = self.hash_table.access(self.key_2)
        self.assertEqual(self.val_2, val_2)

    def test_exists(self):
        exist = self.hash_table.exists('aquarius')
        self.assertFalse(exist)

        self.hash_table.insert(self.key_1, self.val_1)
        exist = self.hash_table.exists(self.key_1)
        self.assertTrue(exist)

        self.hash_table.insert(self.key_2, self.val_2)
        exist = self.hash_table.exists(self.key_2)
        self.assertTrue(exist)


if __name__ == "__main__":
    unittest.main()
