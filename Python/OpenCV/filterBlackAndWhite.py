import cv2

img = cv2.imread('ranz.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

(thresh, blackAndWhiteImage) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imshow('BlackWhiteImage', blackAndWhiteImage)
cv2.waitKey()
