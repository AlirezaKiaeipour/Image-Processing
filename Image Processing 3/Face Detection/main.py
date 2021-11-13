import cv2
import cvzone

face_detector = cv2.CascadeClassifier("package/face.xml")
eyes_detection = cv2.CascadeClassifier("package/eyes.xml")
lip_detection = cv2.CascadeClassifier("package/smile.xml")

def main():
    flag= 0
    cam = cv2.VideoCapture(0)
    while True:
        ret , frame = cam.read()
        if ret==False:
            break
        cv2.putText(frame,'Emoji on my face:   1',(15,20),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
        cv2.putText(frame,'Emoji on my lips & eyes:   2',(15,50),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
        cv2.putText(frame,'Pixelate my face:   3',(15,80),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
        cv2.putText(frame,'Flip:   4',(15,110),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
        cv2.putText(frame,'Paint my:   5',(15,140),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
        cv2.putText(frame,'Exit:   6',(15,170),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)

        key = cv2.waitKey(1)
        if key==ord("1") or flag==1:
            flag = 1
            emoji = cv2.imread("img/smile.png",cv2.IMREAD_UNCHANGED)
            faces = face_detector.detectMultiScale(frame , 1.3, minNeighbors=10)
            for face in faces:
                x, y, w, h = face
                # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
                emoji = cv2.resize(emoji,(w,h))
                frame = cvzone.overlayPNG(frame,emoji,[x,y])

        if key==ord("2") or flag==2:
            flag = 2
            eye_emoji = cv2.imread("img/eye.png",cv2.IMREAD_UNCHANGED)
            eyes = eyes_detection.detectMultiScale(frame , 1.3, minNeighbors=45)
            for eye in eyes:
                x, y, w, h = eye
                # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
                try:
                    frame = cvzone.overlayPNG(frame,eye_emoji,[x,y])
                except:
                    pass
            

            lip_img =  cv2.imread("img/lip.png",cv2.IMREAD_UNCHANGED)
            lips = lip_detection.detectMultiScale(frame , 1.8,minNeighbors=22)
            for lip in lips:
                lx, ly, lw, lh = lip
                # cv2.rectangle(frame,(lx,ly),(lx+lw,ly+lh),(0,0,255),4)
                try:
                    frame = cvzone.overlayPNG(frame,lip_img,[lx+10,ly-15])
                except:pass

        if key==ord("3") or flag==3:
            flag = 3
            faces = face_detector.detectMultiScale(frame , 1.3, minNeighbors=5)
            for face in faces:
                x, y, w, h = face
                # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),4)
                blur = frame[y:y+h,x:x+w]
                pixlate = cv2.resize(blur, (20,20), interpolation=cv2.INTER_LINEAR)
                output = cv2.resize(pixlate, (w, h), interpolation=cv2.INTER_NEAREST)
                frame[y:y+h,x:x+w] = output 

        if key==ord("4") or flag==4:
            flag = 4
            frame = cv2.flip(frame,1)

        if key==ord("5") or flag==5:
            flag = 5
            blur = cv2.GaussianBlur(frame,(21,21),0)
            frame = frame / blur

        if key==ord("6"):
            break

        cv2.imshow("Webcam",frame)

main()