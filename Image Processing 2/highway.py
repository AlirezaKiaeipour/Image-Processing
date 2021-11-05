import cv2
import numpy as np
images = []
for i in range(0,19):
    img = cv2.imread(f"Assignment22/highway/h{i}.jpg",0)
    images.append(img)
    row , col = img.shape

res = np.zeros((row,col),dtype="uint8")
for img in images:
    res += img//19

res = cv2.resize(res,(500,500))
cv2.imshow("HighWay",res)
cv2.waitKey()
