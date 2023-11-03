from math import floor, sqrt

# Пока мы используем только простые оптимизации, без применения сложных алгоритмов.

def main():
    user_number = int(input("Введите любое целое число и узнайте, является ли оно простым: "))
    print(f"Ответ: {is_prime_number(user_number)}")

    print("\nПростые числа от 1 до 100:", end=" ")

    # Для проверки распечатаем все простые числа от 1 до 100.
    for number in irange(1, 100):
        if is_prime_number(number):
            print(number, end=" ")
    print()


# Основная функция, которая проверяет, является ли переданное в аргументах число простым.
def is_prime_number(number):

    if number < 2: return False
    if number == 2: return True
    if number % 2 == 0: return False

    max_number = floor(sqrt(number))  # Поиск множителей только в диапазоне 2..sqrt(x).

    for divider in irange(3, max_number, 2):  # Действуем с шагом 2, так как чётные множители нас не интересуют.
        if number % divider == 0:
            return False

    return True


# Вспомогательная функция = inclusive range. По умолчанию в Python вторая граница диапазона (range) не включается.
# Например: range(0, 9) вернёт нам список чисел 0..8. Это не всегда бывает удобно, поэтому данная функция это исправляет.
def irange(start, end, step=1):
    if step > 0:
        return range(start, end + 1, step)
    else:
        return range(start, end - 1, step)


main()