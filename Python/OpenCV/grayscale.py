import cv2

img = cv2.imread('ranz.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('GrayImg', gray)
cv2.imshow('PenghuniAsli', img)
cv2.waitKey()
