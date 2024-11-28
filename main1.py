from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1144, 720)
        MainWindow.setStyleSheet("background-color: rgb(45, 44, 44);\n"
                                 "color: white")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(parent=self.widget_3)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(638, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "    border: 2px solid white;\n"
                                    "    border-radius: 10px;\n"
                                    "    color: white;\n"
                                    "\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_14.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/search_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_14.setIcon(icon)
        self.pushButton_14.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_3)
        self.stackedWidget.setStyleSheet("background-color: rgb(45, 44, 44);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.main_page)
        self.acc_page = QtWidgets.QWidget()
        self.acc_page.setObjectName("acc_page")
        self.stackedWidget.addWidget(self.acc_page)
        self.money_page = QtWidgets.QWidget()
        self.money_page.setObjectName("money_page")
        self.stackedWidget.addWidget(self.money_page)
        self.news_page = QtWidgets.QWidget()
        self.news_page.setObjectName("news_page")
        self.stackedWidget.addWidget(self.news_page)
        self.socials_page = QtWidgets.QWidget()
        self.socials_page.setObjectName("socials_page")
        self.stackedWidget.addWidget(self.socials_page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 1, 3, 1, 1)
        self.widget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_4.setStyleSheet("QWidget{\n"
                                    "background-color: rgb(0, 85, 0);\n"
                                    "}\n"
                                    "\n"
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
        self.label_3.setPixmap(QtGui.QPixmap(
            ":/res/kisspng-user-profile-2018-in-sight-user-conference-expo-5b554c0968c377.0307553315323166814291-fotor-bg-remover-20241102121640.png"))
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
        self.pushButton_main2 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_main2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/home_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(":/res/home_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.pushButton_main2.setIcon(icon1)
        self.pushButton_main2.setCheckable(True)
        self.pushButton_main2.setAutoExclusive(True)
        self.pushButton_main2.setObjectName("pushButton_main2")
        self.verticalLayout_7.addWidget(self.pushButton_main2)
        self.pushButton_acc1 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_acc1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/res/add_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap(":/res/add_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.pushButton_acc1.setIcon(icon2)
        self.pushButton_acc1.setCheckable(True)
        self.pushButton_acc1.setAutoExclusive(True)
        self.pushButton_acc1.setObjectName("pushButton_acc1")
        self.verticalLayout_7.addWidget(self.pushButton_acc1)
        self.pushButton_money1 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_money1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/res/paid_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap(":/res/paid_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.pushButton_money1.setIcon(icon3)
        self.pushButton_money1.setCheckable(True)
        self.pushButton_money1.setAutoExclusive(True)
        self.pushButton_money1.setObjectName("pushButton_money1")
        self.verticalLayout_7.addWidget(self.pushButton_money1)
        self.pushButton_news1 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_news1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/res/update_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap(":/res/update_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButton_news1.setIcon(icon4)
        self.pushButton_news1.setCheckable(True)
        self.pushButton_news1.setAutoExclusive(True)
        self.pushButton_news1.setObjectName("pushButton_news1")
        self.verticalLayout_7.addWidget(self.pushButton_news1)
        self.pushButton_social1 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_social1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/res/forum_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon5.addPixmap(QtGui.QPixmap(":/res/forum_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButton_social1.setIcon(icon5)
        self.pushButton_social1.setCheckable(True)
        self.pushButton_social1.setAutoExclusive(True)
        self.pushButton_social1.setObjectName("pushButton_social1")
        self.verticalLayout_7.addWidget(self.pushButton_social1)
        self.pushButton_settings1 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_settings1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/res/settings_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon6.addPixmap(QtGui.QPixmap(":/res/settings_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButton_settings1.setIcon(icon6)
        self.pushButton_settings1.setCheckable(True)
        self.pushButton_settings1.setAutoExclusive(True)
        self.pushButton_settings1.setObjectName("pushButton_settings1")
        self.verticalLayout_7.addWidget(self.pushButton_settings1)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 278, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.pushButton_logout1 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_logout1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/res/logout_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon7.addPixmap(QtGui.QPixmap(":/res/logout_24dp_005500_FILL0_wght400_GRAD0_opsz24.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButton_logout1.setIcon(icon7)
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
        self.label_6 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_6.setMinimumSize(QtCore.QSize(0, 10))
        self.label_6.setMaximumSize(QtCore.QSize(40, 10))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setStyleSheet("border:none;\n"
                                      "")
        self.pushButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/res/menu_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_13.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/res/remove_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_13.setIcon(icon9)
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.pushButton_22 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_22.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/res/check_box_outline_blank_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"),
                         QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_22.setIcon(icon10)
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_23.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/res/close_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"),
                         QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_23.setIcon(icon11)
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout.addWidget(self.pushButton_23)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 4)
        self.widget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_5.setStyleSheet("QWidget{\n"
                                    "background-color: rgb(0, 85, 0);\n"
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
        self.label_5.setPixmap(QtGui.QPixmap(
            ":/res/kisspng-user-profile-2018-in-sight-user-conference-expo-5b554c0968c377.0307553315323166814291-fotor-bg-remover-20241102121640.png"))
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
        self.pushButton_main1 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_main1.setStyleSheet("")
        self.pushButton_main1.setIcon(icon1)
        self.pushButton_main1.setCheckable(True)
        self.pushButton_main1.setAutoExclusive(True)
        self.pushButton_main1.setObjectName("pushButton_main1")
        self.verticalLayout_2.addWidget(self.pushButton_main1)
        self.pushButton_acc2 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_acc2.setIcon(icon2)
        self.pushButton_acc2.setCheckable(True)
        self.pushButton_acc2.setAutoExclusive(True)
        self.pushButton_acc2.setObjectName("pushButton_acc2")
        self.verticalLayout_2.addWidget(self.pushButton_acc2)
        self.pushButton_money2 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_money2.setIcon(icon3)
        self.pushButton_money2.setCheckable(True)
        self.pushButton_money2.setAutoExclusive(True)
        self.pushButton_money2.setObjectName("pushButton_money2")
        self.verticalLayout_2.addWidget(self.pushButton_money2)
        self.pushButton_news2 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_news2.setIcon(icon4)
        self.pushButton_news2.setCheckable(True)
        self.pushButton_news2.setAutoExclusive(True)
        self.pushButton_news2.setObjectName("pushButton_news2")
        self.verticalLayout_2.addWidget(self.pushButton_news2)
        self.pushButton_social2 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_social2.setIcon(icon5)
        self.pushButton_social2.setCheckable(True)
        self.pushButton_social2.setAutoExclusive(True)
        self.pushButton_social2.setObjectName("pushButton_social2")
        self.verticalLayout_2.addWidget(self.pushButton_social2)
        self.pushButton_settings2 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_settings2.setIcon(icon6)
        self.pushButton_settings2.setCheckable(True)
        self.pushButton_settings2.setAutoExclusive(True)
        self.pushButton_settings2.setObjectName("pushButton_settings2")
        self.verticalLayout_2.addWidget(self.pushButton_settings2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 273, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setIcon(icon7)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_5.addWidget(self.pushButton_12)
        self.gridLayout.addWidget(self.widget_5, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.toggled['bool'].connect(self.widget_4.setHidden)  # type: ignore
        self.pushButton.toggled['bool'].connect(self.widget_5.setVisible)  # type: ignore
        self.pushButton_settings1.toggled['bool'].connect(self.pushButton_settings2.setChecked)  # type: ignore
        self.pushButton_social1.toggled['bool'].connect(self.pushButton_social2.setChecked)  # type: ignore
        self.pushButton_news1.toggled['bool'].connect(self.pushButton_news2.setChecked)  # type: ignore
        self.pushButton_money1.toggled['bool'].connect(self.pushButton_money2.setChecked)  # type: ignore
        self.pushButton_acc1.toggled['bool'].connect(self.pushButton_acc2.setChecked)  # type: ignore
        self.pushButton_main2.toggled['bool'].connect(self.pushButton_main1.setChecked)  # type: ignore
        self.pushButton_main1.toggled['bool'].connect(self.pushButton_main2.setChecked)  # type: ignore
        self.pushButton_acc2.toggled['bool'].connect(self.pushButton_acc1.setChecked)  # type: ignore
        self.pushButton_money2.toggled['bool'].connect(self.pushButton_money1.setChecked)  # type: ignore
        self.pushButton_news2.toggled['bool'].connect(self.pushButton_news1.setChecked)  # type: ignore
        self.pushButton_social2.toggled['bool'].connect(self.pushButton_social1.setChecked)  # type: ignore
        self.pushButton_settings2.toggled['bool'].connect(self.pushButton_settings1.setChecked)  # type: ignore
        self.pushButton_23.toggled['bool'].connect(MainWindow.close)  # type: ignore
        self.pushButton_logout1.toggled['bool'].connect(self.pushButton_12.setChecked)  # type: ignore
        self.pushButton_12.toggled['bool'].connect(self.pushButton_logout1.setChecked)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "V1.02.3"))
        self.label.setText(_translate("MainWindow", "Читай многое, интересное, полезное!"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_main1.setText(_translate("MainWindow", "Основное меню"))
        self.pushButton_acc2.setText(_translate("MainWindow", " Акаунт"))
        self.pushButton_money2.setText(_translate("MainWindow", "Подписка"))
        self.pushButton_news2.setText(_translate("MainWindow", "Что нового"))
        self.pushButton_social2.setText(_translate("MainWindow", "Соц. сети"))
        self.pushButton_settings2.setText(_translate("MainWindow", "Настройки"))
        self.pushButton_12.setText(_translate("MainWindow", "Выход"))
