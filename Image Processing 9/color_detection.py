import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(650,650))
    row ,col = frame.shape[:2]
    frame_blur = cv2.blur(frame,(30,30))
    frame_rectangle = frame[row//2-50:row//2+50,col//2-50:col//2+50]
    cv2.rectangle(frame_blur,(row//2-50,col//2-50),(row//2+50,col//2+50),(0,255,0),4)
    frame_blur[row//2-50:row//2+50,col//2-50:col//2+50] = frame_rectangle
    mean_color_R = int(np.mean(frame_rectangle[:,:,2]))
    mean_color_G = int(np.mean(frame_rectangle[:,:,1]))
    mean_color_B = int(np.mean(frame_rectangle[:,:,0]))
    
    if mean_color_B>150 and mean_color_G>150 and mean_color_R>150:
        color = "White"
    elif 70<mean_color_B<=150 and 70<mean_color_G<=150 and 70<mean_color_R<=150:
        color = "Gray"
    elif mean_color_B<=70 and mean_color_G<=70 and mean_color_R<=70:
        color="Black"
    elif mean_color_R>180 and mean_color_G<40 and mean_color_B<40:
        color="Red"
    elif mean_color_R<50 and mean_color_G>160 and mean_color_B<50:
        color="Green"
    elif mean_color_R<50 and mean_color_G<50 and mean_color_B>180:
        color = "Blue"
    elif mean_color_R>150 and mean_color_G<50 and mean_color_B>150:
        color="Purple"
    elif mean_color_R>150 and mean_color_G>150 and mean_color_B<50:
        color="Yellow"
    elif mean_color_R<50 and mean_color_G>150 and mean_color_B>150:
        color = "Cyan"

    cv2.putText(frame_blur,f"R: {str(mean_color_R)}, G: {str(mean_color_G)}, B: {str(mean_color_B)}",(10,40),cv2.FONT_HERSHEY_COMPLEX,0.75,(0,0,0),2)
    cv2.putText(frame_blur,f"Color: {color}",(10,70),cv2.FONT_HERSHEY_COMPLEX,0.75,(0,0,0),2)  
    cv2.imshow("frame",frame_blur)
    if cv2.waitKey(1) & 0xFF==ord("0"):
        break

cap.release()
cv2.destroyAllWindows()
