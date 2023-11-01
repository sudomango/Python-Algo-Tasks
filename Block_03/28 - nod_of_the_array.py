import sys
sys.path.append("..")
import useful_functions as useful


def main():
    new_array = (54, 576, 450, 162, 144)
    print("\nSource Array = ", new_array)
    print(f"НОД для всех чисел в указанном массиве будет равен {array_gcd(new_array)}.")


# Вспомогательная функция, позволяющая найти НОД(a, b) через последовательное вычитание чисел.
def find_gcd(num_a, num_b):
    while num_a != num_b:
        if num_a > num_b: num_a = num_a - num_b
        else: num_b = num_b - num_a
    return num_a


# Основная функция для вычисления НОД в массиве чисел.
def array_gcd(user_array):
    gcd = find_gcd(user_array[0], user_array[1])

    for index in range(2, len(user_array)):
        gcd = find_gcd(gcd, user_array[index])

    return gcd


main()