import cv2 as cv
import numpy as np

img = cv.imread('Photos/dd.jpg')
cv.imshow('Image', img)

# masking - allows us to focus on certain parts of an image as per our requirement we want to focus.
# eg - In image of people, if we want to focus on their faces we apply masking
#  over people's faces and remove all unwanted parts of image
# using bitwise operators we can perform masking in opencv

blank = np.zeros(img.shape[:2], dtype='uint8')
# Note dimensions of mask have to be at same size as that of the image otherwise it won't work.
cv.imshow('Blank', blank)

mask1 = cv.circle(blank, (230, 210), 100, 255, -1)
cv.imshow('Mask', mask1)

mask2 = cv.rectangle(blank, [350, 150],[550, 340], 255, -1)
cv.imshow('Mask', mask2)

mask3 = cv.circle(blank, (750, 255), 100, 255, -1)
cv.imshow('Mask', mask3)

masked = cv.bitwise_and(img, img, mask=mask1)
cv.imshow('Masked', masked)

cv.waitKey(0)
