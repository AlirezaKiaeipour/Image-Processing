import cv2

image1 = cv2.imread("Assignment 21/1.jpg",0)
image2 =cv2.imread("Assignment 21/2.jpg",0)

img1 = cv2.resize(image1,(250,250))
img2 = cv2.resize(image2,(220,250))
img1[:,:] = 255-img1[:,:]
img2[:,:] = 255-img2[:,:]

cv2.imshow("output2-1",img1)
cv2.imshow("output2-2",img2)
cv2.waitKey()