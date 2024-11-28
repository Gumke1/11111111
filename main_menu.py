# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 754)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(45, 44, 44);\n"
"color: white")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_5.setStyleSheet("QWidget{\n"
"background-color: rgb(0, 85, 0);\n"
"border-top-right-radius:20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: white;\n"
"text-align:left;\n"
"height: 30px;\n"
"border:none;\n"
"border-radius: 10px;\n"
"border-bottom-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"color: rgb(0, 85, 0);\n"
"background-color: white;\n"
"\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_5.setMaximumSize(QtCore.QSize(55, 55))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/res/kisspng-user-profile-2018-in-sight-user-conference-expo-5b554c0968c377.0307553315323166814291-fotor-bg-remover-20241102121640.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_acc2_us = QtWidgets.QPushButton(parent=self.widget_5)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/add_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(":/res/add_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButton_acc2_us.setIcon(icon)
        self.pushButton_acc2_us.setCheckable(True)
        self.pushButton_acc2_us.setAutoExclusive(True)
        self.pushButton_acc2_us.setObjectName("pushButton_acc2_us")
        self.verticalLayout_2.addWidget(self.pushButton_acc2_us)
        self.pushButton_education2_us = QtWidgets.QPushButton(parent=self.widget_5)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/school_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(":/res/school_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButton_education2_us.setIcon(icon1)
        self.pushButton_education2_us.setCheckable(True)
        self.pushButton_education2_us.setAutoExclusive(True)
        self.pushButton_education2_us.setObjectName("pushButton_education2_us")
        self.verticalLayout_2.addWidget(self.pushButton_education2_us)
        self.pushButton_order2_2 = QtWidgets.QPushButton(parent=self.widget_5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/res/summarize_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap(":/res/summarize_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButton_order2_2.setIcon(icon2)
        self.pushButton_order2_2.setCheckable(True)
        self.pushButton_order2_2.setAutoExclusive(True)
        self.pushButton_order2_2.setObjectName("pushButton_order2_2")
        self.verticalLayout_2.addWidget(self.pushButton_order2_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 273, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_12.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/res/logout_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap(":/res/logout_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_5.addWidget(self.pushButton_12)
        self.gridLayout.addWidget(self.widget_5, 1, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background-color: rgb(45, 44, 44);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.education_page = QtWidgets.QWidget()
        self.education_page.setObjectName("education_page")
        self.label_12 = QtWidgets.QLabel(parent=self.education_page)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 261, 291))
        self.label_12.setStyleSheet("border-radius:20px;\n"
"")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/res/dude.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_17 = QtWidgets.QLabel(parent=self.education_page)
        self.label_17.setGeometry(QtCore.QRect(290, 50, 281, 291))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/res/dude2.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_25 = QtWidgets.QLabel(parent=self.education_page)
        self.label_25.setGeometry(QtCore.QRect(590, 50, 271, 291))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap(":/res/dude1.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.label_30 = QtWidgets.QLabel(parent=self.education_page)
        self.label_30.setGeometry(QtCore.QRect(10, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.pushButton_link1 = QtWidgets.QPushButton(parent=self.education_page)
        self.pushButton_link1.setGeometry(QtCore.QRect(20, 510, 261, 41))
        self.pushButton_link1.setStyleSheet("background-color: rgb(0, 153, 81);\n"
"color: white;\n"
"border-radius: 20px;")
        self.pushButton_link1.setObjectName("pushButton_link1")
        self.pushButton_link2 = QtWidgets.QPushButton(parent=self.education_page)
        self.pushButton_link2.setGeometry(QtCore.QRect(310, 510, 261, 41))
        self.pushButton_link2.setStyleSheet("background-color: rgb(0, 153, 81);\n"
"color: white;\n"
"border-radius: 20px;")
        self.pushButton_link2.setObjectName("pushButton_link2")
        self.pushButton_link3 = QtWidgets.QPushButton(parent=self.education_page)
        self.pushButton_link3.setGeometry(QtCore.QRect(590, 510, 261, 41))
        self.pushButton_link3.setStyleSheet("background-color: rgb(0, 153, 81);\n"
"color: white;\n"
"border-radius: 20px;")
        self.pushButton_link3.setObjectName("pushButton_link3")
        self.label_31 = QtWidgets.QLabel(parent=self.education_page)
        self.label_31.setGeometry(QtCore.QRect(10, 360, 271, 121))
        self.label_31.setStyleSheet("QLabel{\n"
"setWordWrap(true);\n"
"}")
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(parent=self.education_page)
        self.label_32.setGeometry(QtCore.QRect(300, 360, 271, 121))
        self.label_32.setWordWrap(True)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(parent=self.education_page)
        self.label_33.setGeometry(QtCore.QRect(594, 365, 251, 131))
        self.label_33.setWordWrap(True)
        self.label_33.setObjectName("label_33")
        self.stackedWidget.addWidget(self.education_page)
        self.acc_page = QtWidgets.QWidget()
        self.acc_page.setObjectName("acc_page")
        self.label_8 = QtWidgets.QLabel(parent=self.acc_page)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 271, 271))
        self.label_8.setMinimumSize(QtCore.QSize(40, 40))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/res/kisspng-user-profile-2018-in-sight-user-conference-expo-5b554c0968c377.0307553315323166814291-fotor-bg-remover-20241102121640.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.textEdit_pfil = QtWidgets.QTextEdit(parent=self.acc_page)
        self.textEdit_pfil.setGeometry(QtCore.QRect(10, 410, 831, 171))
        self.textEdit_pfil.setStyleSheet("border: 2px solid white;\n"
"border-radius: 10px;\n"
"color: white;")
        self.textEdit_pfil.setObjectName("textEdit_pfil")
        self.label_34 = QtWidgets.QLabel(parent=self.acc_page)
        self.label_34.setGeometry(QtCore.QRect(10, 380, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.layoutWidget = QtWidgets.QWidget(parent=self.acc_page)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 330, 241, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.label_exp = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_exp.setObjectName("label_exp")
        self.horizontalLayout_12.addWidget(self.label_exp)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.acc_page)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 280, 731, 37))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.label_age = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_age.setObjectName("label_age")
        self.horizontalLayout_9.addWidget(self.label_age)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.label_level = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_level.setObjectName("label_level")
        self.horizontalLayout_11.addWidget(self.label_level)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_11)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.acc_page)
        self.layoutWidget2.setGeometry(QtCore.QRect(290, 10, 451, 247))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_18 = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_13.addWidget(self.label_18)
        self.label_nik = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_nik.setObjectName("label_nik")
        self.horizontalLayout_13.addWidget(self.label_nik)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_19 = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_14.addWidget(self.label_19)
        self.label_Password = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_Password.setObjectName("label_Password")
        self.horizontalLayout_14.addWidget(self.label_Password)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.label_midlename = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_midlename.setObjectName("label_midlename")
        self.horizontalLayout_7.addWidget(self.label_midlename)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.label_secondnaame = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_secondnaame.setObjectName("label_secondnaame")
        self.horizontalLayout_5.addWidget(self.label_secondnaame)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label_name = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_6.addWidget(self.label_name)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_16 = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16)
        self.label_post = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_post.setObjectName("label_post")
        self.horizontalLayout_8.addWidget(self.label_post)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.stackedWidget.addWidget(self.acc_page)
        self.order_page = QtWidgets.QWidget()
        self.order_page.setObjectName("order_page")
        self.lineEdit_id_input = QtWidgets.QLineEdit(parent=self.order_page)
        self.lineEdit_id_input.setGeometry(QtCore.QRect(30, 80, 261, 30))
        self.lineEdit_id_input.setStyleSheet("QLineEdit {\n"
"    border: 2px solid white;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"\n"
"}")
        self.lineEdit_id_input.setObjectName("lineEdit_id_input")
        self.label_6 = QtWidgets.QLabel(parent=self.order_page)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 261, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.order_page)
        self.label_7.setGeometry(QtCore.QRect(30, 50, 141, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_send_order = QtWidgets.QPushButton(parent=self.order_page)
        self.pushButton_send_order.setGeometry(QtCore.QRect(40, 330, 161, 41))
        self.pushButton_send_order.setStyleSheet("background-color: rgb(0, 153, 81);\n"
"color: white;\n"
"border-radius: 20px;")
        self.pushButton_send_order.setObjectName("pushButton_send_order")
        self.textEdit_com_1 = QtWidgets.QTextEdit(parent=self.order_page)
        self.textEdit_com_1.setGeometry(QtCore.QRect(30, 150, 841, 171))
        self.textEdit_com_1.setStyleSheet("border: 2px solid white;\n"
"    border-radius: 10px;\n"
"    color: white;")
        self.textEdit_com_1.setObjectName("textEdit_com_1")
        self.label_35 = QtWidgets.QLabel(parent=self.order_page)
        self.label_35.setGeometry(QtCore.QRect(30, 10, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_20 = QtWidgets.QLabel(parent=self.order_page)
        self.label_20.setGeometry(QtCore.QRect(40, 390, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.pushButton_send_order_2 = QtWidgets.QPushButton(parent=self.order_page)
        self.pushButton_send_order_2.setGeometry(QtCore.QRect(40, 430, 161, 41))
        self.pushButton_send_order_2.setStyleSheet("background-color: rgb(0, 153, 81);\n"
"color: white;\n"
"border-radius: 20px;")
        self.pushButton_send_order_2.setObjectName("pushButton_send_order_2")
        self.textEdit_com_2 = QtWidgets.QTextEdit(parent=self.order_page)
        self.textEdit_com_2.setGeometry(QtCore.QRect(30, 520, 841, 81))
        self.textEdit_com_2.setStyleSheet("border: 2px solid white;\n"
"    border-radius: 10px;\n"
"    color: white;")
        self.textEdit_com_2.setObjectName("textEdit_com_2")
        self.label_22 = QtWidgets.QLabel(parent=self.order_page)
        self.label_22.setGeometry(QtCore.QRect(30, 480, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.pushButton_send_order_3 = QtWidgets.QPushButton(parent=self.order_page)
        self.pushButton_send_order_3.setGeometry(QtCore.QRect(40, 610, 161, 41))
        self.pushButton_send_order_3.setStyleSheet("background-color: rgb(0, 153, 81);\n"
"color: white;\n"
"border-radius: 20px;")
        self.pushButton_send_order_3.setObjectName("pushButton_send_order_3")
        self.stackedWidget.addWidget(self.order_page)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 1, 3, 1, 1)
        self.widget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_4.setStyleSheet("QWidget{\n"
"background-color: rgb(0, 85, 0);\n"
"border-top-right-radius:20px;\n"
"}\n"
"QPushButton{\n"
"color: white;\n"
"\n"
"height: 30px;\n"
"border:none;\n"
"border-radius: 10px;\n"
"border-bottom-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"color: rgb(0, 85, 0);\n"
"background-color: white;\n"
"\n"
"}\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_3.setMaximumSize(QtCore.QSize(55, 55))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/res/kisspng-user-profile-2018-in-sight-user-conference-expo-5b554c0968c377.0307553315323166814291-fotor-bg-remover-20241102121640.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_acc1_us = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_acc1_us.setText("")
        self.pushButton_acc1_us.setIcon(icon)
        self.pushButton_acc1_us.setCheckable(True)
        self.pushButton_acc1_us.setAutoExclusive(True)
        self.pushButton_acc1_us.setObjectName("pushButton_acc1_us")
        self.verticalLayout_7.addWidget(self.pushButton_acc1_us)
        self.pushButton_education1us = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_education1us.setText("")
        self.pushButton_education1us.setIcon(icon1)
        self.pushButton_education1us.setCheckable(True)
        self.pushButton_education1us.setAutoExclusive(True)
        self.pushButton_education1us.setObjectName("pushButton_education1us")
        self.verticalLayout_7.addWidget(self.pushButton_education1us)
        self.pushButton_orde1_2 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_orde1_2.setText("")
        self.pushButton_orde1_2.setIcon(icon2)
        self.pushButton_orde1_2.setCheckable(True)
        self.pushButton_orde1_2.setAutoExclusive(True)
        self.pushButton_orde1_2.setObjectName("pushButton_orde1_2")
        self.verticalLayout_7.addWidget(self.pushButton_orde1_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 278, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.pushButton_logout1 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_logout1.setText("")
        self.pushButton_logout1.setIcon(icon3)
        self.pushButton_logout1.setCheckable(True)
        self.pushButton_logout1.setAutoExclusive(True)
        self.pushButton_logout1.setObjectName("pushButton_logout1")
        self.verticalLayout_4.addWidget(self.pushButton_logout1)
        self.gridLayout.addWidget(self.widget_4, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setStyleSheet("border:none;\n"
"")
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/res/menu_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_13.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/res/remove_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.pushButton_22 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_22.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/res/check_box_outline_blank_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_22.setIcon(icon6)
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_23.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/res/close_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_23.setIcon(icon7)
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout.addWidget(self.pushButton_23)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton.toggled['bool'].connect(self.widget_4.setHidden) # type: ignore
        self.pushButton.toggled['bool'].connect(self.widget_5.setVisible) # type: ignore
        self.pushButton_education1us.toggled['bool'].connect(self.pushButton_education2_us.setChecked) # type: ignore
        self.pushButton_acc1_us.toggled['bool'].connect(self.pushButton_acc2_us.setChecked) # type: ignore
        self.pushButton_acc2_us.toggled['bool'].connect(self.pushButton_acc1_us.setChecked) # type: ignore
        self.pushButton_education2_us.toggled['bool'].connect(self.pushButton_education1us.setChecked) # type: ignore
        self.pushButton_23.toggled['bool'].connect(MainWindow.close) # type: ignore
        self.pushButton_logout1.toggled['bool'].connect(self.pushButton_12.setChecked) # type: ignore
        self.pushButton_12.toggled['bool'].connect(self.pushButton_logout1.setChecked) # type: ignore
        self.pushButton_order2_2.toggled['bool'].connect(self.pushButton_orde1_2.setChecked) # type: ignore
        self.pushButton_orde1_2.toggled['bool'].connect(self.pushButton_order2_2.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_acc2_us.setText(_translate("MainWindow", " Акаунт"))
        self.pushButton_education2_us.setText(_translate("MainWindow", "Обучение"))
        self.pushButton_order2_2.setText(_translate("MainWindow", "Заявки"))
        self.pushButton_12.setText(_translate("MainWindow", "Выход"))
        self.label_30.setText(_translate("MainWindow", "Повышение квалификация"))
        self.pushButton_link1.setText(_translate("MainWindow", "Повысить квалификацию"))
        self.pushButton_link2.setText(_translate("MainWindow", "Повысить квалификацию"))
        self.pushButton_link3.setText(_translate("MainWindow", "Повысить квалификацию"))
        self.label_31.setText(_translate("MainWindow", "На курсе вы узнаете про устройство и эксплуатацию токарных станков, правилам заточки и термообработки, а также вспомните основные свойства обрабатываемых материалов. После вы сможете применять эти знания непосредственно на практике."))
        self.label_32.setText(_translate("MainWindow", "Курс обучает методам консервации и хранения техники, предотвращению ее повреждения, а также безопасной транспортировке. Слушатели освоят технологии, материалы и принципы сохранения техники."))
        self.label_33.setText(_translate("MainWindow", "Специалисты сваривают и режут металлические или полимерные изделий на производстве, стройплощадках, станциях технического обслуживания и других объектах. Наладчики оборудования и операторы установок контролируют режимы работы и следят за исправностью спецтехники"))
        self.label_34.setText(_translate("MainWindow", "Расскажи о себе "))
        self.label_15.setText(_translate("MainWindow", "Стаж"))
        self.label_exp.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "Возраст"))
        self.label_age.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "Разряд"))
        self.label_level.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "Никнейм"))
        self.label_nik.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "Пароль"))
        self.label_Password.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "Отчество"))
        self.label_midlename.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "Фамилия"))
        self.label_secondnaame.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "Имя"))
        self.label_name.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "Должность"))
        self.label_post.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Введите личный коментарий(по желанию)"))
        self.label_7.setText(_translate("MainWindow", "Введите номер станка"))
        self.pushButton_send_order.setText(_translate("MainWindow", "Отправить заявку"))
        self.label_35.setText(_translate("MainWindow", "Сломалось? оборудование не беда, отправь заявку!"))
        self.label_20.setText(_translate("MainWindow", "Починил? отправь отчет!"))
        self.pushButton_send_order_2.setText(_translate("MainWindow", "Отправить заявку"))
        self.label_22.setText(_translate("MainWindow", "Не получилось напиши комментарий."))
        self.pushButton_send_order_3.setText(_translate("MainWindow", "Отправить заявку"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Хорошего рабочего дня!"))
