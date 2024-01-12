import cv2 as cv
import matplotlib.pyplot as plt

# matplotlib uses RGB whereas openCV uses BGR format

img = cv.imread('Photos/london.jpg')
cv.imshow('Image', img)

# in matplotlib
plt.imshow(img)
plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BRG TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR TO L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# in matplotlib
plt.imshow(rgb)
plt.show()

#  we can convert Grayscale to BGR, HSV to BGR ,BGR to Lab,  RGB to BGR etc.
# but we cannot convert Grayscale to HSV, Grayscale to Lab, etc. directly , we have to convert to BGR first.

# HSV TO BGR
bgr1 = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv --> BGR', bgr1)

# Lab TO BGR
bgr2 = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
cv.imshow('lab --> BGR', bgr2)

cv.waitKey(0)
