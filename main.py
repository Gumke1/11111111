import sys
from PyQt6.QtWidgets import QApplication, QMainWindow,QPushButton
from vhod import Ui_reg2 as Vhod
from registration import Ui_Dialog as Main_reg
from reg1 import Ui_Dialog as Smol_reg
import reg1
from main_menu import Ui_MainWindow
from main_admin import Ui_MainWindow as Ui_adminWindow

nickname = "nick"


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.ui = Smol_reg()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())