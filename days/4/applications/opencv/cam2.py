import cv

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)

def repeat():
    while True:
        frame = cv.QueryFrame(capture)
        cv.ShowImage("w1", frame)
        cv.WaitKey(10)

repeat()
cv.WaitKey(0)

