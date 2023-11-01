# Основная теорема арифметики:
# Любое натуральное число n > 1, можно разложить в произведение простых чисел, причём это разложение единственно верное с точностью до порядка следования сомножителей.

def main():
    number = int(input("Введите число, которое необходимо разложить на простые множители: "))
    factors = factorize(number)

    print(f"Простые множители числа {number}:", end=" ")

    for index in range(0, len(factors) - 1):
        print(factors[index], end=" * ")
    else:
        print(factors[-1])


def factorize(n_number):
    factors = []

    div = 2

    while div * div <= n_number:  # Для проверки используем возведение в квадрат вместо math.sqrt(n_number).
        # Можно конечно использовать while div <= math.floor(math.sqrt(n_number)).
        if n_number % div == 0:
            factors.append(div)
            n_number = n_number // div
        else:
            if div == 2: div += 1
            else: div += 2  # Всё чётные числа можно пропустить, так как они не являются простыми на 100%.

    if n_number > 1: factors.append(n_number)
    return factors


main()