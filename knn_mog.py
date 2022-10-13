import cv2
import numpy as np
import matplotlib.pyplot as plt

if input('Methode : ') == 'KNN':
    backSub = cv2.createBackgroundSubtractorKNN()
    capture = cv2.VideoCapture("tp1_old.mp4")
    if not capture.isOpened():
        print('Unable to open ')
        exit(0)
    while capture.isOpened():
        ret, frame = capture.read()
        if frame is None:
            break

        frame = cv2.resize(frame, None, fx=0.4, fy=0.4)
        frame = cv2.flip(frame, 0)
        fgMask = backSub.apply(frame)
        cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
        cv2.putText(frame, str(capture.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
        
        
        cv2.imshow('REAL SCENE',frame)
        
        a, result = cv2.threshold(fgMask,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imshow('KNN',result)
        
        keyboard = cv2.waitKey(1) & 0xFF
        if keyboard == 'q':
            break
else :
    backSub = cv2.createBackgroundSubtractorMOG2()
    capture = cv2.VideoCapture("tp1.mp4")
    if not capture.isOpened():
        print('Unable to open ')
        exit(0)
    while capture.isOpened():
        ret, frame = capture.read()
        if frame is None:
            break
        
        frame = cv2.resize(frame, None, fx=0.4, fy=0.4)
        frame = cv2.flip(frame, 0)
        fgMask = backSub.apply(frame)
        cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
        cv2.putText(frame, str(capture.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
        
    
        cv2.imshow('Real scene',frame)
        a, result = cv2.threshold(fgMask,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imshow('MOG2',result)
        
        keyboard = cv2.waitKey(1) & 0xFF
        if keyboard == 'q':
            break