#!/usr/bin/env python3
"""Module that performs a convolution on images using multiple kernels"""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Performs a convolution on images using multiple kernels

    images: numpy.ndarray of shape (m, h, w, c) with the images
    kernels: numpy.ndarray of shape (kh, kw, c, nc) with the kernels
    padding: tuple (ph, pw), 'same' or 'valid'
    stride: tuple (sh, sw) with the stride for height and width
    Returns: numpy.ndarray with the convolved images
    """
    m, h, w, c = images.shape
    kh, kw, _, nc = kernels.shape
    sh, sw = stride
    if padding == 'valid':
        top = bottom = left = right = 0
    elif padding == 'same':
        total_h = max((-(-h // sh) - 1) * sh + kh - h, 0)
        total_w = max((-(-w // sw) - 1) * sw + kw - w, 0)
        bottom = total_h // 2
        top = total_h - bottom
        right = total_w // 2
        left = total_w - right
    else:
        top = bottom = padding[0]
        left = right = padding[1]
    padded = np.pad(images, ((0, 0), (top, bottom), (left, right), (0, 0)),
                    mode='constant')
    oh = (h + top + bottom - kh) // sh + 1
    ow = (w + left + right - kw) // sw + 1
    output = np.zeros((m, oh, ow, nc))
    for i in range(oh):
        for j in range(ow):
            for k in range(nc):
                patch = padded[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
                output[:, i, j, k] = np.sum(patch * kernels[:, :, :, k],
                                            axis=(1, 2, 3))
    return output
