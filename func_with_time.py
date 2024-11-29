from datetime import datetime
import time


def time_now():
    import datetime
    return f"{datetime.date.today()} {time.strftime("%H")}"


# Функция для расчета времени в часах
def calculate_time_difference(time_str1, time_str2):
    time_format = '%Y-%m-%d %H'
    if time_str2 is None:
        time_str2 = time_now()
    time2 = datetime.strptime(time_str2, time_format)
    time1 = datetime.strptime(time_str1, time_format)
    time_difference = abs((time1 - time2).total_seconds() // 3600)

    return int(time_difference)
