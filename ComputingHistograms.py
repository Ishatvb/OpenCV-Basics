import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/london.jpg')
cv.imshow('Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')



# histograms allow us to visualize the distribution of pixel intensities in an image.
# whether it is color image or a gray scale image we can visualize thse pixel intensity distributions with the help of histogram

# Histogram for Grayscale Images

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# mask1 = cv.circle(blank, (580, 360), 80, 255, -1)
# masked = cv.bitwise_and(gray, gray, mask=mask1)
# cv.imshow('Masked', masked)

#  without mask
# gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
#  with mask
# gray_hist = cv.calcHist([gray], [0], mask1, [256], [0, 256])

# plt.figure()
# plt.title('Grayscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Histogram for RGB Images

mask2 = cv.circle(blank, (580, 360), 80, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask2)
cv.imshow('Masked', masked)

plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv.calcHist([img], [i], mask2, [256],[0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
