import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (380, 380), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND - take rectangle and circle, and returns intersection of both of them
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR - take rectangle and circle, and returns union of both of them
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR - take rectangle and circle, and returns non - intersecting regions or complement of intersection of both of them
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise Not - take rectangle or circle, and it inverts the binary color
bitwise_not_rectangle= cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT - rectangle', bitwise_not_rectangle)
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT - circle', bitwise_not_circle)

cv.waitKey(0)
