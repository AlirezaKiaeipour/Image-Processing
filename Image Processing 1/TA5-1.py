import cv2

img = cv2.imread("Assignment 21/5.jpg",0)
img = cv2.resize(img,(250,350))
w,h = img.shape
for i in range(70):
    for j in range(70):
        if ((i+j)/35)%2==0:
            img[i-1:i+8,j-1:j+8]=0

cv2.imshow("output-5",img)
cv2.waitKey()