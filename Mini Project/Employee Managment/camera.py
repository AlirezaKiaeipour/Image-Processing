import cv2
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QImage,QPixmap

class Camera(QWidget):
    def __init__(self,pic):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form_cam.ui",None)
        self.ui.show()
        self.ui.btn_image.clicked.connect(self.save)
        self.pic = pic
        detetor = cv2.CascadeClassifier("package/face.xml")
        cap = cv2.VideoCapture(0)
        while True:
            _,self.frame = cap.read()
            self.frame_rgb = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
            self.frame_rgb = cv2.resize(self.frame_rgb,(308,260))
            faces = detetor.detectMultiScale(self.frame,1.3,4)
            img = QImage(self.frame_rgb, self.frame_rgb.shape[1], self.frame_rgb.shape[0],QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            self.ui.label_img.setPixmap(pixmap)
            for x,y,w,h in faces:
                self.frame_face = self.frame[y:y+h,x:x+w]
            self.key = cv2.waitKey(1)
        
    def save(self):
        self.frame_face_label = cv2.resize(self.frame_face,(72,72))
        cv2.imwrite(self.pic,self.frame_face_label)
        self.ui.close()
        