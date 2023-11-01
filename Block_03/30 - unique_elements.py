import sys, os
sys.path.append(os.path.dirname(__file__) + "/..")
import useful_functions as useful


def main():
    array = useful.random_array(-10, 10, 20, "y")
    print("\nSource Array = ")
    useful.print_array(array)

    print("\nUnique Elements From Array = ")

    print("Sorted: ", end="")
    useful.print_array(uniques_sorted(array.copy()))

    print("Keep Order: ", end="")
    useful.print_array(unique_elements(array.copy()))


# Сортируем список, после чего поочерёдно проверяем элементы на уникальность.
def uniques_sorted(user_list):
    user_list.sort()
    uniques = []

    for index in range(0, len(user_list)):
        current = user_list[index]
        if index == 0:
            next = user_list[index + 1]
            if current != next:
                uniques.append(current)

        elif index == len(user_list) - 1:
            previous = user_list[index - 1]
            if current != previous:
                uniques.append(current)

        else:
            next = user_list[index + 1]
            previous = user_list[index - 1]

            if current != next and current != previous:
                uniques.append(current)
    return uniques


# Альтернативная реализация, в которой мы используем метод list.count().
def unique_elements(user_list):
    uniques = []

    for x in user_list:
        if user_list.count(x) == 1: uniques.append(x)

    return uniques


main()