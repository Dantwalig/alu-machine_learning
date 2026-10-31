#!/usr/bin/env python3
"""Module that calculates the inverse of a matrix"""


def _det(matrix):
    """Determinant of a non-empty square matrix, without validation"""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    total = 0
    for j in range(n):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        total += (-1) ** j * matrix[0][j] * _det(sub)
    return total


def _cofactor(matrix):
    """Cofactor matrix of a non-empty square matrix, without validation"""
    n = len(matrix)
    if n == 1:
        return [[1]]
    result = []
    for i in range(n):
        new_row = []
        for j in range(n):
            sub = [row[:j] + row[j + 1:]
                   for k, row in enumerate(matrix) if k != i]
            new_row.append((-1) ** (i + j) * _det(sub))
        result.append(new_row)
    return result


def inverse(matrix):
    """Calculates the inverse of a matrix

    matrix: list of lists whose inverse should be calculated
    Returns: the inverse of matrix, or None if matrix is singular
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    det = _det(matrix)
    if det == 0:
        return None
    cof = _cofactor(matrix)
    return [[cof[j][i] / det for j in range(n)] for i in range(n)]
