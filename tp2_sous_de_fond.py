
import cv2 as cv
import numpy as np
from tp1_segmentation import seuillage

def enhance_contrast(image):
    lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
    l, a, b = cv.split(lab)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l)

    limg = cv.merge((cl, a, b))
    enhanced_img = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
    return np.hstack((image,enhanced_img))


if __name__ == '__main__':
    video = cv.VideoCapture('tp1.mp4')

    width = video.get(cv.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
    fps = video.get(cv.CAP_PROP_FPS)
    frame_count = video.get(cv.CAP_PROP_FRAME_COUNT)
    r = 1
    T = 96
    idx = 0
    m = []
    while video.isOpened():
        ret, frame = video.read()
        if (idx % r) == 0:
            if ret == True:
                frame = cv.resize(frame, None, fx=0.4, fy=0.4)
                frame = cv.flip(frame, 0)
                frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                #frame = cv.fastNlMeansDenoising(frame, None, 10, 7, 21)
                if idx == 0:
                    B = frame
                    idx += 1
                    continue
                m = cv.subtract(B, frame)
                T, m  = seuillage(m, T)
                print(f'Threshold at frame {idx+1} : ', T)
                B = frame
                
                cv.imshow('Gray scale', m)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        idx += 1
        

    #Release capture
    video.release()
    cv.destroyAllWindows()