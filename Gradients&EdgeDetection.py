import cv2 as cv
import numpy as np

img = cv.imread('Photos/london.jpg')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# laplacian placing method
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel method - computes gradient in two directions x and y
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

# combining sobelx and sobel y
combine_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined sobel x and sobel y', combine_sobel)

# canny edge detector
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny ', canny)

cv.waitKey(0)
