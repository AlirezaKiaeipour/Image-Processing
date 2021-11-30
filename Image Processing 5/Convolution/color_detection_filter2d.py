import cv2 as cv
import numpy as np

mask = np.ones((71,71)) / 5041
cap = cv.VideoCapture(0)
while True:
    _,frame = cap.read()
    frame = cv.resize(frame,(600,600))
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    frame = cv.equalizeHist(frame)
    row ,col = frame.shape

    resualt = cv.filter2D(frame,0,mask)
    frame_rectangle = frame[row//2:row//2+100,col//2:col//2+100]
    cv.rectangle(resualt,(row//2,col//2),(row//2+100,col//2+100),(0,255,0),4)
    resualt[row//2:row//2+100,col//2:col//2+100] = frame_rectangle
    
    mean_color = int(np.mean(frame_rectangle))
    if mean_color <=80:
        color = "Black"
    elif 80< mean_color <=150:
        color = "Gray"
    elif mean_color > 150:
        color = "White"

    cv.putText(resualt,f"Colors Mean: {str(mean_color)}",(10,40),cv.FONT_HERSHEY_COMPLEX,0.75,(0,0,0),2)
    cv.putText(resualt,f"Color: {color}",(10,70),cv.FONT_HERSHEY_COMPLEX,0.75,(0,0,0),2)
    cv.putText(resualt,"Less than 80 is black",(10,col-20),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    cv.putText(resualt,"Between 80 to 150 is gray",(10,col-40),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    cv.putText(resualt,"Above 150 is white",(10,col-60),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    cv.imshow("Color Detection",resualt)
    if cv.waitKey(1) & 0xFF==ord("0"):
        break