import cv2
import numpy as np

img1 = cv2.imread("Assignment22/pic/1.jpg",0)
img2 = cv2.imread("Assignment22/pic/2.jpg",0)
img1 = cv2.resize(img1,(200,300))
img2 = cv2.resize(img2,(200,300))
res1 = img1//2 + img2//8
res2 = img1//2 + img2//4
res3 = img1//2 + img2//2
res4 = img1//4 + img2//2
res5 = img1//8 + img2//2

res = np.concatenate((img1,res1,res2,res4,res5,img2),axis=1)
cv2.imshow("Photo_Merge",res)
cv2.waitKey()