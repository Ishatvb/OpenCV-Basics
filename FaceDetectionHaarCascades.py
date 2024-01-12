import cv2 as cv

# face detection is nearly detecting presence of any face in an image
# while face recognition involves identifying the face whose face it is

# usually face detection is performed using classifiers ,
# A classifier is an algorithm that decides whether given image is positive or negative,
# i.e., whether a face is present or not
# now a classifier needs to be trained on thousands of image with and without faces
# opencv already comes with a lot of pretrained classifiers that we can use in any program
# so two main classifiers exist today are haar cascades and more advanced classifiers called local binary patterns.
# more advanced classifier - local binary patterns are not prone to noise in an image as compared to haar cascades.

img = cv.imread('Photos/f.jpg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale image', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=11)
print(f'Number of faces found = {len(faces_rect)}')

for x,y,w,h in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', img)

# haar_cascade is very sensitive to noise anything which looks like face it will detect it
# so to minimize the sensitivity to noise we can modiefy the scale factor in minimum neighbors.
# so haar cascades are not that effective but popular we don't we haar in advanced computer vision
# for advanced computer vision projects dealings face recognizer is more effective and less sensitive to noise then opencv haar cascades


cv.waitKey(0)
