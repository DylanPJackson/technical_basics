import unittest
from heap import Heap
from heap_type import HeapType


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()
        self.val_1 = 10
        self.inputs = [[5, 7, 4, 10, 8, 6], [1, 1, 2, 1, 1]]
        self.inputs_solutions_max = [[10, 8, 6, 5, 7, 4], [2, 1, 1, 1, 1]]
        self.inputs_solutions_min = [[4, 7, 5, 10, 8, 6], [1, 1, 2, 1, 1]]

    def test_push(self):
        for heap_type in HeapType:
            self.heap.kind = heap_type
            for i in range(len(self.inputs)):
                for val in self.inputs[i]:
                    self.heap.push(val)
                if self.heap.kind == HeapType.MAX:
                    self.assertEqual(self.heap._heap_arr, self.inputs_solutions_max[i])
                else:
                    self.assertEqual(self.heap._heap_arr, self.inputs_solutions_min[i])
                self.assertEqual(self.heap.size, len(self.inputs[i]))
                self.assertEqual(self.heap.is_empty, False)
                self.heap.empty()

    @unittest.expectedFailure
    def test_peek_empty(self):
        for heap_type in HeapType:
            self.heap.kind = heap_type
            self.heap.peek()
            self.heap.empty()

    def test_peek(self):
        for heap_type in HeapType:
            self.heap.kind = heap_type
            self.heap.push(self.val_1)
            root = self.heap.peek()
            self.assertEqual(root, self.val_1)
            self.heap.empty()


if __name__ == "__main__":
    unittest.main()
