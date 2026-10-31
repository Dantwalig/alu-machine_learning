#!/usr/bin/env python3
"""Module that calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial

    poly: list of coefficients, the index is the power of x
    Returns: a new list with the coefficients of the derivative,
    or None if poly is not valid
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    for coef in poly:
        if not isinstance(coef, (int, float)) or isinstance(coef, bool):
            return None
    result = [i * poly[i] for i in range(1, len(poly))]
    if all(coef == 0 for coef in result):
        return [0]
    return result
