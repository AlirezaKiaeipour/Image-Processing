import cv2
import numpy as np

images =[]
for i in range(1,6):
    img = cv2.imread(f"Assignment22/blackhole/1/{i}.jpg",0)
    images.append(img)
    row , col = img.shape
res1 = np.zeros((row,col),dtype="uint8")
for image in images:
    res1 += image//5

images.clear()
for i in range(1,6):
    img = cv2.imread(f"Assignment22/blackhole/2/{i}.jpg",0)
    images.append(img)
res2 = np.zeros((row,col),dtype="uint8")
for image in images:
    res2 += image//5

images.clear()
for i in range(1,6):
    img = cv2.imread(f"Assignment22/blackhole/3/{i}.jpg",0)
    images.append(img)
res3 = np.zeros((row,col),dtype= "uint8")
for image in images:
    res3 += image//5

images.clear()
for i in range(1,6):
    img = cv2.imread(f"Assignment22/blackhole/4/{i}.jpg",0)
    images.append(img)
res4 = np.zeros((row,col),dtype="uint8")
for image in images:
    res4 += image//5

resualt1 = np.concatenate((res1,res2),axis=1)
resualt2 = np.concatenate((res3,res4),axis=1)
resualt = np.concatenate((resualt1,resualt2),axis=0)
resualt = cv2.resize(resualt,(500,500))
cv2.imshow("Noise Reduction",resualt)
cv2.waitKey()