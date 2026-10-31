#!/usr/bin/env python3
"""Module that calculates the determinant of a matrix"""


def determinant(matrix):
    """Calculates the determinant of a matrix

    matrix: list of lists whose determinant should be calculated
    Returns: the determinant of matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    total = 0
    for j in range(n):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        total += (-1) ** j * matrix[0][j] * determinant(sub)
    return total
