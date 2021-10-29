import cv2

img = cv2.imread("Assignment 21/5.jpg",0)
img = cv2.resize(img,(250,350))
cv2.line(img,(-5,70),(70,-5),(0,0,0),15)
cv2.imshow("output-5",img)
cv2.waitKey()