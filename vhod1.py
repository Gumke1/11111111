from pyclbr import Class

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QInputDialog, QMessageBox, QPushButton, QLabel

import vhod
import sqlite3
import sys
import registration
from main import ActiveUser


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

    def sign(self):
        con = sqlite3.connect('db/tab.db')
        a = self.lineEdit_log_log.text()
        nickname = a
        b = self.lineEdit_passwor_log.text()
        cur = con.cursor()
        result = cur.execute("""SELECT password from users
                    WHERE name = ?""", (b,)).fetchone()

        if a == '' and b == '':
            pass
        else:
            if result is not None:
                f = result[0]
                if f == a:
                    self.w = Window()
                    self.w.show()


class Registr(QMainWindow, registration.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_reg_reg.clicked.connect(self.regis)

    def regis(self):
        g = self.lineEdit_expirience_reg.text()
        h = self.lineEdit_level_reg.text()
        a = self.lineEdit_login_reg.text()
        c = self.lineEdit_midlname_reg.text()
        b = self.lineEdit_paswword_reg.text()
        d = self.lineEdit_secondname_reg.text()
        e = self.lineEdit_name_reg.text()
        f = self.lineEdit_post_reg.text()
        g = self.lineEdit_age_reg.text()
        con = sqlite3.connect('db/tab.db')
        cur = con.cursor()
        result = cur.execute("""SELECT name from users""").fetchall()
        if a == '':
            pass
        else:
            sp = [el[0] for el in result]
            print(sp)
            if a not in sp:
                cur.execute(f"INSERT INTO users VALUES ('{a}', '{b}', '{c}', '{d}', '{a}', '{a}', '{a}', '{a}', '{a}','{a}', '{a}', '{a}')")
                con.commit()
            con.close()



app = QApplication(sys.argv)
w = Vhodi()
w.show()
app.exec()
