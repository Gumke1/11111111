import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from vhod import Ui_reg2


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.ui = Ui_reg2()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
