import datetime
import sqlite3
import sys
import time
import traceback

from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QTableWidgetItem, QTableView, QApplication
from PyQt6.QtWidgets import QMainWindow
import main_admin
import main_menu
from main import nickname
from func_with_time import time_now


def send_application(number_hardware, comment):
    # Функция для отправки заявки на ремонт в базу данных
    con = sqlite3.connect("db/tab.db")  # Установка соединения с базой данных
    cur = con.cursor()
    start_time = time_now()  # Получаем текущее время

    # Вставляем новую запись о ремонте в таблицу repair_hardware
    cur.execute("""INSERT INTO repair_hardware(start, comment_applicant, id_hardware, done) VALUES(?, ?, ?, ?)""",
                (start_time, comment, number_hardware, 0)).fetchall()
    con.commit()  # Сохраняем изменения
    con.close()  # Закрываем соединение


def send_to_db(nik_work, id_problem):
    # Функция для обновления информации о работнике и проблеме в базе данных
    con = sqlite3.connect("db/tab.db")  # Установка соединения с базой данных
    cur = con.cursor()
    req_for_busy = cur.execute(
        """select nickname, busy from users""").fetchall()  # Запрашиваем информацию о пользователях

    for i in req_for_busy:
        print(i[0], i[1])
        # Проверяем, занят ли работник или его ник не совпадает
        if i[0] != nik_work or i[1] == 1:
            return
    print("123123123123123213213")
    # Устанавливаем статус работника как 'занятый' и обновляем запись о ремонте
    cur.execute("""UPDATE users SET busy = ? where nickname = ?""", (1, nik_work)).fetchall()
    cur.execute("""update repair_hardware set nickname = ? where id = ?""", (nickname, id_problem)).fetchall()
    con.commit()  # Сохраняем изменения
    con.close()  # Закрываем соединение


def update_good_status():
    # Функция для обновления статуса записи о ремонте на 'выполнено'
    con = sqlite3.connect("db/tab.db")  # Установка соединения с базой данных
    cur = con.cursor()
    cur.execute("""update repair_hardware set done = ?, end = ? where nickname = ?""",
                (1, time_now(), nickname)).fetchall()
    cur.execute("""update users set busy = ? where nickname = ?""", (0, nickname)).fetchall()
    con.commit()  # Сохраняем изменения
    con.close()  # Закрываем соединение


def update_bad_status(comment_worker):
    # Функция для обновления статуса записи о ремонте на 'не выполнено'
    con = sqlite3.connect("db/tab.db")  # Установка соединения с базой данных
    cur = con.cursor()
    cur.execute("""update users set busy = ? where nickname = ?""", (0, nickname)).fetchall()
    cur.execute("""update repair_hardware set nickname = null, comment_applicant = ? where nickname = ?""",
                (comment_worker, nickname)).fetchall()
    con.commit()  # Сохраняем изменения
    con.close()  # Закрываем соединение


class Ui_MainWindow2(QMainWindow, main_menu.Ui_MainWindow):
    # Класс основного окна пользователя
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Настройка интерфейса из файла дизайна
        # Подключение кнопок к соответствующим функциям
        self.pushButton_send_order.clicked.connect(self.send_application)
        self.pushButton_send_order_2.clicked.connect(self.send_good_statement)
        self.pushButton_send_order_3.clicked.connect(self.send_bad_statement)

    def send_application(self):
        # Получение данных заявки и отправка в базу данных
        number_hardware = self.lineEdit_id_input.text()  # Получаем ID оборудования
        comment_applicant = self.textEdit_com_1.toPlainText()  # Получаем комментарий от заявителя
        send_application(number_hardware, comment_applicant)  # Вызываем функцию для отправки заявки

    def send_good_statement(self):
        # Вызываем функцию для обновления статуса успешного завершения ремонта
        update_good_status()

    def send_bad_statement(self):
        # Получаем комментарий о плохом результате и обновляем статус
        comment_worker = self.textEdit_com_2.toPlainText()  # Получаем комментарий о плохом состоянии
        update_bad_status(comment_worker)  # Вызываем функцию для обновления статуса


def excepthook(exc_type, exc_value, exc_tb):
    # Обработчик исключений, который выводит информацию об ошибке
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Error:", tb)  # Выводим ошибку в консоль