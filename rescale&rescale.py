import cv2 as cv

''' we resize and rescale images and videos to prevent computational strain.
large media files tend to store a lot of information in it and displaying it
 takes a lot of processing. 
 So by resizing and rescaling we are actually trying to get rid of that information.
 rescaling a video means modifying its height and width to a particular height and width.
 Generally it is good practice to downscale height and width to smaller value as compared to original dimensions.
 as most cameras do not support going higher that its maximum capability'''

img = cv.imread('Photos/cat.jpg')
cv.imshow('cat', img)


def rescaleFrame(frame, scale=0.75):
    # this method will work for videos , images and live videos
    # frame.shape[1] is width of image
    width = int(frame.shape[1] * scale)
    # frame.shape[0] is height of image
    height = int(frame.shape[0] * scale)

    dimensions = (width , height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img)
cv.imshow('Image',resized_image)


def changeResolution(width,height):
    # only works for live video , not going to work for video files already exists
    capture.set(3,width)
    capture.set(4,height)


capture = cv.VideoCapture('Videos/t.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()