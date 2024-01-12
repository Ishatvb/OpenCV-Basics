import cv2 as cv
import numpy as np


# to create a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
blank1 = np.zeros((500, 500, 3), dtype='uint8')
blank2 = np.zeros((500, 500, 3), dtype='uint8')
blank3 = np.zeros((500, 500, 3), dtype='uint8')

# dtype ='uint8' , uint8 is a datatype of an image
# 500 = height, 500 = width and 3 = no of color channels
cv.imshow('Blank', blank)

# 1. paint the image a certain color

# Green Colored Image
blank1[:] = 0, 255, 0
cv.imshow('Green Colored Image', blank1)

# Red Colored Image
blank1[:] = 0, 0, 255
cv.imshow('Red Colored Image', blank1)

# Blue Colored Image
blank1[:] = 255, 0, 0
cv.imshow('Blue Colored Image', blank1)

# to color certain range or area of image give it a range
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('color certain area Image', blank)

# to draw a rectangle by cv.rectangle method
cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=2)
cv.imshow('rectangle', blank)

# to fill the shape with color thickness= cv.FILLED or thickness=-1
cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=-1)
cv.imshow('rectangle', blank)

# instead of giving actual coordinates
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow('rectangle', blank)

# instead of actual coordinates
cv.circle(blank2, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=5)
cv.imshow('Circle', blank2)

# to fill color in circle
cv.circle(blank2, (250, 250), 40, (0, 0, 255), thickness=5)
cv.imshow('Circle1', blank2)

# to draw a circle
cv.circle(blank2, (250, 250), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle2', blank2)

# to drwa a line
cv.line(blank2, (0, 0), (250, 250), (255, 255, 255), thickness=5)
cv.imshow('line1', blank2)
cv.line(blank2, (100, 250), (300, 400), (255, 255, 255), thickness=5)
cv.imshow('line2', blank2)

# how to write text on an image
cv.putText(blank3, 'Hello, My name is Ishatv!!!', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank3)

cv.waitKey(0)
