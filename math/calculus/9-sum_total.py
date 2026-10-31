#!/usr/bin/env python3
"""Module that calculates the sum of squares from 1 to n"""


def summation_i_squared(n):
    """Calculates the sum of i^2 for i from 1 to n

    n: the stopping condition
    Returns: the integer value of the sum, or None if n is not valid
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
