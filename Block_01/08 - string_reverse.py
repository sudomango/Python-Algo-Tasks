import sys, os
sys.path.append(os.path.dirname(__file__) + "/..")
import useful_functions as useful


def main():
    print(string_reverse("Hello, World!"))
    print(string_reverse(string_reverse("Hello, Python!")))
    print(string_reverse("Функция генерирует массив случайных чисел"))


def string_reverse(text):
    result_string = ""
    for index in useful.irange(len(text) - 1, 0, -1):
        result_string += text[index]
    return result_string

# Конечно, адекватным вариантом будет использовать slicing: string[::-1].
# Но по условию задачи мы не имеем права использовать встроенные в язык методы и slicing.


# Альтернативная реализация функции с использованием другого алгоритма.
def reverse_string(text):
    result_string = ""
    for char in text:
        result_string = char + result_string
    return result_string

# Здесь мы, в отличие от предыдущего варианта, проходим по символам в прямом порядке, а не в обратном.


main()