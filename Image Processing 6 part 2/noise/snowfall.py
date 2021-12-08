import random
import cv2
import numpy as np
import imageio

snow =[]
arr_random = []
img = cv2.imread("img/snow2.jpg")
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
row , col = img_rgb.shape[:2]

for i in range(1500):
    x = random.randint(0,col)
    y = random.randint(-1000,row)
    s = random.choice([1,2])
    move = random.choice([-3,-2,-1,0,1,2,3])
    down = random.randint(5,10)
    arr_random.append([x,y,s,move,down])

for i in range(row//5):
    img = cv2.imread("img/snow2.jpg")
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    for k,j in enumerate(arr_random): 

        cv2.circle(img_rgb,(j[0],j[1]),j[2],(223, 219, 219),-1)
        j[0] = j[0] + j[3]
        j[1] = j[1] + j[4]
    snow.append(img_rgb)

imageio.mimsave("snow_fall.gif",snow)