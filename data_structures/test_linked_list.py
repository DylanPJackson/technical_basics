import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.test_val_1 = 'dogs'
        self.test_val_2 = 234
        self.test_val_3 = 45

    def test_create(self):
        self.assertEqual(self.ll.value, 0)
        self.assertEqual(self.ll.head, None)
        self.assertTrue(self.ll.root)
        print(str(self.ll))

    def test_insert(self):
        self.assertEqual(self.ll.size, 0)
        self.ll.insert(self.test_val_1)
        self.assertEqual(self.ll.size, 1)
        str_check_1 = 'Head -> {val_1}'.format(val_1=self.test_val_1)
        self.assertEqual(str(self.ll), str_check_1)

        self.ll.insert(self.test_val_2)
        self.assertEqual(self.ll.size, 2)
        str_check_2 = 'Head -> {val_1} -> {val_2}'.format(val_1=self.test_val_1, val_2=self.test_val_2)
        self.assertEqual(str(self.ll), str_check_2)

    @unittest.expectedFailure
    def test_access_ind_empty(self):
        self.ll.access_ind(2)

    @unittest.expectedFailure
    def test_access_ind_outOfBounds_positive(self):
        self.ll.insert(10)
        self.ll.access_ind(1)

    @unittest.expectedFailure
    def test_access_ind_outOfBounds_negative(self):
        self.ll.insert(15)
        self.ll.access_ind(-1)

    def test_access_ind(self):
        self.ll.insert(self.test_val_1)
        self.ll.insert(self.test_val_2)
        self.ll.insert(self.test_val_3)
        self.assertEqual(self.ll.access_ind(0), self.test_val_1)
        self.assertEqual(self.ll.access_ind(1), self.test_val_2)
        self.assertEqual(self.ll.access_ind(2), self.test_val_3)

    @unittest.expectedFailure
    def test_delete_ind_outOfBounds_empty(self):
        self.ll.delete_ind(5)

    @unittest.expectedFailure
    def test_delete_ind_outOfBounds_positive(self):
        self.ll.insert(self.test_val_1)
        self.ll.delete_ind(4)

    @unittest.expectedFailure
    def test_delete_ind_outOfBounds_negative(self):
        self.ll.insert(self.test_val_1)
        self.ll.delete_ind(-1)

    def test_delete_ind(self):
        self.ll.insert(self.test_val_1)
        self.ll.insert(self.test_val_2)
        str_check_1 = 'Head -> {val_1} -> {val_2}'.format(val_1=self.test_val_1, val_2=self.test_val_2)
        self.assertEqual(str(self.ll), str_check_1)
        self.ll.delete_ind(0)
        str_check_2 = 'Head -> {val_2}'.format(val_2=self.test_val_2)
        self.assertEqual(str(self.ll), str_check_2)

        self.ll.insert(self.test_val_3)
        str_check_3 = 'Head -> {val_2} -> {val_3}'.format(val_2=self.test_val_2, val_3=self.test_val_3)
        self.assertEqual(str(self.ll), str_check_3)
        self.ll.delete_ind(1)
        self.assertEqual(str(self.ll), str_check_2)

        self.ll.delete_ind(0)
        str_check_4 = ''
        self.assertEqual(str(self.ll), str_check_4)

    @unittest.expectedFailure
    def test_delete_empty(self):
        self.ll.delete_val(self.test_val_1)

    @unittest.expectedFailure
    def test_delete_noExist(self):
        self.ll.insert(self.test_val_1)
        self.ll.delete_val(self.test_val_2)

    def test_delete_val(self):
        self.ll.insert(self.test_val_1)
        self.ll.insert(self.test_val_2)
        str_check_1 = 'Head -> {val_1} -> {val_2}'.format(val_1=self.test_val_1, val_2=self.test_val_2)
        self.assertEqual(str_check_1, str(self.ll))
        self.ll.delete_val(self.test_val_1)
        str_check_2 = 'Head -> {val_2}'.format(val_2=self.test_val_2)
        self.assertEqual(str_check_2, str(self.ll))


if __name__ == '__main__':
    unittest.main()
