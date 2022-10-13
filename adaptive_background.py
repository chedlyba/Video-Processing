import cv2 as cv
import numpy as np

if __name__ == '__main__':
    video = cv.VideoCapture('tp1.mp4')

    width = video.get(cv.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
    fps = video.get(cv.CAP_PROP_FPS)
    frame_count = video.get(cv.CAP_PROP_FRAME_COUNT)
    r = 2
    T = 96
    idx = 0
    m = []
    alpha = 0.9
    while video.isOpened():
        ret, frame = video.read()
        if (idx % r) == 0:
            if ret == True:
                frame = cv.resize(frame, None, fx=0.4, fy=0.4)
                frame = cv.flip(frame, 0)
                frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                if idx == 0:
                    B = frame
                    idx += 1
                    continue
                m = cv.subtract(frame, B)
                B = cv.addWeighted(frame, alpha, B, 1-alpha, 0.0)
                T, m = cv.threshold(m,100,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
                
                print(f'Threshold at frame {idx+1} : ', T)

                
                cv.imshow('Gray scale', m)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        idx += 1
        

    #Release capture
    video.release()
    cv.destroyAllWindows()