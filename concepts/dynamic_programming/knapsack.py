"""
Construct a solution array from a given set of items and their respective values and weights
Call the solution array for maximum value with given total weight

TODO Implement call to retrieve indices of elements in knapsack, not just maximum value
"""
from typing import List


def create_knapsack(values: List[int], weights: List[int], capacity: int):
    """
    Create a solution array using dynamic programming to maximize value under capacity
    :param values: item values
    :param weights: item weights
    :param capacity: total capacity of knapsack
    :return: solution_array [int][int]
    """
    solution_array = [[0 for i in range(capacity + 1)] for i in range(len(values) + 1)]
    for i in range(1, len(values) + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                solution_array[i][w] = solution_array[i-1][w]
            else:
                solution_array[i][w] = max(solution_array[i-1][w],
                                           solution_array[i-1][w - weights[i - 1]] + values[i - 1])

    return solution_array


def get_max_value(solution_array: List[List[int]], items: int):
    """
    Return the maximum value in the solutions array for a given amount of items
    :param solution_array: contains solutions to all sub-problems
    :param items: number of items to include in solution
    :return: int, maximum value
    """
    return solution_array[items][-1]
