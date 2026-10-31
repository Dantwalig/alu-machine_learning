#!/usr/bin/env python3
"""Module that calculates the definiteness of a matrix"""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix

    matrix: numpy.ndarray of shape (n, n) whose definiteness is calculated
    Returns: Positive definite, Positive semi-definite,
    Negative semi-definite, Negative definite or Indefinite,
    or None if matrix is not valid or fits none of those categories
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None
    if matrix.shape[0] == 0:
        return None
    if not np.array_equal(matrix, matrix.T):
        return None
    eigenvalues = np.linalg.eigvalsh(matrix)
    eigenvalues[np.isclose(eigenvalues, 0)] = 0
    if np.all(eigenvalues > 0):
        return "Positive definite"
    if np.all(eigenvalues < 0):
        return "Negative definite"
    if np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    if np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    return "Indefinite"
