#!/usr/bin/python3
"""
Pascal triangle Interview question.
"""


def pascal_triangle(n):
    """
    function that returns a lsit of lists of integers.
    representing pascal's triangle of n.
    """

    arr = [[] for i in range(n)]
    if n <= 0:
        return []

    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                arr[i].append(1)
            else:
                arr[i].append(arr[i - 1][j - 1] + arr[i - 1][j])
    return arr
