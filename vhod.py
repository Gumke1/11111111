# Form implementation generated from reading ui file 'vhod.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_reg2(object):
    def setupUi(self, reg2):
        reg2.setObjectName("reg2")
        reg2.resize(440, 545)
        reg2.setStyleSheet("background-color: rgb(45, 44, 44);\n"
                           "color: white;")
        self.pushButton_forgot_log = QtWidgets.QPushButton(parent=reg2)
        self.pushButton_forgot_log.setGeometry(QtCore.QRect(150, 390, 131, 31))
        self.pushButton_forgot_log.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.pushButton_forgot_log.setStyleSheet("border-radius: 20px;\n"
                                                 "color: rgb(6, 255, 172);")
        self.pushButton_forgot_log.setObjectName("pushButton_forgot_log")
        self.label = QtWidgets.QLabel(parent=reg2)
        self.label.setGeometry(QtCore.QRect(120, 70, 211, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/res/logo-no-bg-preview (carve.photos).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_login_log = QtWidgets.QPushButton(parent=reg2)
        self.pushButton_login_log.setGeometry(QtCore.QRect(150, 350, 131, 41))
        self.pushButton_login_log.setStyleSheet("background-color: rgb(0, 153, 81);\n"
                                                "color: white;\n"
                                                "border-radius: 20px;")
        self.pushButton_login_log.setObjectName("pushButton_login_log")
        self.lineEdit_log_log = QtWidgets.QLineEdit(parent=reg2)
        self.lineEdit_log_log.setGeometry(QtCore.QRect(140, 250, 161, 30))
        self.lineEdit_log_log.setStyleSheet("QLineEdit {\n"
                                            "    border: 2px solid white;\n"
                                            "    border-radius: 10px;\n"
                                            "    color: white;\n"
                                            "\n"
                                            "}")
        self.lineEdit_log_log.setObjectName("lineEdit_log_log")
        self.lineEdit_passwor_log = QtWidgets.QLineEdit(parent=reg2)
        self.lineEdit_passwor_log.setGeometry(QtCore.QRect(140, 300, 161, 30))
        self.lineEdit_passwor_log.setStyleSheet("QLineEdit {\n"
                                                "    border: 2px solid white;\n"
                                                "    border-radius: 10px;\n"
                                                "    color: white;\n"
                                                "\n"
                                                "}")
        self.lineEdit_passwor_log.setText("")
        self.lineEdit_passwor_log.setObjectName("lineEdit_passwor_log")
        self.label_2 = QtWidgets.QLabel(parent=reg2)
        self.label_2.setGeometry(QtCore.QRect(140, 230, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=reg2)
        self.label_3.setGeometry(QtCore.QRect(140, 280, 47, 13))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(reg2)
        QtCore.QMetaObject.connectSlotsByName(reg2)

    def retranslateUi(self, reg2):
        _translate = QtCore.QCoreApplication.translate
        reg2.setWindowTitle(_translate("reg2", "Dialog"))
        self.pushButton_forgot_log.setText(_translate("reg2", "Забыли пароль?"))
        self.pushButton_login_log.setText(_translate("reg2", "Вход"))
        self.label_2.setText(_translate("reg2", "Логин"))
        self.label_3.setText(_translate("reg2", "Пароль"))
