import cv

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)


frame = cv.QueryFrame(capture)
cv.ShowImage("w1", frame)

cv.WaitKey(0)


