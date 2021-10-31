import cv2
import numpy as np
img = np.arange(0, 62500, 1, np.uint8)
img = np.reshape(img, (250,250))
img[:,:] = 255

for i in range(0,60,10):
    img[120-i:130-i,105+(i//2):115+(i//2)]=0
    img[70+i:80+i,135+(i//2):145+(i//2)]=0
img[100:110,125:150] =0       
cv2.imshow("output-7",img)
cv2.waitKey()