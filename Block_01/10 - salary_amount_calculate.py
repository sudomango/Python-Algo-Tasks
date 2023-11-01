def salary_amount(employee):
    result = 1000 + 20 * employee["hours"] + 30 * employee["clients"]
    return result


# Создаём массив сотрудников, каждый сотрудник = это отдельный ассоциативный массив (словарь).
employees = [
    {"name": "Jack", "hours": 120, "clients": 10},
    {"name": "Andrew", "hours": 100, "clients": 6},
    {"name": "Henry", "hours": 96, "clients": 10},
    {"name": "Alice", "hours": 80, "clients": 32},
    {"name": "Elizabeth", "hours": 108, "clients": 8},
]

# Рассчитываем зарплату, и добавляем её в словарь к каждому сотруднику.
for employee in employees:
    salary = salary_amount(employee)
    employee["salary"] = salary

# Сортируем массив словарей в порядке убывания, используя ключ "зарплата".
employees = sorted(employees, key=lambda x: x["salary"], reverse=True)

for employee in employees:
    print(f"Имя = {employee['name']}, зарплата = {employee['salary']}")