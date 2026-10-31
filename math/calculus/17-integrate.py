#!/usr/bin/env python3
"""Module that calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial

    poly: list of coefficients, the index is the power of x
    C: integer integration constant
    Returns: a new list with the coefficients of the integral,
    or None if poly or C are not valid
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    for coef in poly:
        if not isinstance(coef, (int, float)) or isinstance(coef, bool):
            return None
    if not isinstance(C, int) or isinstance(C, bool):
        return None
    result = [C]
    for i in range(len(poly)):
        value = poly[i] / (i + 1)
        if value == int(value):
            value = int(value)
        result.append(value)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result
