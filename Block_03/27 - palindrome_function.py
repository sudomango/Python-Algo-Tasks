import sys, os
sys.path.append(os.path.dirname(__file__) + "/..")
import useful_functions as useful


def main():
    str_a = "Идем, молод, долом меди."  # Отрывок из произведения Велимира Хлебникова.
    str_b = "Искать такси."
    str_c = "Я тоже палиндром!"

    print(f'Является ли строка "{str_a}" палиндромом? Ответ = {str_palindrome(str_a)}.')
    print(f'Является ли строка "{str_b}" палиндромом? Ответ = {str_palindrome(str_b)}.')
    print(f'Является ли строка "{str_c}" палиндромом? Ответ = {str_palindrome(str_c)}.\n')

    int_a = 128060821
    int_b = 546786345

    print(f"Число {int_a} является палиндромом? Ответ = {int_palindrome(int_a)}.")
    print(f"Число {int_b} является палиндромом? Ответ = {int_palindrome(int_b)}.")


def str_palindrome(user_string):
    # Фильтруем строку, оставляем только буквы в нижнем регистре.
    chars = tuple(filter(lambda a: a.isalpha(), user_string.lower()))

    for index in range(0, len(chars) // 2):
        last_index = len(chars) - 1 - index
        if chars[index] != chars[last_index]:
            return False
    return True


def int_palindrome(user_number):
    digits = useful.num_to_array(user_number)
    for index in range(0, len(digits) // 2):
        last_index = len(digits) - 1 - index
        if digits[index] != digits[last_index]:
            return False
    return True


main()