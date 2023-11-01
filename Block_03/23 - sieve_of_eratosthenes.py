import sys, math, os
sys.path.append(os.path.dirname(__file__) + "/..")
import useful_functions as useful

# Решето Эратосфена является очень эффективным алгоритмом для поиска простых чисел: О(n * log(log n)).

def main():
    user_n = int(input("Введите максимальное число, до которого мы ищем простые числа: "))

    print(f"Простые числа от 2 до {user_n} включительно с использованием Решета Эратосфена:")
    useful.print_array(prime_soe(user_n))


def prime_soe(max_number):
    # Создаём список чисел от 0 .. max_number, по умолчанию все числа считаются простыми (True).
    # Сами числа мы будем брать из индексов, в значении будут храниться только True и False, это должно уменьшить объём потребляемой памяти.

    sieve = [True] * (max_number + 1)
    sieve[0:2] = [False, False]  # 0 и 1 не являются простыми числами по определению.

    max_sqrt = math.floor(math.sqrt(max_number))

    for number in range(2, max_sqrt + 1):
        # Если число = простое, то мы удаляем из решета все числа, кратные ему. Сначала кратные 2, потом кратные 3 и т. д.
        if sieve[number]:
            for multiple in range(number * number, max_number + 1, number):
                if multiple % number == 0: sieve[multiple] = False

    prime_numbers = []

    # Теперь нам нужно достать все индексы, которые соответствуют простым числам, и создать из них отдельный список.
    for index in range(0, len(sieve)):
        if sieve[index]:
            prime_numbers.append(index)

    return prime_numbers


main()