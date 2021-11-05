import cv2

img1 = cv2.imread("Assignment22/origin.bmp",0)
img2 = cv2.imread("Assignment22/test.bmp",0)
img2 = cv2.flip(img2,1)

img = cv2.subtract(img2,img1)*10
img = cv2.resize(img ,(500,500))
cv2.imshow("Troubleshooting board",img)
cv2.waitKey()