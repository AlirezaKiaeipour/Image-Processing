import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser(description="Time Warp Scan Filter v-1.3")
parser.add_argument("-- camera",type=int,help="Please Enter number of your camera",default=0)
parser.add_argument("--output",type=str,help="Please Enter path of output image/  Example: output.jpg",default="time_warp_filter.jpg")
arg = parser.parse_args()

filter = False
cap = cv2.VideoCapture(arg.camera)
pixels_list = []
row=1
while True:
    _,frame = cap.read()
    width , height = frame.shape[:2]
    cv2.putText(frame,"Time Warp Filter and save it:  1",(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"Exit:  0",(10,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),2,cv2.LINE_AA)
    key = cv2.waitKey(1)
    if key==ord("0"):
        break
    if key==ord("1") or filter==True:
        filter = True
        cv2.line(frame,(0,row+4),(height,row+4),(255,0,255),4)
        pixels_list.append(frame[row-1,:])
        frame[:row,:] = pixels_list
        row+=1
        if row>width:
            cv2.imwrite(arg.output,frame)
            row=1
            filter=False
            pixels_list.clear()
    cv2.imshow("Time Warp Scan Filter",frame)

cap.release()
cv2.destroyAllWindows()