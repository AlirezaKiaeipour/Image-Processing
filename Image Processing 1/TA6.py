import cv2
import numpy as np
img = np.arange(0, 62500, 1, np.uint8)
img = np.reshape(img, (250,250))
w,h = img.shape
for i in range(w):
        img[i:i+1,:]=255-i
        
cv2.imshow("output-6",img)
cv2.waitKey()