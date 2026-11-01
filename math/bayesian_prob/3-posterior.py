#!/usr/bin/env python3
"""Module that calculates the posterior probability given the data"""
import numpy as np


def likelihood(x, n, P):
    """Calculates the likelihood of obtaining the data x and n

    x: number of patients that develop severe side effects
    n: total number of patients observed
    P: 1D numpy.ndarray of hypothetical probabilities of side effects
    Returns: 1D numpy.ndarray with the likelihood for each probability in P
    """
    comb = 1
    for i in range(1, x + 1):
        comb = comb * (n - x + i) // i
    return float(comb) * (P ** x) * ((1 - P) ** (n - x))


def posterior(x, n, P, Pr):
    """Calculates the posterior probability of each P given x and n

    x: number of patients that develop severe side effects
    n: total number of patients observed
    P: 1D numpy.ndarray of hypothetical probabilities of side effects
    Pr: 1D numpy.ndarray of the prior beliefs of P
    Returns: 1D numpy.ndarray with the posterior probability of each P
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    inter = likelihood(x, n, P) * Pr
    return inter / np.sum(inter)
