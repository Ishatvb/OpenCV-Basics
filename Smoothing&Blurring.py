import cv2 as cv
import numpy as np

# we smooth an image when it has a lot of noise,
# that is caused from camera sensors and inefficient lighting
# we can smooth the image or remove noise by applying some blur

img = cv.imread('Photos/dog.jpg')
cv.imshow('Image', img)


# Averaging blur method - In this (Kernel size) takes average of surrounding pixel intensity
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian blur method - Instead of computing average of surrounding pixel intensity, each surrounding pixel is given a particular weight
# and it is more natural as compared to average blur
Gauss = cv.GaussianBlur(img,(3,3), 0)
cv.imshow('Gaussian Blur', Gauss)

# Median blur method - Instead of computing average of surrounding pixel intensity,it finds median of surrounding pixels
# Median is more effective in reducing noise as compared to average and even gaussian blur.
# very good at removing salt and pepper noise that is existing in image - reduction in substantial amount of noise
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral bluring - mostly used in computer vision projects
# in traditional blurring methods we blur image without caring about reducing edges in the image or not
# But in Bilateral blurring applies bluring but it retain the edges in the image
# d is diameter not kernel size
bilateral = cv.bilateralFilter(img, 25,15, 50)
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)