import datetime, pytz


def main():
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

    timezone = pytz.timezone("Europe/Moscow")
    time = datetime.datetime.now(timezone)

    print("Текущая дата и время: ", time.strftime("%d.%m.%Y %H:%M:%S"), ", день недели: ", days_of_week[time.isoweekday() - 1], ".", sep="")


main()