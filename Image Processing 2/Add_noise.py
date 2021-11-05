import cv2
import numpy as np
import random

img = np.zeros((500,500),dtype="uint8")
for i in range(1000):
    a = random.randint(1,500)
    b = random.randint(1,500)
    img[a:a+1,b:b+1]=random.randint(100,225)
cv2.imshow("Add noise to image",img)
cv2.waitKey()



