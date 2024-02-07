import unittest
from heap import Heap
from heap_type import HeapType


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()
        self.val_1 = 10
        self.inputs = [[5, 7, 4, 10, 8, 6], [1, 1, 2, 1, 1]]
        self.solutions_max_push = [[10, 8, 6, 5, 7, 4], [2, 1, 1, 1, 1]]
        self.solutions_min_push = [[4, 7, 5, 10, 8, 6], [1, 1, 2, 1, 1]]
        self.solutions_max_pop = [[[10, 8, 6, 5, 7, 4], [8, 7, 6, 5, 4], [7, 5, 6, 4], [6, 5, 4], [5, 4], [4], []],
                                  [[2, 1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1], [1], []]]
        self.solutions_min_pop = [[[4, 7, 5, 10, 8, 6], [5, 7, 6, 10, 8], [6, 7, 8, 10], [7, 10, 8], [8, 10], [10], []],
                                  [[1, 1, 2, 1, 1], [1, 1, 2, 1], [1, 1, 2], [1, 2], [2], []]]

    def test_push(self):
        for heap_type in HeapType:
            self.heap.kind = heap_type
            for i in range(len(self.inputs)):
                for val in self.inputs[i]:
                    self.heap.push(val)
                if self.heap.kind == HeapType.MAX:
                    self.assertEqual(self.heap._heap_arr, self.solutions_max_push[i])
                else:
                    self.assertEqual(self.heap._heap_arr, self.solutions_min_push[i])
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

    @unittest.expectedFailure
    def test_pop_empty(self):
        for heap_type in HeapType:
            self.heap.kind = heap_type
            self.heap.pop()

    def test_pop(self):
        for heap_type in HeapType:
            self.heap.kind = heap_type
            for i in range(len(self.inputs)):
                for val in self.inputs[i]:
                    self.heap.push(val)
                if self.heap.kind == HeapType.MAX:
                    for solution in self.solutions_max_pop[i]:
                        self.assertEqual(self.heap._heap_arr, solution)
                        if not self.heap.is_empty:
                            top = self.heap.pop()
                            self.assertEqual(top, solution[0])
                else:
                    for solution in self.solutions_min_pop[i]:
                        self.assertEqual(self.heap._heap_arr, solution)
                        if not self.heap.is_empty:
                            top = self.heap.pop()
                            self.assertEqual(top, solution[0])


if __name__ == "__main__":
    unittest.main()
