def main():

    # Запрашиваем у пользователя информацию.
    user_sum = float(input("Введите сумму, которую вы хотите внести на вклад: "))
    user_months = int(input("Укажите, на какое количество месяцев вы хотите разместить вклад: "))

    if user_months < 1:
        print("Вы ввели неверное значение для количества месяцев.")
        exit()

    result = deposit_calc(user_sum, user_months)

    print(f"Финальная сумма на вкладе будет равна {result:.2f}. Ждём вас среди наших клиентов!")


def deposit_calc(sum, months):
    if months <= 6:
        for x in range(0, months):
            sum += sum * 0.065 / 12
    elif months > 6:
        procent = 0
        if sum <= 500000:
            procent = 0.1
        else:
            procent = 0.08

        for x in range(0, months):
            sum += sum * procent / 12

    return sum


main()