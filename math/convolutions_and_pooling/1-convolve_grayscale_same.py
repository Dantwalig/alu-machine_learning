#!/usr/bin/env python3
"""Module that performs a same convolution on grayscale images"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """Performs a same convolution on grayscale images

    images: numpy.ndarray of shape (m, h, w) with the grayscale images
    kernel: numpy.ndarray of shape (kh, kw) with the convolution kernel
    Returns: numpy.ndarray with the convolved images, same height and width
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    top = (kh - 1) // 2
    bottom = kh - 1 - top
    left = (kw - 1) // 2
    right = kw - 1 - left
    padded = np.pad(images, ((0, 0), (top, bottom), (left, right)),
                    mode='constant')
    output = np.zeros((m, h, w))
    for i in range(h):
        for j in range(w):
            patch = padded[:, i:i + kh, j:j + kw]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2))
    return output
