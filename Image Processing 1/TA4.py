import cv2

img = cv2.imread("Assignment 21/4.jpg",0)
img = cv2.resize(img,(600,400))
width,height = img.shape
for i in range(width):
    for j in range(height):
        if 250 > img[i,j] > 190 :
            img[i,j]=190
        elif 189 > img[i,j] > 130:
            img[i,j] = 150
        elif 129 > img[i,j] > 110:
            img[i,j] = 120
        else:img[i,j] = 0
        
cv2.imshow("output-4",img)
cv2.waitKey()