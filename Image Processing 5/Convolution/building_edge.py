import cv2 as cv
import numpy as np

img = cv.imread("Assignment25/building.tif",0)
resualt1 = np.zeros(img.shape,np.uint8)
resualt2 = np.zeros(img.shape,np.uint8)
mask1 = np.array([[-1,-1,-1],
                [0,0,0],
                [1,1,1]])
mask2 = np.array([[-1,0,1],
                [-1,0,1],
                [-1,0,1]])
row ,col = img.shape
for i in range(1,row-1):
    for j in range(1,col-1):
        small_image = img[i-1:i+2,j-1:j+2]
        res1 = np.sum(mask1*small_image)
        res2 = np.sum(mask2*small_image)
        if res1 <=0:
            res1 = 0
        if res2 <=0:
            res2 = 0

        resualt1[i,j] = res1
        resualt2[i,j] = res2
resualt = np.hstack((resualt1,resualt2))
cv.imshow("Edge Detection",resualt)
cv.waitKey()
