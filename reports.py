import datetime
import sqlite3
import csv
from datetime import datetime
import sqlite3

from docx import Document

from func_with_time import calculate_time_difference, time_now


def create_report_of_day():
    # Работа с отчетом
    document = Document()

    count_of_applications = 0
    equipment_under_repair = 0
    unused_equipment = 0
    count_applications = 0

    con = sqlite3.connect("db/tab.db")
    cur = con.cursor()

    req = cur.execute("""select * from repair_hardware""").fetchall()
    for i in req:
        start = i[2]
        end = i[3]
        done = i[7]
        count_of_applications += done
        if done == 0:
            equipment_under_repair += 1
        print(end)
        if end is None:
            unused_equipment += calculate_time_difference(start, time_now())
        count_applications += 1

    document.add_heading('Отчет Бригады 1', 0)
    p = document.add_paragraph(f'ФИО работников: ')
    document.add_paragraph(f'Общее количество заявок: {count_applications}')
    document.add_paragraph(f'Количество закрытых заявок: {count_of_applications}')
    document.add_paragraph(f'Количество оборудования в ремонте: {equipment_under_repair}')
    document.add_paragraph(f"Оборудование простаивало(в часах): {unused_equipment}")
    document.save("test.doc")

def benefits_calculating():
    result = 0
    con = sqlite3.connect("db/tab.db")
    cur = con.cursor()
    req = cur.execute("""select hardware.details, repair_hardware.start, repair_hardware.end from repair_hardware
    inner join hardware on repair_hardware.id_hardware = hardware.id""").fetchall()
    for i in req:
        result += (i[0] / 24) * calculate_time_difference(i[1], i[2])
    return round(result)


print(benefits_calculating())
