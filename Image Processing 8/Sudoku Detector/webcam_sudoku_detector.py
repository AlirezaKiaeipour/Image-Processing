import numpy as np
import cv2

def order_points(point):
        rect = np.zeros((4, 2), dtype = "float32")
        sum_ = point.sum(axis = 1)
        rect[0] = point[np.argmin(sum_)]
        rect[2] = point[np.argmax(sum_)]
        dif = np.diff(point, axis = 1)
        rect[1] = point[np.argmin(dif)]
        rect[3] = point[np.argmax(dif)]
        return rect
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    height , width = frame.shape[:2]
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_blur = cv2.GaussianBlur(frame_gray,(7,7),3)
    frame_thresh = cv2.adaptiveThreshold(frame_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,2)
    contours,_ = cv2.findContours(frame_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=cv2.contourArea,reverse=True)
    cv2.putText(frame,'Save Croped Sudoku:   S',(15,20),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
    cv2.putText(frame,'Exit:   0',(15,50),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)

    sudoku_contour = None
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour,True)
        approx = cv2.approxPolyDP(contour,epsilon,True)
        if len(approx)==4:
            sudoku_contour = approx
            break
    if sudoku_contour is None:
        cv2.putText(frame,'Please Enter correct image',(15,80),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
    else:
        cv2.drawContours(frame,[sudoku_contour],-1,(0,255,0),2)
        cv2.imshow("frame",frame)
        key = cv2.waitKey(1)
        if key==ord("s"):
            src_pts = order_points(sudoku_contour.reshape(4,2))
            dst_pts = np.float32([[0, 0],[width, 0],[width,height],[0,height]])
            transform = cv2.getPerspectiveTransform(src_pts, dst_pts)
            warp = cv2.warpPerspective(frame, transform, (width, height))
            cv2.imwrite("sudoku.jpg",warp)
        if key==ord("0"):
            break

cap.release()
cv2.destroyAllWindows()        


