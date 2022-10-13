import cv2 as cv
import numpy as np
from tp1_segmentation import seuillage

video = cv.VideoCapture('tp1.mp4')

width = video.get(cv.CAP_PROP_FRAME_WIDTH)
height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv.CAP_PROP_FPS)
frame_count = video.get(cv.CAP_PROP_FRAME_COUNT)

idx = 0
while video.isOpened():
    ret, frame = video.read()
    if ret == True:
        frame = cv.resize(frame, None, fx=0.3, fy=0.3)
        frame = cv.flip(frame, 0)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #T, frame = seuillage(frame, 150) 
        #ret, thresh = cv.threshold(image, 150, 255, cv.THRESH_OTSU)

        cv.imshow('Gray scale', frame)
        idx += 1
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
         break

#Release capture
video.release()
cv.destroyAllWindows()