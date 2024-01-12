import cv2 as cv

# *TO READ IMAGES*
img = cv.imread('Photos/cat.jpg')

cv.imshow('cat', img)

cv.waitKey(0)
