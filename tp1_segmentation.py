import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def seuillage(image, T):
    hist = cv.calcHist([image], [0], None, [256], [0,256])
    c = 1
    idx = np.arange(0,256,1)
    while c !=0:
        G1 = hist[T:-1]
        G2 = hist[0:T]

        m1 = np.dot(idx[T:-1], G1)/np.sum(G1)
        m2 = np.dot(idx[0:T], G2)/np.sum(G2)

        c = T - int((m1+m2)/2)
        T = int((m1+m2)/2)
    res_image = np.where( image > T , np.uint8(255), np.uint8(0))
    return T, res_image


if __name__ == '__main__':
    image = cv.imread("frames_gray/0.png", cv.IMREAD_GRAYSCALE)

    T = 128
    T, res_image = seuillage(image, T)
    print('Threshold (seuillage global):', T)
    cv.imshow('Seuillage Global', res_image)
    cv.waitKey(0)