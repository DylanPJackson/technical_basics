"""
Implementation of fibonacci sequence using dynamic programming

Fibonacci sequence
0 1 1 2 3 5 8 13 21 34
In other words, index 0 and 1 are default at 0 and 1.
Besides that, Fib(n) = Fib(n-1) + Fib(n-2)
We store all sub problems in memo so that we only compute each entry once, whereas the naive recursive solution
    computes every entry every time.
"""


def naive_fib(n: int):
    """
    Naively compute fibonacci number for given n using recursion
    :param n: nth fibonacci number to generate
    :return: int, fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return naive_fib(n-1) + naive_fib(n-2)


def dp_fib(n: int):
    """
    Compute fibonacci number using dynamic programming
    :param n: nth fibonacci number to generate
    :return: int, fibonacci number
    """
    memo = {0: 0, 1: 1}
    for sub_n in range(2, n + 1):
        memo[sub_n] = memo[sub_n - 1] + memo[sub_n - 2]

    return memo[n]
