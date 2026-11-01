#!/usr/bin/env python3
"""Module that represents a normal distribution"""


class Normal:
    """Class that represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes the distribution

        data: list of data used to estimate the distribution
        mean: mean of the distribution
        stddev: standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Calculates the PDF for a given x-value"""
        pi = 3.1415926536
        e = 2.7182818285
        z = self.z_score(x)
        return e ** (-0.5 * z ** 2) / (self.stddev * (2 * pi) ** 0.5)

    def cdf(self, x):
        """Calculates the CDF for a given x-value"""
        pi = 3.14159265359
        t = (x - self.mean) / (self.stddev * 2 ** 0.5)
        erf = (2 / pi ** 0.5) * (t - t ** 3 / 3 + t ** 5 / 10 -
                                 t ** 7 / 42 + t ** 9 / 216)
        return 0.5 * (1 + erf)
