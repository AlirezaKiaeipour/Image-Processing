import cv2

cam = cv2.VideoCapture(0)
format = cv2.VideoWriter_fourcc(*"XVID")
save = cv2.VideoWriter("output/video.mp4",format,20.0,(640, 480))
while True:
    ret , frame = cam.read()
    cv2.imshow("frame",frame)
    save.write(frame)
    if cv2.waitKey(1) & 0xFF==ord("0"):
        break

cam.release()
save.release()
cv2.destroyAllWindows()