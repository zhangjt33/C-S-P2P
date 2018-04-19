import cv2 as cv
import numpy as np
capture = cv.VideoCapture(0)
while(True):
    ret, frame = capture.read()
    # gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('frame', frame)
    if cv.waitKey & 0xFF == ord('q'):
        break
# print("debug")
# img = cv.imread("a.png")
# cv.imshow("a", img)
# cv.waitKey(10000)
# nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))


# fps = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS)

# wait = int (1/fps * 1000/1)
# duration = (nbFrames * fps) / 1000

# print('Num. Frames = ', nbFrames)
# print('Frame Rate = ', fbs, 'fps')
# print('Duration = ', duration, 'sec')

# for f in xrange(nbFrames):
#     frameImg = cv.QueryFrame(capture)
#     print(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAMES))
#     cv.ShowImage("The Video", frameImg)
#     cv.WaitKey(wait)
# print('Num. Frames = ', nbFrames)
# print('Frame Rate = ', fbs, 'fps')
# print('Duration = ', duration, 'sec')

# for f in xrange(nbFrames):
#     frameImg = cv.QueryFrame(capture)
#     print(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAMES))
#     cv.ShowImage("The Video", frameImg)
#     cv.WaitKey(wait)