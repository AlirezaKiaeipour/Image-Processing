import cv2
import cvzone

class Face_detection():
    def __init__(self):
        self.face_detector = cv2.CascadeClassifier("package/face.xml")
        self.eyes_detection = cv2.CascadeClassifier("package/eyes.xml")
        self.lip_detection = cv2.CascadeClassifier("package/smile.xml")
        self.flag= 0
        
        cam = cv2.VideoCapture(0)
        while True:
            ret , self.frame = cam.read()
            if ret==False:
                break
            cv2.putText(self.frame,'Emoji on my face:   1',(15,20),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
            cv2.putText(self.frame,'Emoji on my lips & eyes:   2',(15,50),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
            cv2.putText(self.frame,'Pixelate my face:   3',(15,80),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
            cv2.putText(self.frame,'Flip:   4',(15,110),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
            cv2.putText(self.frame,'Paint my:   5',(15,140),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)
            cv2.putText(self.frame,'Exit:   6',(15,170),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2,cv2.LINE_4)

            self.key = cv2.waitKey(1)
            if self.key==ord("1") or self.flag==1:
                self.emoji_face()
            if self.key==ord("2") or self.flag==2:
                self.emoji_eyes()
            if self.key==ord("3") or self.flag==3:
                self.pixelate_face()
            if self.key==ord("4") or self.flag==4:
                self.flip()
            if self.key==ord("5") or self.flag==5:
                self.paint()
            if self.key==ord("6"):
                break
            cv2.imshow("Webcam",self.frame)

    def emoji_face(self):
        self.flag = 1
        emoji = cv2.imread("img/smile.png",cv2.IMREAD_UNCHANGED)
        faces = self.face_detector.detectMultiScale(self.frame , 1.3, minNeighbors=10)
        for face in faces:
            x, y, w, h = face
            # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
            emoji = cv2.resize(emoji,(w,h))
            self.frame = cvzone.overlayPNG(self.frame,emoji,[x,y])
            return self.frame

    def emoji_eyes(self):
        self.flag = 2
        eye_emoji = cv2.imread("img/eye.png",cv2.IMREAD_UNCHANGED)
        eyes = self.eyes_detection.detectMultiScale(self.frame , 1.3, minNeighbors=45)
        for eye in eyes:
            x, y, w, h = eye
            # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
            try:
                self.frame = cvzone.overlayPNG(self.frame,eye_emoji,[x,y])
            except:
                pass
            
        lip_img =  cv2.imread("img/lip.png",cv2.IMREAD_UNCHANGED)
        lips = self.lip_detection.detectMultiScale(self.frame , 1.8,minNeighbors=22)
        for lip in lips:
            lx, ly, lw, lh = lip
            # cv2.rectangle(frame,(lx,ly),(lx+lw,ly+lh),(0,0,255),4)
            try:
                self.frame = cvzone.overlayPNG(self.frame,lip_img,[lx+10,ly-15])
            except:pass
        return self.frame

    def pixelate_face(self):
        self.flag = 3
        faces = self.face_detector.detectMultiScale(self.frame , 1.3, minNeighbors=5)
        for face in faces:
            x, y, w, h = face
            # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),4)
            blur = self.frame[y:y+h,x:x+w]
            pixlate = cv2.resize(blur, (20,20), interpolation=cv2.INTER_LINEAR)
            output = cv2.resize(pixlate, (w, h), interpolation=cv2.INTER_NEAREST)
            self.frame[y:y+h,x:x+w] = output
            return self.frame
        
    def flip(self):
        self.flag = 4
        self.frame = cv2.flip(self.frame,1)
        return self.frame

    def paint(self):
        self.flag = 5
        blur = cv2.GaussianBlur(self.frame,(21,21),0)
        self.frame = self.frame / blur
        return self.frame

Face_detection()