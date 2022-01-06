import cv2
import numpy as np

lower = np.array([0, 40, 75])
upper = np.array([20, 255, 255])
cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    skin = cv2.inRange(frame_hsv, lower, upper)    

    kernel = np.ones((15,15),np.uint8)
    skin = cv2.dilate(skin,kernel,iterations = 1)
    skin = cv2.bitwise_and(frame, frame,mask=skin)
    cv2.imshow("Skin Detection",skin)
    if cv2.waitKey(1) & 0xFF==ord("0"):
        break
cap.release()
cv2.destroyAllWindows()
