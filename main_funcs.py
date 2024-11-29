import datetime
import sqlite3
import time
import traceback

from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QTableWidgetItem, QTableView

import main_admin
import main_menu
from func_with_time import time_now
from main import *


def send_application(number_hardware, comment):
    con = sqlite3.connect("db/tab.db")
    cur = con.cursor()
    start_time = time_now()

    cur.execute("""INSERT INTO repair_hardware(start, comment_applicant, id_hardware, done) VALUES(?, ?, ?, ?)""",
                (start_time, comment, number_hardware, 0)).fetchall()
    con.commit()
    con.close()


def send_to_db(nik_work, id_problem):
    con = sqlite3.connect("db/tab.db")
    cur = con.cursor()
    req_for_busy = cur.execute("""select nickname, busy from users""").fetchall()
    for i in req_for_busy:
        print(i[0], i[1])
        if i[0] != nik_work or i[1] == 1:
            return
    print("123123123123123213213")
    cur.execute("""UPDATE users
    SET busy = ? where nickname = ?""", (1, nik_work)).fetchall()
    cur.execute("""update repair_hardware set nickname = ? where id = ?""", (nickname, id_problem)).fetchall()
    con.commit()
    con.close()


def update_good_status():
    con = sqlite3.connect("db/tab.db")
    cur = con.cursor()
    cur.execute("""update repair_hardware set done = ?, end = ? where nickname = ?""", (1, time_now(), nickname)).fetchall()
    cur.execute("""update users set busy = ? where nickname = ?""", (0, nickname)).fetchall()
    con.commit()
    con.close()


def update_bad_status(comment_worker):
    con = sqlite3.connect("db/tab.db")
    cur = con.cursor()
    cur.execute("""update users set busy = ? where nickname = ?""", (0, nickname)).fetchall()
    cur.execute("""update repair_hardware set nickname = null, comment_applicant = ? where nickname = ?""", (comment_worker, nickname)).fetchall()
    con.commit()
    con.close()


class Ui_MainWindow2(QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_send_order.clicked.connect(self.send_application)
        self.pushButton_send_order_2.clicked.connect(self.send_good_statement)
        self.pushButton_send_order_3.clicked.connect(self.send_bad_statement)

    def send_application(self):
        number_hardware = self.lineEdit_id_input.text()
        comment_applicant = self.textEdit_com_1.toPlainText()
        send_application(number_hardware, comment_applicant)

    def send_good_statement(self):
        update_good_status()

    def send_bad_statement(self):
        comment_worker = self.textEdit_com_2.toPlainText()
        update_bad_status(comment_worker)


class Ui_MainWindow1(QMainWindow, main_admin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_send_order.clicked.connect(self.send_order)
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('db/tab.db')
        # И откроем подключение
        db.open()
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('users')
        model.select()

        self.tableView.setModel(model)

        model = QSqlTableModel(self, db)
        model.setTable('repair_hardware')
        model.select()

        self.tableView_2.setModel(model)

    def send_order(self):
        nik_work = self.lineEdit_nik_work.text()
        id_problem = self.lineEdit_id_problem.text()
        send_to_db(nik_work, id_problem)

    def select_data(self):
        def select_data(self):
            # Получим результат запроса,
            # который ввели в текстовое поле
            query = self.textEdit.toPlainText()
            res = self.connection.cursor().execute(query).fetchall()
            # Заполним размеры таблицы
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setRowCount(0)
            # Заполняем таблицу элементами
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))



def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Error:", tb)


sys.excepthook = excepthook
app = QApplication(sys.argv)
w = Ui_MainWindow1()
w.show()
app.exec()
