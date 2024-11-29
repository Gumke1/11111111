import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel

import main_funcs
import main_menu
import main_admin
import reg1
import slidebar_admin
import slidebar_menu
import vhod
import sqlite3
import registration
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QInputDialog, QMessageBox, QPushButton, QLabel

from func_with_time import time_now


def send_to_db(nik_work, id_problem):
    # Функция для отправкиNickname работника и ID проблемы в базу данных
    con = sqlite3.connect("db/tab.db")
    cur = con.cursor()
    req_for_busy = cur.execute("""select nickname, busy from users""").fetchall()

    # Проверяем, занят ли работник или совпадает ли ник
    for i in req_for_busy:
        print(i[0], i[1])
        if i[0] != nik_work or i[1] == 1:
            return

    # Если работник не занят, устанавливаем его статус как занятый и обновляем запись о ремонте
    print("123123123123123213")
    cur.execute("""UPDATE users
                   SET busy = ? WHERE nickname = ?""", (1, nik_work))
    cur.execute("""UPDATE repair_hardware
                   SET nickname = ? WHERE id = ?""", (nickname, id_problem))

    con.commit()
    con.close()


nickname = "nick"  # Глобальная переменная для ника текущего пользователя


class Reg(QMainWindow, reg1.Ui_Dialog):
    # Класс диалогового окна регистрации
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Настройка интерфейса из файла дизайна
        # Подключение кнопок к соответствующим функциям
        self.pushButton_login_reg.clicked.connect(self.sign_vhod)
        self.pushButton_registration.clicked.connect(self.sign_reg)

    def sign_vhod(self):
        # Открытие окна входа
        self.window = Vhodi()
        self.window.show()
        self.close()  # Закрывает окно регистрации

    def sign_reg(self):
        # Открытие окна регистрации
        self.window = Registr()
        self.window.show()
        self.close()  # Закрывает окно регистрации


class Window(QWidget):
    # Простой класс окна, указывающий на вход пользователя
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 100, 100)  # Установка размера и положения окна
        self.lab1 = QLabel(self)
        self.lab1.setGeometry(30, 30, 50, 50)
        self.lab1.setText('Вы вошли')  # Отображает 'Вы вошли'


class Ui_MainWindow1(QMainWindow, main_admin.Ui_MainWindow):
    # Класс основного окна администратора
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Подключение кнопок к соответствующим функциям
        self.pushButton_send_order.clicked.connect(self.send_order)
        self.refresh_btn.clicked.connect(self.refresh_bd)
        self.widget_5.setHidden(True)

    def send_order(self):
        # Отправка информации о заказе в базу данных
        nik_work = self.lineEdit_nik_work.text()  # Получение ника работника
        id_problem = self.lineEdit_id_problem.text()  # Получение ID проблемы
        send_to_db(nik_work, id_problem)  # Отправка в базу данных

    def refresh_bd(self):
        # Обновление данных, отображаемых в таблицах
        db = QSqlDatabase.addDatabase('QSQLITE')  # Указание типа базы данных
        db.setDatabaseName('db/tab.db')  # Установка имени базы данных
        db.open()  # Открытие соединения с базой данных

        # Создание модели для таблицы пользователей и установка её в представление таблицы
        model = QSqlTableModel(self, db)
        model.setTable('users')
        model.select()
        self.tableView_2.setModel(model)
        self.tableView_2.setStyleSheet("color: black; background-color: white;")

        # Создание модели для таблицы ремонтов и установка её в представление таблицы
        model = QSqlTableModel(self, db)
        model.setTable('repair_hardware')
        model.select()
        self.tableView.setModel(model)
        self.tableView.setStyleSheet("color: black; background-color: white;")


class Vhodi(QMainWindow, vhod.Ui_reg2):
    # Класс окна входа
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        # Подключение кнопок к их функциям
        self.pushButton_login_log.clicked.connect(self.sign)
        self.pushButton_login_log.clicked.connect(self.to_main)

    def sign(self):
        # Логика для входа в систему
        con = sqlite3.connect('db/tab.db')
        a = self.lineEdit_log_log.text()  # Получение введенного ника
        b = self.lineEdit_passwor_log.text()  # Получение введенного пароля
        cur = con.cursor()
        result = cur.execute("""SELECT password from users WHERE nickname = ?""", (a,)).fetchone()

        # Проверка на пустой ник или пароль
        if a == '' and b == '':
            pass
        else:
            if result is not None:
                f = result[0]
                if f == b:  # Если пароль совпадает
                    self.w = Ui_MainWindow2()  # Открывает основное окно для пользователя
                    self.w.show()
                    self.name = b  # Сохраняем имя пользователя
                    self.close()  # Закрывает окно входа

    def to_main(self):
        # Логика для входа администратора
        a = self.lineEdit_log_log.text()
        b = self.lineEdit_passwor_log.text()
        if a == 'admin' and b == 'admin':  # Хардкодированные учетные данные администратора
            self.w = Ui_MainWindow1()
            self.w.show()
            self.close()  # Закрывает окно входа


def send_application(number_hardware, comment):
    # Функция для отправки заявки на ремонт в базу данных
    con = sqlite3.connect("db/tab.db")
    cur = con.cursor()
    start_time = time_now()  # Получаем текущее время

    # Вставляем новую запись о ремонте в базу данных
    cur.execute("""INSERT INTO repair_hardware(start, comment_applicant, id_hardware, done) VALUES(?, ?, ?, ?)""",
                (start_time, comment, number_hardware, 0)).fetchall()
    con.commit()
    con.close()


class Registr(QMainWindow, registration.Ui_Dialog):
    # Класс окна регистрации
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_reg_reg.clicked.connect(self.regis)

    def regis(self):
        # Регистрация нового пользователя
        i = self.lineEdit_expirience_reg.text()
        h = self.lineEdit_level_reg.text()
        a = self.lineEdit_login_reg.text()  # Получение введенного логина
        c = self.lineEdit_midlname_reg.text()
        b = self.lineEdit_paswword_reg.text()  # Получение введенного пароля
        d = self.lineEdit_secondname_reg.text()
        e = self.lineEdit_name_reg.text()
        f = self.lineEdit_post_reg.text()
        g = self.lineEdit_age_reg.text()

        con = sqlite3.connect('db/tab.db')
        cur = con.cursor()
        result = cur.execute("""SELECT nickname from users""").fetchall()  # Проверка существующих пользователей
        if a == '':
            pass
        else:
            sp = [el[0] for el in result]  # Список существующих никнеймов

            if a not in sp:  # Если ник не занят
                # Вставка нового пользователя в базу данных
                cur.execute(
                    f"INSERT INTO users VALUES ('{a}', '{b}', '{c}', '{d}', '{e}', '{f}', '{g}', '{''}', '{h}', '{i}', '{g}', '{1}')")
                con.commit()
            con.close()
        self.w = Vhodi()  # Возврат к окну входа после регистрации
        self.w.show()
        self.close()


class MysideBar(QMainWindow, main_admin.Ui_MainWindow):
    # Боковое меню для администратора
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('SideBar Menu')

        self.widget_5.setHidden(True)

        # Подключение кнопок бокового меню к их функционалу
        self.pushButton_money1.clicked.connect(self.switch_to_money)
        self.pushButton_money2.clicked.connect(self.switch_to_money)

        self.pushButton_education1us.clicked.connect(self.switch_to_trackng)
        self.pushButton_education2us.clicked.connect(self.switch_to_trackng)

        self.pushButton_tracing1.clicked.connect(self.switch_to_order)
        self.pushButton_tracing2.clicked.connect(self.switch_to_order)

    def switch_to_money(self):
        self.stackedWidget.setCurrentIndex(0)  # Переключение на страницу "Деньги"

    def switch_to_trackng(self):
        self.stackedWidget.setCurrentIndex(2)  # Переключение на страницу "Отслеживание"

    def switch_to_order(self):
        self.stackedWidget.setCurrentIndex(1)  # Переключение на страницу "Заказ"


def my_exception_hook(exctype, value, traceback):
    # Обработчик исключений, который выводит информацию об исключении и завершает приложение
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


def update_good_status():
    # Обновление статуса записи о ремонте на "выполнена"
    con = sqlite3.connect("db/tab.db")
    cur = con.cursor()
    cur.execute("""update repair_hardware set done = ?, end = ? where nickname = ?""",
                (1, time_now(), nickname)).fetchall()
    cur.execute("""update users set busy = ? where nickname = ?""", (0, nickname)).fetchall()
    con.commit()
    con.close()


def update_bad_status(comment_worker):
    # Обновление статуса, если ремонт не удался
    con = sqlite3.connect("db/tab.db")
    cur = con.cursor()
    cur.execute("""update users set busy = ? where nickname = ?""", (0, nickname)).fetchall()
    cur.execute("""update repair_hardware set nickname = null, comment_applicant = ? where nickname = ?""",
                (comment_worker, nickname)).fetchall()
    con.commit()
    con.close()


class Ui_MainWindow2(QMainWindow, main_menu.Ui_MainWindow):
    # Класс основного окна пользователя
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('SideBar Menu')
        self.pushButton_link1.clicked.connect(self.func_url)

        # Подключение кнопок к их функционалу
        self.pushButton_education1us.clicked.connect(self.switch_to_money)
        self.pushButton_education2_us.clicked.connect(self.switch_to_money)

        self.pushButton_acc2_us.clicked.connect(self.switch_to_trackng)
        self.pushButton_acc1_us.clicked.connect(self.switch_to_trackng)

        self.pushButton_orde1_2.clicked.connect(self.switch_to_order)
        self.pushButton_order2_2.clicked.connect(self.switch_to_order)
        self.widget_5.setHidden(True)

    def switch_to_money(self):
        self.stackedWidget.setCurrentIndex(0)  # Переключение на страницу "Деньги"

    def func_url(self):
        # Открытие определенного URL в веб-браузере
        url = QUrl("https://dpoprof.ru/povyshenie/povyshenie-kvalifikacii-tokar/")
        QDesktopServices.openUrl(url)

    def switch_to_trackng(self):
        self.stackedWidget.setCurrentIndex(1)  # Переключение на страницу "Отслеживание"

    def switch_to_order(self):
        self.stackedWidget.setCurrentIndex(2)  # Переключение на страницу "Заказ"

    def send_application(self):
        # Отправка деталей заявки в базу данных
        number_hardware = self.lineEdit_id_input.text()
        comment_applicant = self.textEdit_com_1.toPlainText()
        send_application(number_hardware, comment_applicant)  # Вызов функции для отправки заявки
        self.textEdit_com_1.clear()  # Очистка текстового поля комментария
        self.lineEdit_id_input.clear()  # Очистка текстового поля ввода ID оборудования

    def send_good_statement(self):
        update_good_status()  # Обновление статуса хороших ремонтов

    def send_bad_statement(self):
        comment_worker = self.textEdit_com_2.toPlainText()  # Получение комментария о плохом состоянии
        self.textEdit_com_2.clear()  # Очистка текстового поля комментария
        update_bad_status(comment_worker)  # Обновление статуса с плохим ремонтом


# Сохранение ссылки на обработчик исключений
sys._excepthook = sys.excepthook

# Установка обработчика исключений на нашу обёртку
sys.excepthook = my_exception_hook

app = QApplication(sys.argv)  # Инициализация приложения
w = Reg()  # Создание экземпляра начального окна регистрации
w.show()  # Показ окна
app.exec()  # Запуск цикла приложения