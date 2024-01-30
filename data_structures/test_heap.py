import unittest
from heap import Heap
from heap_type import HeapType


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap(kind=HeapType.MAX)
        self.test_val_1 = 10
        self.test_vals_1 = [5, 7, 4, 10, 8, 6]
        self.test_vals_1_max_heap = [10, 8, 6, 5, 7, 4]
        self.test_vals_1_min_heap = [4, 7, 5, 10, 8, 6]
        self.test_vals_2 = [1, 1, 2, 1, 1]
        self.test_vals_2_max_heap = [2, 1, 1, 1, 1]
        self.test_vals_2_min_heap = [1, 1, 2, 1, 1]

    def test_push(self):
        for val in self.test_vals_1:
            self.heap.push(val)
        self.assertEqual(self.heap._heap_arr, self.test_vals_1_max_heap)
        self.assertEqual(self.heap.size, len(self.test_vals_1))
        self.assertEqual(self.heap.is_empty, False)

        self.heap.reset()
        for val in self.test_vals_2:
            self.heap.push(val)
        self.assertEqual(self.heap._heap_arr, self.test_vals_2_max_heap)
        self.assertEqual(self.heap.size, len(self.test_vals_2))
        self.assertEqual(self.heap.is_empty, False)

    def test_push_min(self):
        self.heap = Heap(HeapType.MIN)
        for val in self.test_vals_1:
            self.heap.push(val)
        self.assertEqual(self.heap._heap_arr, self.test_vals_1_min_heap)
        self.assertEqual(self.heap.size, len(self.test_vals_1))
        self.assertEqual(self.heap.is_empty, False)

        self.heap.reset()
        for val in self.test_vals_2:
            self.heap.push(val)
        self.assertEqual(self.heap._heap_arr, self.test_vals_2_min_heap)
        self.assertEqual(self.heap.size, len(self.test_vals_2))
        self.assertEqual(self.heap.is_empty, False)

    @unittest.expectedFailure
    def test_peek_empty(self):
        self.heap.peek()

    def test_peek(self):
        self.heap.push(self.test_val_1)
        root = self.heap.peek()
        self.assertEqual(root, self.test_val_1)


if __name__ == "__main__":
    unittest.main()
