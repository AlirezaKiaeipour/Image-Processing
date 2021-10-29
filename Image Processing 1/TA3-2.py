import cv2

image = cv2.imread("Assignment 21/3.jpg",0)
img = cv2.resize(image,(500,500))
img = img[::-1,::-1]
cv2.imshow("output-3",img)
cv2.waitKey()
