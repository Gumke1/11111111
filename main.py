import sys

import main_menu
import reg1
import slidebar_admin
import slidebar_menu
from reg1 import Ui_Dialog as Reg1
from slidebar_admin import MysideBar
from main_admin import Ui_MainWindow as Admin
from pyclbr import Class
import vhod
import sqlite3
import sys
import registration
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QInputDialog, QMessageBox, QPushButton, QLabel


class Reg(QMainWindow, reg1.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_login_reg.clicked.connect(self.sign_vhod)
        self.pushButton_registration.clicked.connect(self.sign_reg)

    def sign_vhod(self):
        self.w = Vhodi()
        self.w.show()
        self.close()

    def sign_reg(self):
        self.w = Registr()
        self.w.show()
        self.close()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 100, 100)
        self.lab1 = QLabel(self)
        self.lab1.setGeometry(30, 30, 50, 50)
        self.lab1.setText('Вы вошли')


class Vhodi(QMainWindow, vhod.Ui_reg2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.pushButton_login_log.clicked.connect(self.sign)
        self.pushButton_login_log.clicked.connect(self.to_main)

    def sign(self):
        con = sqlite3.connect('tab.db')
        a = self.lineEdit_log_log.text()
        b = self.lineEdit_passwor_log.text()
        cur = con.cursor()
        result = cur.execute("""SELECT password from users
                    WHERE nikname = ?""", (a,)).fetchone()

        if a == '' and b == '':
            pass
        else:
            if result is not None:
                f = result[0]
                if f == b:
                    self.w = Window()
                    self.w.show()
                    self.name = b

    def to_main(self):
        if True:
            self.w = Slide_menu()
            self.w.show()
            self.close()


class Registr(QMainWindow, registration.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_reg_reg.clicked.connect(self.regis)

    def regis(self):
        i = self.lineEdit_expirience_reg.text()
        h = self.lineEdit_level_reg.text()
        a = self.lineEdit_login_reg.text()
        c = self.lineEdit_midlname_reg.text()
        b = self.lineEdit_paswword_reg.text()
        d = self.lineEdit_secondname_reg.text()
        e = self.lineEdit_name_reg.text()
        f = self.lineEdit_post_reg.text()
        g = self.lineEdit_age_reg.text()
        con = sqlite3.connect('tab.db')
        cur = con.cursor()
        result = cur.execute("""SELECT name from users""").fetchall()
        if a == '':
            pass
        else:
            sp = [el[0] for el in result]

            if a not in sp:
                cur.execute(
                    f"INSERT INTO users VALUES ('{a}', '{b}', '{c}', '{d}', '{e}', '{f}', '{g}', '{''}', '{h}','{i}', '{g}', '{1}')")
                con.commit()
            con.close()


class Slide_menu(QMainWindow, slidebar_menu.MysideBar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Slide_admin(QMainWindow, slidebar_admin.MysideBar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

app = QApplication(sys.argv)
w = Reg()
w.show()
app.exec()
