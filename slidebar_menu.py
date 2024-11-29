from main_admin import Ui_MainWindow
import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton

class MysideBar(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('SideBar Menu')

        self.widget_5.setHidden(True)

        self.pushButton_money1.clicked.connect(self.switch_to_money)
        self.pushButton_money2.clicked.connect(self.switch_to_money)

        self.pushButton_tracing1.clicked.connect(self.switch_to_trackng)
        self.pushButton_tracing2.clicked.connect(self.switch_to_trackng)

        self.pushButton_orde1_2.clicked.connect(self.switch_to_order)
        self.pushButton_order2_2.clicked.connect(self.switch_to_order)


    def switch_to_money(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_trackng(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_order(self):
        self.stackedWidget.setCurrentIndex(2)


app = QApplication(sys.argv)
wind = MysideBar()
wind.show()
app.exec()