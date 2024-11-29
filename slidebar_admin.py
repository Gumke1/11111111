from main_menu import Ui_MainWindow
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton

class MysideBar(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('SideBar Menu')

        self.widget_5.setHidden(True)

        self.pushButton_orde1_2.clicked.connect(self.switch_to_money)
        self.pushButton_order2_2.clicked.connect(self.switch_to_money)

        self.pushButton_education1us.clicked.connect(self.switch_to_trackng)
        self.pushButton_education2_us.clicked.connect(self.switch_to_trackng)

        self.pushButton_acc1_us.clicked.connect(self.switch_to_order)
        self.pushButton_acc2_us.clicked.connect(self.switch_to_order)


    def switch_to_money(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_trackng(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_order(self):
        self.stackedWidget.setCurrentIndex(1)
