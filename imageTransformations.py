import numpy as np
import cv2 as cv
# translation , Rotation , Flipping , Resizing , Clipping , Cropping

img = cv.imread('Photos/opencv.png')
cv.imshow('Image', img)

# ----------------------------------------------------------------------------

# Translation - shifting an image along the x and y axis, up down left right


def translate(img, x, y):
    translationMatrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translationMatrix, dimensions)


# if we have negative values of x -> translate/shifting image to the left
# if we have negative values of y -> translate/shifting image up
# if we have positive values of x -> translate/shifting image to the right
# if we have positive values of y -> translate/shifting image down

translated = translate(img, 100, 100)
# shifting right by 100px and down by 100px and so on...
cv.imshow('Translated', translated)

# ----------------------------------------------------------------------------

# Rotation


def rotate(img, angle, rotPoint=None):
    # rotPoint means rotating about some point
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
        # rotating wrt center

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated1 = rotate(img, 45)
# rotate by 45 degrees
cv.imshow('Rotated 1', rotated1)
rotated2 = rotate(img, -45)
# rotate by -45 degrees
cv.imshow('Rotated 2', rotated2)
rotated3 = rotate(rotated1, -45)
# rotating a rotated image by 45 degrees
cv.imshow('Rotated 3', rotated3)

# ----------------------------------------------------------------------------

# Resizing an image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# ----------------------------------------------------------------------------

# Flipping an image

flipped = cv.flip(img, 0)
# flipCode can be either 0 or 1 or -1
# 0 means flip image vertically
# 1 mean flip image horizontally
# -1 means flip image both horizontally and vertically
cv.imshow('Flipped', flipped)

# ----------------------------------------------------------------------------

# Cropping

cropped = img[50:200, 100:200]
cv.imshow('Cropped', cropped)

# ----------------------------------------------------------------------------

cv.waitKey(0)