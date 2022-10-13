
import cv2 as cv
import numpy as np
from tp1_segmentation import seuillage


if __name__ == '__main__':
    video = cv.VideoCapture('tp1_old.mp4')

    width = video.get(cv.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
    fps = video.get(cv.CAP_PROP_FPS)
    frame_count = video.get(cv.CAP_PROP_FRAME_COUNT)
    r = 50
    T = 96
    idx = 0
    m = []
    while video.isOpened():
        ret, frame = video.read()
        if ret == True:

            if (idx % r) == 0:
                frame = cv.resize(frame, None, fx=0.4, fy=0.4)
                frame = cv.flip(frame, 0)
                frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                #frame = cv.fastNlMeansDenoising(frame, None, 10, 7, 21)
                if idx == 0:
                    B1 = frame
                    idx += 1
                    continue
                if idx == r:
                    B2 = frame
                    idx += 1 
                    continue
                if idx > 2*r:
                        D1 = cv.subtract(B2, B1) 
                        _, D1 = cv.threshold(D1,100,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

                        D2 = cv.subtract(frame, B2)
                        _, D2 = cv.threshold(D2,100,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

                        D = cv.bitwise_and(D1, D2) 

                        D = np.hstack((D, D1, D2))

                        B1 = B2
                        B2 = frame
                        cv.imshow('Gray scale', D)

                        if cv.waitKey(1) & 0xFF == ord('q'):
                            break
        else:
            break
        idx += 1
        

    #Release capture
    video.release()
    cv.destroyAllWindows()