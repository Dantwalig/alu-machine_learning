#!/usr/bin/env python3
"""Module that performs a valid convolution on grayscale images"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Performs a valid convolution on grayscale images

    images: numpy.ndarray of shape (m, h, w) with the grayscale images
    kernel: numpy.ndarray of shape (kh, kw) with the convolution kernel
    Returns: numpy.ndarray with the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    oh = h - kh + 1
    ow = w - kw + 1
    output = np.zeros((m, oh, ow))
    for i in range(oh):
        for j in range(ow):
            patch = images[:, i:i + kh, j:j + kw]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2))
    return output
