import argparse
import numpy as np
import cv2

parser = argparse.ArgumentParser(description="Sudoku Detector Using Opencv")
parser.add_argument("--input",type=str,help="Please Enter path of input image/  Example: image.jpg")
parser.add_argument("--save",type=str,help="Please Enter path of output image/  Example: output.jpg",default="output.jpg")
arg = parser.parse_args()

def order_points(point):
    rect = np.zeros((4, 2), dtype = "float32")
    sum_ = point.sum(axis = 1)
    rect[0] = point[np.argmin(sum_)]
    rect[2] = point[np.argmax(sum_)]
    dif = np.diff(point, axis = 1)
    rect[1] = point[np.argmin(dif)]
    rect[3] = point[np.argmax(dif)]
    return rect

img = cv2.imread(arg.input)
img = cv2.resize(img,None,fx=0.5,fy=0.5)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7),3)
img_thresh = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,2)
contours,_ = cv2.findContours(img_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours,key=cv2.contourArea,reverse=True)

sudoku_contour = None
for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)
    if len(approx)==4:
        sudoku_contour = approx
        break
if sudoku_contour is None:
    print("Please Enter correct image")   
else:
    height , width = img.shape[:2]
    src_pts = order_points(sudoku_contour.reshape(4,2))
    dst_pts = np.float32([[0, 0],[width, 0],[width,height],[0,height]])
    transform = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warp = cv2.warpPerspective(img, transform, (width, height))
    cv2.imwrite(arg.save,warp)

