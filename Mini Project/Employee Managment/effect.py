import cv2
import numpy as np
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QImage

class Effects(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form_filter.ui",None)
        self.ui.show()
        cap = cv2.VideoCapture(0)
        while True:
            _,self.frame = cap.read()
            self.frame = cv2.resize(self.frame,(164,164))
            self.frame_rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            winter = self.winter()
            img1 = QImage(winter, winter.shape[1], winter.shape[0],QImage.Format_RGB888)
            pixmap1 = QPixmap.fromImage(img1)
            self.ui.label_filter1.setPixmap(pixmap1)

            x_ray = self.x_ray()
            img2 = QImage(x_ray, x_ray.shape[1], x_ray.shape[0],QImage.Format_RGB888)
            pixmap2 = QPixmap.fromImage(img2)
            self.ui.label_filter2.setPixmap(pixmap2)

            frame_hsv = self.hsv()
            img3 = QImage(frame_hsv, frame_hsv.shape[1], frame_hsv.shape[0],QImage.Format_BGR888)
            pixmap3 = QPixmap.fromImage(img3)
            self.ui.label_filter3.setPixmap(pixmap3)

            frame_blue = self.blue()
            img4 = QImage(frame_blue, frame_blue.shape[1], frame_blue.shape[0],QImage.Format_BGR888)
            pixmap4 = QPixmap.fromImage(img4)
            self.ui.label_filter4.setPixmap(pixmap4)

            frame_green = self.green()
            img5 = QImage(frame_green, frame_green.shape[1], frame_green.shape[0],QImage.Format_BGR888)
            pixmap5 = QPixmap.fromImage(img5)
            self.ui.label_filter5.setPixmap(pixmap5)

            frame_red = self.red()
            img6 = QImage(frame_red, frame_red.shape[1], frame_red.shape[0],QImage.Format_BGR888)
            pixmap6 = QPixmap.fromImage(img6)
            self.ui.label_filter6.setPixmap(pixmap6)

            frame_purple = self.purple()
            img7 = QImage(frame_purple, frame_purple.shape[1], frame_purple.shape[0],QImage.Format_BGR888)
            pixmap7 = QPixmap.fromImage(img7)
            self.ui.label_filter7.setPixmap(pixmap7)

            frame_yellow = self.yellow()
            img8 = QImage(frame_yellow, frame_yellow.shape[1], frame_yellow.shape[0],QImage.Format_BGR888)
            pixmap8 = QPixmap.fromImage(img8)
            self.ui.label_filter8.setPixmap(pixmap8)

            frame_cyan = self.cyan()
            img9 = QImage(frame_cyan, frame_cyan.shape[1], frame_cyan.shape[0],QImage.Format_BGR888)
            pixmap9 = QPixmap.fromImage(img9)
            self.ui.label_filter9.setPixmap(pixmap9)
            cv2.waitKey(1)          

    def winter(self):
        frame_winter = cv2.applyColorMap(self.frame, cv2.COLORMAP_WINTER)
        return frame_winter

    def x_ray(self):
        frame_x_ray = 255 - self.frame_rgb
        return frame_x_ray

    def hsv(self):
        frame_hsv = cv2.cvtColor(self.frame_rgb,cv2.COLOR_RGB2HSV)
        return frame_hsv

    def blue(self):
        b,g,r = cv2.split(self.frame)
        g = np.zeros((self.frame.shape[0], self.frame.shape[1]), dtype=np.uint8)
        r = np.zeros((self.frame.shape[0], self.frame.shape[1]), dtype=np.uint8)
        return cv2.merge((b,g,r))

    def green(self):
        b,g,r = cv2.split(self.frame)
        b = np.zeros((self.frame.shape[0], self.frame.shape[1]), dtype=np.uint8)
        r = np.zeros((self.frame.shape[0], self.frame.shape[1]), dtype=np.uint8)
        return cv2.merge((b,g,r))

    def red(self):
        b,g,r = cv2.split(self.frame)
        b = np.zeros((self.frame.shape[0], self.frame.shape[1]), dtype=np.uint8)
        g = np.zeros((self.frame.shape[0], self.frame.shape[1]), dtype=np.uint8)
        return cv2.merge((b,g,r))

    def purple(self):
        b,g,r = cv2.split(self.frame)
        g = np.zeros((self.frame.shape[0], self.frame.shape[1]), dtype=np.uint8)
        return cv2.merge((b,g,r))

    def yellow(self):
        b,g,r = cv2.split(self.frame)
        b = np.zeros((self.frame.shape[0], self.frame.shape[1]), dtype=np.uint8)
        return cv2.merge((b,g,r))

    def cyan(self):
        b,g,r = cv2.split(self.frame)
        r = np.zeros((self.frame.shape[0], self.frame.shape[1]), dtype=np.uint8)
        return cv2.merge((b,g,r))
