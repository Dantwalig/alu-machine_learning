#!/usr/bin/env python3
"""Module that represents a Multivariate Normal distribution"""
import numpy as np


class MultiNormal:
    """Class that represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """Initializes the distribution

        data: numpy.ndarray of shape (d, n) with the data set
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        n = data.shape[1]
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        centered = data - self.mean
        self.cov = np.matmul(centered, centered.T) / (n - 1)

    def pdf(self, x):
        """Calculates the PDF at a data point

        x: numpy.ndarray of shape (d, 1) with the data point
        Returns: the value of the PDF
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.cov.shape[0]
        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))
        diff = x - self.mean
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        exponent = -0.5 * np.matmul(np.matmul(diff.T, inv), diff)[0][0]
        norm = 1 / np.sqrt(((2 * np.pi) ** d) * det)
        return norm * np.exp(exponent)
