import cv2
import numpy as np

img = np.arange(0, 640000, 1, np.uint8)
img = np.reshape(img, (800, 800))
w,h = img.shape

for i in range(0,w,100):
    for j in range(0,h,100):
        if ((i+j)/4)%2==0:
            img[i:i+100,j:j+100]=255
        else:
            img[i:i+100,j:j+100]=0

cv2.imshow("output-1",img)
cv2.waitKey()