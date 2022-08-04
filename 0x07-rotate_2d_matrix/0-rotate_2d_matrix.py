#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

        - Prototype: def rotate_2d_matrix(matrix):
        - Do not return anything. The matrix must be edited in-place.
        - You can assume the matrix will have 2 dimensions and will
          not be empty.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    res = []

    for i in range(cols):
        temp = []

        for j in range(rows):
            temp.append(matrix[j][i])
        res.append(temp[::-1])

    return res
