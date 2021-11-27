import cv2 as cv
import numpy as np

img = cv.imread("Assignment25/lion.png",0)
img = cv.resize(img,(0,0),fx=0.5,fy=0.5)
resualt = np.zeros(img.shape,np.uint8)
mask = np.array([[0,-1,0],
                [-1,4,-1],
                [0,-1,0]])

row ,col = img.shape
for i in range(1,row-1):
    for j in range(1,col-1):
        small_image = img[i-1:i+2,j-1:j+2]
        res = np.sum(mask*small_image)
        if res<0:
            res=0
        resualt[i,j]=res
cv.imshow("Canny edge",resualt)
cv.waitKey()
