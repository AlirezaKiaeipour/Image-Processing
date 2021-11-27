import cv2 as cv
import numpy as np

img = cv.imread("Assignment25/cat.jpg",0)
img = cv.resize(img,(0,0),fx=0.25,fy=0.25)

def convolution(size):
    resualt = np.zeros(img.shape,np.uint8)
    mask = np.ones((size,size)) / size **2
    row ,col = img.shape
    for i in range(size//2,row-size//2):
        for j in range(size//2,col-size//2):
            small_image = img[i-size//2:i+size//2+1,j-size//2:j+size//2+1]
            resualt[i,j] = np.sum(small_image*mask)
    return resualt

resualt1 = convolution(3)
resualt2 = convolution(5)
resualt3 = convolution(7)
resualt4 = convolution(15)
resualt = np.hstack((resualt1,resualt2,resualt3,resualt4))

cv.imshow("convolution",resualt)
cv.waitKey()