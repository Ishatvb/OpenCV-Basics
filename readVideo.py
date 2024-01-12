import cv2 as cv

# *TO READ VIDEOS*

# capture = cv.VideoCapture(0)
# web cam is referenced by integer 0
capture = cv.VideoCapture('Videos/t.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# after capturing the last frame it will break out of loop and raise an cv2 error that is run out of frame
