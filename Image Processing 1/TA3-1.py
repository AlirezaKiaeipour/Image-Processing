import cv2

image = cv2.imread("Assignment 21/3.jpg",0)
img = cv2.resize(image,(400,280))
img = cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow("output-3",img)
cv2.waitKey()
