#!/usr/bin/env python3
"""Module that represents an exponential distribution"""


class Exponential:
    """Class that represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Initializes the distribution

        data: list of data used to estimate the distribution
        lambtha: expected number of occurences in a given time frame
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            total = 0
            for value in data:
                total += value
            self.lambtha = float(len(data) / total)

    def pdf(self, x):
        """Calculates the PDF for a given time period x"""
        if x < 0:
            return 0
        e = 2.7182818285
        return self.lambtha * e ** (-self.lambtha * x)

    def cdf(self, x):
        """Calculates the CDF for a given time period x"""
        if x < 0:
            return 0
        e = 2.7182818285
        return 1 - e ** (-self.lambtha * x)
