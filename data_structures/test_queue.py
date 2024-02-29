import unittest
from basic_queue import BasicQueue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = BasicQueue()
        self.val_1 = 80
        self.val_2 = 234
        self.val_3 = 45
        self.items = [self.val_1, self.val_2, self.val_3]

    def test_creation(self):
        str_check_1 = ''
        self.assertEqual(str_check_1, str(self.queue))

    def test_is_empty(self):
        empty = self.queue.is_empty
        self.assertTrue(empty)

        self.queue.enqueue(self.val_1)
        empty = self.queue.is_empty
        self.assertFalse(empty)

        self.queue.dequeue()
        empty = self.queue.is_empty
        self.assertTrue(empty)

    def test_enqueue(self):
        self.queue.enqueue(self.val_1)
        str_check_1 = 'Head -> {val_1}'.format(val_1=self.val_1)
        self.assertEqual(str_check_1, str(self.queue))
        self.queue.enqueue(self.val_2)
        str_check_2 = 'Head -> {val_1} -> {val_2}'.format(val_1=self.val_1, val_2=self.val_2)
        self.assertEqual(str_check_2, str(self.queue))

    def test_enqueue_list(self):
        self.queue.enqueue_list(self.items)
        str_check_1 = 'Head -> {} -> {} -> {}'.format(self.val_1, self.val_2, self.val_3)
        self.assertEqual(str_check_1, str(self.queue))

    @unittest.expectedFailure
    def test_dequeue_empty(self):
        self.queue.dequeue()

    def test_dequeue(self):
        self.queue.enqueue(self.val_1)
        self.queue.dequeue()
        str_check_1 = ''
        self.assertEqual(str_check_1, str(self.queue))

        self.queue.enqueue(self.val_1)
        self.queue.enqueue(self.val_2)
        dq_val = self.queue.dequeue()
        self.assertEqual(self.val_1, dq_val)

    @unittest.expectedFailure
    def test_peek_empty(self):
        self.queue.peek()

    def test_peek(self):
        self.queue.enqueue(self.val_1)
        p_val = self.queue.peek()
        self.assertEqual(p_val, self.val_1)
        self.queue.enqueue(self.val_2)
        p_val = self.queue.peek()
        self.assertEqual(p_val, self.val_1)
        self.queue.dequeue()
        p_val = self.queue.peek()
        self.assertEqual(p_val, self.val_2)


if __name__ == "__main__":
    unittest.main()
