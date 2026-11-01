#!/usr/bin/env python3
"""Module that performs a strided convolution on grayscale images"""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """Performs a convolution on grayscale images

    images: numpy.ndarray of shape (m, h, w) with the grayscale images
    kernel: numpy.ndarray of shape (kh, kw) with the convolution kernel
    padding: tuple (ph, pw), 'same' or 'valid'
    stride: tuple (sh, sw) with the stride for height and width
    Returns: numpy.ndarray with the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride
    if padding == 'valid':
        top = bottom = left = right = 0
    elif padding == 'same':
        top = bottom = int(np.ceil(((h - 1) * sh + kh - h) / 2))
        left = right = int(np.ceil(((w - 1) * sw + kw - w) / 2))
    else:
        top = bottom = padding[0]
        left = right = padding[1]
    padded = np.pad(images, ((0, 0), (top, bottom), (left, right)),
                    mode='constant')
    oh = (h + top + bottom - kh) // sh + 1
    ow = (w + left + right - kw) // sw + 1
    output = np.zeros((m, oh, ow))
    for i in range(oh):
        for j in range(ow):
            patch = padded[:, i * sh:i * sh + kh, j * sw:j * sw + kw]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2))
    return output
