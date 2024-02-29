import cv2

img = cv2.imread('ranz.jpeg')

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('RotateImage90', rotate_90)
cv2.waitKey()
