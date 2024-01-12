import cv2 as cv

# we can a binary image from a regular standalone image
# By setting a threshold value, pixel values below threshold value becomes 0
# and pixel values above threshold values become 255

img = cv.imread('Photos/dog.jpg')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray)

# simple thresholding
# Thresh is binarized image or threshold image
# and threshold is same value that we have passed (150)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple threshold image', thresh)

# inverse threshold image

threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple threshold inverse image', thresh_inverse)


# We get different images with different threshold values
# downside : we have to manually specify specific threshold value
# in some cases this might work but in more advance cases won't work
# we can let the computer find the optimal threshold value by itself to binarize the image - adaptive

# Adaptive thresholding
# block size of kernel size opencv need to find the mean to find the optimal threshold value
# c value is integer that is subtracted from the mean that allow us to fine tune our threshold

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Mean Adaptive thresholding', adaptive_thresh)

# inverse threshold image
adaptive_thresh_inverse = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Mean Adaptive thresholding inverse', adaptive_thresh_inverse)

# we don't have to stick with mean we can change that , example gaussian -
# it add a weight to each pixel value and then computed the mean across those pixels
# ,so we get a better image as compared to mean
# but this depends on situations, in some cases mean works better and in some cases gaussian works better.

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Gaussian Adaptive thresholding', adaptive_thresh)

# inverse threshold image
adaptive_thresh_inverse = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Gaussian Adaptive thresholding inverse', adaptive_thresh_inverse)


cv.waitKey(0)
