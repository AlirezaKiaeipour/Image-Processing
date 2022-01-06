import sys
from functools import partial
import database
import database_admin
import effect
import camera
import hashlib
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QIcon

class Start(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form_login.ui",None)
        self.ui.show()
        self.ui.btn_login.clicked.connect(self.login)       
    
    def login(self):
        resualt = database_admin.select()
        username = self.ui.username.text()
        password = self.ui.password.text()
        hash = hashlib.sha384(password.encode())
        password_hash = hash.hexdigest()
        if username == resualt[0][0] and password_hash == resualt[0][1]:
            self.ui.close()
            self.ui = Main()
        else:
            msg = QMessageBox()
            msg.setText("Incorrect username or password")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("")
            msg.setWindowIcon(QIcon("img/employment"))
            msg.exec()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui",None)
        self.ui.show()
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_setting.clicked.connect(self.setting)
        self.ui.info.triggered.connect(self.info)
        self.read_from_database()

    def read_from_database(self):
        resualt = database.select()
        for i in range(len(resualt)):
            self.label = QLabel()
            self.btn_edit = QPushButton()
            self.btn_delete = QPushButton()
            self.btn_information = QPushButton()
            self.label_img = QLabel()

            self.btn_information.setStyleSheet("background-image : url(img/detail.png);max-width: 24px; min-height: 24px;background-color:#63c132;border-radius:12px;")
            self.btn_delete.setStyleSheet("background-image : url(img/delete.png);max-width: 24px; min-height: 24px;background-color:#ff6978;border-radius:12px;")
            self.btn_edit.setStyleSheet("background-image : url(img/edit.png);max-width: 24px; min-height: 24px;background-color:#f7ff58;border-radius:12px;")
            self.label.setStyleSheet('color: rgb(0, 114, 187);font: 700 11pt "Segoe UI";')
            self.label_img.setStyleSheet("max-width: 72px; min-height: 72px;background-color: rgb(255, 255, 255);border-radius:30%;")
            self.label.setText(f"{resualt[i][1]} {resualt[i][2]}")
            pixmap = QPixmap(f"{resualt[i][7]}")
            self.label_img.setPixmap(pixmap)

            self.ui.gridLayout1.addWidget(self.btn_delete,i,0)
            self.ui.gridLayout1.addWidget(self.btn_edit,i,1)
            self.ui.gridLayout1.addWidget(self.btn_information,i,2)
            self.ui.gridLayout1.addWidget(self.label,i,3)
            self.ui.gridLayout1.addWidget(self.label_img,i,4)
            self.btn_edit.clicked.connect(partial(self.edit,resualt[i]))
            self.btn_information.clicked.connect(partial(self.information,resualt[i]))
            self.btn_delete.clicked.connect(partial(self.delete,resualt[i],self.btn_delete,self.btn_edit,self.btn_information,self.label,self.label_img))

    def add(self):
        self.ui = Add()

    def edit(self,i):
        self.ui = Edit(i)

    def setting(self):
        self.ui = Setting()
        
    def information(self,i):
        msg = QMessageBox()
        msg.setText("Employee information")
        msg.setInformativeText(f"Frist Name: {i[1]}\nLast Name: {i[2]}\nNational Code: {i[3]}\nPhone Number: {i[6]}\nBirth Date: {i[4]}\nEmployment Date: {i[5]}")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(f"{i[1]} {i[2]}")
        msg.setWindowIcon(QIcon("img/employment"))
        msg.exec()

    def delete(self,i,btn_del,btn_edit,btn_info,label,label_img):
        database.delete(i[1])
        label.deleteLater()
        label_img.deleteLater()
        btn_info.deleteLater()
        btn_edit.deleteLater()
        btn_del.deleteLater()
        msg = QMessageBox()
        msg.setText("Delete")
        msg.setInformativeText("Your desired employment has been deleted.")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Delete employment")
        msg.setWindowIcon(QIcon("img/fired"))
        msg.exec()

    def info(self):
        msg = QMessageBox()
        msg.setText("Employee Management")
        msg.setInformativeText("GUI Employee Management using Pyside6 & opencv\ninclude:\n    - Add an employee to the app\n    - Edit employee information\n    - Admin Management\n    - Effects\n    - Hashing\n\nVersion 1.3\nThis program was developed by Alireza Kiaeipour\nContact developer: a.kiaipoor@gmail.com\nBuilt in 2022")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Information")
        msg.setWindowIcon(QIcon("img/employee"))
        msg.exec()

class Add(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form_add.ui",None)
        self.ui.show()
        self.ui.back.clicked.connect(self.back)
        self.ui.added.clicked.connect(self.add_to_database)
        self.ui.btn_webcam.clicked.connect(self.cam)
        self.ui.btn_filter.clicked.connect(self.filter)        

    def add_to_database(self):
        frist_name = self.ui.frist_name.text()
        last_name = self.ui.last_name.text()
        n_code = self.ui.nation_code.text()
        b_date = self.ui.date_birth.text()
        e_date = self.ui.date_employment.text()
        phone_number = self.ui.phone.text()
        
        if frist_name=="" or last_name=="" or n_code=="" or b_date=="" or e_date=="" or phone_number=="":
            msg = QMessageBox()
            msg.setText("Please complete the fields")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
        else:
            database.add(frist_name,last_name,n_code,b_date,e_date,phone_number,self.pic)
            self.ui.frist_name.setText("")
            self.ui.last_name.setText("")
            self.ui.nation_code.setText("")
            self.ui.phone.setText("")
            self.ui.date_birth.setText("")
            self.ui.date_employment.setText("")

    def back(self):
        self.ui = Main()

    def cam(self):
        n_code = self.ui.nation_code.text()
        if n_code=="":
            msg = QMessageBox()
            msg.setText("Please complete the fields")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
        else:
            self.pic = f"pics/{n_code}.jpg"
            self.ui = camera.Camera(self.pic)          

    def filter(self):
        self.ui = effect.Effects()

class Edit(QWidget):
    def __init__(self,i):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form_edit.ui",None)
        self.ui.show()
        self.i = i[3]
        self.ui.back.clicked.connect(self.back)
        self.ui.added.clicked.connect(self.edit_database)
        self.ui.btn_webcam.clicked.connect(self.cam)
        self.ui.frist_name.setText(f"{i[1]}")
        self.ui.last_name.setText(f"{i[2]}")
        self.ui.nation_code.setText(f"{i[3]}")
        self.ui.phone.setText(f"{i[6]}")
        self.ui.date_birth.setText(f"{i[4]}")
        self.ui.date_employment.setText(f"{i[5]}")
        pixmap = QPixmap(f"{i[7]}")
        self.ui.label_image.setPixmap(pixmap)

    def edit_database(self):
        frist_name = self.ui.frist_name.text()
        last_name = self.ui.last_name.text()
        n_code = self.ui.nation_code.text()
        b_date = self.ui.date_birth.text()
        e_date = self.ui.date_employment.text()
        phone_number = self.ui.phone.text()

        if frist_name=="" or last_name=="" or n_code=="" or b_date=="" or e_date=="" or phone_number=="":
            msg = QMessageBox()
            msg.setText("Please complete the fields")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
        else:
            database.update(frist_name,last_name,n_code,b_date,e_date,phone_number,self.i)
            self.back()

    def back(self):
        self.ui = Main()

    def cam(self):
        n_code = self.ui.nation_code.text()
        if n_code=="":
            msg = QMessageBox()
            msg.setText("Please complete the fields")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
        else:
            self.pic = f"pics/{n_code}.jpg"
            self.ui = camera.Camera(self.pic)

class Setting(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form_setting.ui",None)
        self.ui.show()
        self.ui.btn_back.clicked.connect(self.back)
        self.ui.btn_save.clicked.connect(self.save)

    def save(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        if username =="" or password == "":
            msg = QMessageBox()
            msg.setText("Please complete the fields")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
        else:
            hash = hashlib.sha384(password.encode())
            password_hash = hash.hexdigest()
            database_admin.update(username,password_hash)
            self.back()

    def back(self):
        self.ui = Main()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Start()
    app.exec()