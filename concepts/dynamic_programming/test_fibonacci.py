from fibonacci import naive_fib, dp_fib
import unittest
import timeit


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,
                         10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309,
                         3524578]

    def test_naive_fib(self):
        for n in range(len(self.sequence)):
            exec_time = timeit.timeit(lambda: naive_fib(n), number=1)
            print("Exec Time of naive_fib({n}) : {exec_time}".format(n=n, exec_time=exec_time))
            fib_n = naive_fib(n)
            self.assertEqual(fib_n, self.sequence[n])

    def test_dp_fib(self):
        for n in range(len(self.sequence)):
            exec_time = timeit.timeit(lambda: dp_fib(n), number=1)
            print("Exec Time of dp_fib({n}) : {exec_time}".format(n=n, exec_time=exec_time))
            fib_n = dp_fib(n)
            self.assertEqual(fib_n, self.sequence[n])


if __name__ == "__main__":
    unittest.main()
