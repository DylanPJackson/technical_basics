import unittest
from knapsack import create_knapsack
from knapsack import get_max_value


class TestKnapsack(unittest.TestCase):
    def test_knapsack(self):
        values = [5, 4, 3, 2]
        weights = [4, 3, 2, 1]
        capacity = 6
        off_solution_array = [[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 5, 5, 5],
                              [0, 0, 0, 4, 5, 5, 5],
                              [0, 0, 3, 4, 5, 7, 8],
                              [0, 2, 3, 5, 6, 7, 9]]

        solution_array = create_knapsack(values, weights, capacity)
        print(solution_array)
        self.assertEqual(solution_array, off_solution_array)

        for i in range(len(values), 0, -1):
            max_value = get_max_value(solution_array, i)
            off_max_value = get_max_value(off_solution_array, i)
            self.assertEqual(max_value, off_max_value)


if __name__ == "__main__":
    unittest.main()
