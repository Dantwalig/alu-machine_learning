#!/usr/bin/env python3
"""Module that concatenates two numpy.ndarrays along an axis"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two numpy.ndarrays along the given axis"""
    return np.concatenate((mat1, mat2), axis=axis)
