import cv

image = cv.LoadImage('eben.jpg',cv.CV_LOAD_IMAGE_COLOR)

# print some image properties
print 'Depth:',image.depth,'# Channels:',image.nChannels
print 'Size:',image.width,image.height
print 'Pixel values average',cv.Avg(image)

# create the window
cv.NamedWindow('my window', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('my window', image) # show the image
cv.WaitKey() # the window will be closed with a (any)key press

