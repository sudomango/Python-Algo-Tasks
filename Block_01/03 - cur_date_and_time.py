import datetime, pytz


def main():
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

    timezone = pytz.timezone("Europe/Moscow")
    time = datetime.datetime.now(timezone)

    print("Текущая дата и время: ", time.strftime("%d.%m.%Y %H:%M:%S"), ", день недели: ", days_of_week[time.isoweekday() - 1], ".", sep="")


main()

# ----------------

# Несколько полезных туториалов по модулю datetime в Python:

# https://www.geeksforgeeks.org/python-datetime-module
# https://www.w3schools.com/python/python_datetime.asp
# https://www.programiz.com/python-programming/datetime

# ----------------