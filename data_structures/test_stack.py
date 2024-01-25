import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.test_val_1 = 80
        self.test_val_2 = 234
        self.test_val_3 = 45

    def test_create(self):
        str_check_1 = ''
        self.assertEqual(str_check_1, str(self.stack))

    def test_push(self):
        self.stack.push(self.test_val_1)
        str_check_1 = 'Top -> {val_1}'.format(val_1=self.test_val_1)
        self.assertEqual(str_check_1, str(self.stack))
        self.stack.push(self.test_val_2)
        str_check_2 = 'Top -> {val_2} -> {val_1}'.format(val_2=self.test_val_2, val_1=self.test_val_1)
        self.assertEqual(str_check_2, str(self.stack))

    @unittest.expectedFailure
    def test_peek_empty(self):
        self.stack.peek()

    def test_peek(self):
        self.stack.push(self.test_val_1)
        val = self.stack.peek()
        self.assertEqual(val, self.test_val_1)
        self.stack.push(self.test_val_2)
        val = self.stack.peek()
        self.assertEqual(val, self.test_val_2)

    @unittest.expectedFailure
    def test_pop_empty(self):
        self.stack.pop()

    def test_pop(self):
        self.stack.push(self.test_val_1)
        val = self.stack.pop()
        self.assertEqual(val, self.test_val_1)
        str_check_1 = ''
        self.assertEqual(str_check_1, str_check_1)

        self.stack.push(self.test_val_3)
        self.stack.push(self.test_val_2)
        val = self.stack.pop()
        self.assertEqual(val, self.test_val_2)
        str_check_2 = 'Top -> {val_3}'.format(val_3=self.test_val_3)
        self.assertEqual(str_check_2, str(self.stack))
