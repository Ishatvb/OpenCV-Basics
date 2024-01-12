import cv2
import cv2 as cv

img = cv.imread('Photos/peacork.jpg')
cv.imshow('BGR', img)

# converting bgr image to grey scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# how to blur an image
'''bluing removes noise like removing extra elements due to bad lighting, some issues
with camera sensors etc and we can reduce this noise by applying a slight blur '''
# too many bluring techniques :
# Gaussian Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# ksize has to be an odd number
cv.imshow('Gaussian Blur', blur)

# how to create an edge cascade - trying to find edge that are present in the image
canny1 = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges ', canny1)
# to even reduce more number of edges , we can pass blured image
canny2 = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges with blur', canny2)

# how to dilate an image using a specific structuring element
# the structuring element which we're going to use id these canny edges
dilated = cv.dilate(canny2, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding an image - means removing dilation or opposite of dilation
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# how to resize and crop an image
resized1 = cv.resize(img, (500, 500))
cv.imshow('Resized', resized1)
# when you are shrinking the image - smaller from original dimensions
resized2 = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized - shrink', resized2)
# when you are enlarging the image - larger from original dimensions
# interpolation=cv.INTER_CUBIC (slowest, but better quality) or can use interpolation=cv.INTER_LINEAR
resized3 = cv.resize(img, (1600, 2400), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized - enlarged', resized3)

# Cropping - images are arrays and we use array slicing,
# we can select a portion of the images on the basis of pixel values
cropped = img[100:500, 200:400]
cv2.imshow('Cropped', cropped)

cv.waitKey(0)
