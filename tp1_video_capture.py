import cv2 
from tp2_sous_de_fond import enhance_contrast

if __name__=='__main__':
    video = cv2.VideoCapture('tp1.mp4')

    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    print(f'Height : {height}\nWidth : {width}\nfps : {fps}\nFrame count : {frame_count}')

    idx = 0
    ## PLAY VIDEO AND SAVE FRAMES EVERY 50ms:
    while video.isOpened():
        ret, frame = video.read()
        sec = video.get(cv2.CAP_PROP_POS_FRAMES)
        if ret == True:
            if sec % 50 == 0:
                frame = cv2.flip(frame,0)
                frame = cv2.resize(frame, None, fx=0.4, fy=0.4)
                frame = enhance_contrast(frame)
                cv2.imwrite(f'frames/{idx}.png',frame)
                idx += 1
                cv2.imshow('TP1',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        else:
            break

    #Release capture
    video.release()
    cv2.destroyAllWindows()

