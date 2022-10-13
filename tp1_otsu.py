import cv2 as cv
import numpy as np

image = cv.imread("frames_gray/159.png", cv.IMREAD_GRAYSCALE)
ret, thresh = cv.threshold(image, 150, 255, cv.THRESH_OTSU)
print('Threshold (otsu): ', ret)
cv.imshow('Otsu Threshold', thresh)         
       
# De-allocate any associated memory usage         
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows() 