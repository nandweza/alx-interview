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
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Swap columns
    for i in range(n):
        for j in range(n // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - j - 1]
            matrix[i][n - j - 1] = temp
