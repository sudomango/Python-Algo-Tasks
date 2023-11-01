import re

def main():
    str_number = input("Введите число: ")

    result_sum = 0

    # Подсчитываем сумму чисел через перевод в строку и регулярного выражения "[0-9]".
    # Альтернативная реализация: в цикле брать остаток от деления на 10, и складывать результаты.

    if can_be_number(str_number):
        for char in str_number:
            if re.fullmatch(r"[0-9]", char):
                result_sum += int(char)

        print(f"Сумма всех чисел числа {str_number} равна {result_sum}.")
    else:
        print("Скорее всего, вы опечатались при вводе числа.")


def can_be_number(user_string):
    pattern = r"^[+-]?\d+[\.]?\d*$"
    return bool(re.fullmatch(pattern, user_string))


main()