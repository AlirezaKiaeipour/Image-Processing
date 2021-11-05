import cv2

img = cv2.imread("Assignment22/Mona_Lisa.jpg",0)
img = cv2.resize(img,(500,500))
blurred = cv2.GaussianBlur(img,(21,21),0)
sketch = img / blurred

cv2.imshow("Convert image to painting",sketch)
cv2.waitKey()