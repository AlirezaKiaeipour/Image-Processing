import sys
import cv2
import numpy as np
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui",None)
        self.ui.show()
        self.ui.actionHelp.triggered.connect(self.help)
        while True:
            self.img = np.ones((150,500),np.uint8) * 255
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.img[:,:,0] = self.ui.Slider_R.value()
            self.ui.label_index_R.setText("R: "+str(self.ui.Slider_R.value()))
            self.img[:,:,1] = self.ui.Slider_G.value()
            self.ui.label_index_G.setText("G: "+str(self.ui.Slider_G.value()))
            self.img[:,:,2] = self.ui.Slider_B.value()
            self.ui.label_index_B.setText("B: "+str(self.ui.Slider_B.value()))
            img = QImage(self.img, self.img.shape[1], self.img.shape[0],QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            self.ui.label_img.setPixmap(pixmap)
            cv2.waitKey(1)

    def help(self):
        msg = QMessageBox()
        msg.setText("Color Picker")
        msg.setInformativeText("GUI RGB Color Picker using Pyside6\nThis program was developed by Alireza Kiaeipour\nContact developer: a.kiaipoor@gmail.com\nBuilt in 2022")
        msg.setIcon(QMessageBox.Information)
        msg.exec()
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    app.exec()