import cv2
import numpy as np


def gamma_correction(src, gamma):

    # output pixel value [0,255] = (i/255)^(1/gamma) * 255
    gamma = 1 / gamma
    table = [((i / 255) ** gamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    # For each pixel value in the range [0, 255] is calculated
    # corresponding gamma corrected value.
    # OpenCV provides LUT function which performs a lookup table transform.
    return cv2.LUT(src, table)
    # γ - gamma that controls image brightness.
    # If gamma < 1 then image will be darker,
    # if gamma > 1 then image will be lighter.
    # A gamma = 1 has no effect.


img = cv2.imread('image7.jpg')
new_img1 = gamma_correction(img, 2.2)
cv2.imwrite('new1_image7.jpg', new_img1)
new_img2 = gamma_correction(img, 1.5)
cv2.imwrite('new2_image7.jpg', new_img2)
new_img3 = gamma_correction(img, 0.5)
cv2.imwrite('new3_image7.jpg', new_img3)
