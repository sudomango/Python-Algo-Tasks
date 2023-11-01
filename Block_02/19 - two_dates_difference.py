import datetime

# Запрашиваем данные у пользователя.
date_string_a = input("Введите первую дату в формате DD.MM.YYYY (например, 23.08.2018): ")
date_string_b = input("Введите вторую дату в формате DD.MM.YYYY (например, 23.08.2018): ")

try:
    date_a = datetime.datetime.strptime(date_string_a, "%d.%m.%Y")
    date_b = datetime.datetime.strptime(date_string_b, "%d.%m.%Y")
except ValueError:
    print("Ошибка. Вы использовали неправильный формат для ввода даты.")
    exit()

difference = date_b - date_a  # difference является объектом timedelta.

# Официальная документация по классу timedelta в Python:
# https://docs.python.org/3.12/library/datetime.html#datetime.timedelta

print(f"Разница между указанными датами (в днях) составляет = {difference.days}.")