import cv2 as cv
import numpy as np

img = cv.imread("Assignment25/flower_input.jpg",0)
img = cv.resize(img,(0,0),fx=0.5,fy=0.5)
blur = cv.GaussianBlur(img,(51,51),0)
resualt = np.zeros(img.shape,np.uint8)

row ,col = img.shape
for i in range(2,row-2):
    for j in range(2,col-2):
        small_image = img[i-2:i+3,j-2:j+3]
        small_image_reshape = small_image.reshape(25)
        small_image_reshape_sort = np.sort(small_image_reshape)
        resualt[i,j] = small_image_reshape_sort[12]

for i in range(row):
    for j in range(col):
        if resualt[i,j] > 120:
            blur[i,j] = resualt[i,j]
        
cv.imshow("focus on flower",blur)
cv.waitKey()
