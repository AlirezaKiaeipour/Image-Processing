import cv2

img1 = cv2.imread("Assignment22/a.tif",0)
img2 =cv2.imread("Assignment22/b.tif",0)
img = img2 - img1

cv2.imshow("Decrypt Image",img)
cv2.waitKey()
