#!/usr/bin/env python3
"""Module that performs a convolution on grayscale images with padding"""
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """Performs a convolution on grayscale images with custom padding

    images: numpy.ndarray of shape (m, h, w) with the grayscale images
    kernel: numpy.ndarray of shape (kh, kw) with the convolution kernel
    padding: tuple (ph, pw) with the padding for height and width
    Returns: numpy.ndarray with the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), mode='constant')
    oh = h + 2 * ph - kh + 1
    ow = w + 2 * pw - kw + 1
    output = np.zeros((m, oh, ow))
    for i in range(oh):
        for j in range(ow):
            patch = padded[:, i:i + kh, j:j + kw]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2))
    return output
