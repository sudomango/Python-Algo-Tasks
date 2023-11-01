def main():
    source_matrix = ((1, 5, 8, 0, 4), (-10, 2, -3, 12, 1), (18, 3, 0, 42, 10), (0, 0, 0, 1, -15), (16, 4, 5, 6, 12))

    print("Исходная матрица:")
    print_matrix(source_matrix)

    print("\nТранспонированная матрица:")
    print_matrix(transp_matrix(source_matrix))

    print(f"\nСумма элементов с чётными индексами на главной диагонали = {sum_of_main(source_matrix)}")
    print(f"Последняя цифра суммы всех элементов на главной и побочной диагоналях = {last_digit_of_sum(source_matrix)}")
    min_element = last_minimal(source_matrix)
    print(f"Минимальный элемент матрицы и координаты его последнего вхождения = {min_element['min']}, {min_element['index_i']}, {min_element['index_j']}")


# Функция для нахождения самого длинного (по количеству символов) элемента в матрице.
def max_in_matrix(user_matrix):
    max_length = 0
    for row in user_matrix:
        for a in row:
            length = len(str(a))
            if length > max_length:
                max_length = length
    return max_length


def print_matrix(user_matrix):
    # Самая большая длина символов у элемента матрицы (по ней будем ровнять остальные элементы).
    max_length = max_in_matrix(user_matrix)
    for i in range(0, len(user_matrix)):
        for j in range(0, len(user_matrix[i])):
            spaces = " " * (max_length - len(str(user_matrix[i][j])))
            # Проверяем, является ли текущий индекс - последним индексом в строке.
            if j != len(user_matrix[i]) - 1:
                print(spaces, user_matrix[i][j], " ", sep=" ", end="")
            else:
                # Если это последний элемент строки, то выводим с символом "\n".
                print(spaces, user_matrix[i][j], sep=" ")


# Функция возвращает нам транспонированную матрицу.
def transp_matrix(user_matrix):
    t_matrix = []
    i, j = 0, 0

    for i in range(0, len(user_matrix)):
        t_matrix.append([])
        for j in range(0, len(user_matrix[i])):
            t_matrix[i].append(user_matrix[j][i])

    return t_matrix


# Функция суммирует элементы с чётными индексами на главной диагонали.
def sum_of_main(user_matrix):
    sum = 0

    for i in range(0, len(user_matrix), 2):
        sum += user_matrix[i][i]

    return sum


# Последняя цифра суммы всех элементов главной и побочной диагонали матрицы.
def last_digit_of_sum(user_matrix):
    sum = 0
    n = len(user_matrix)  # Вычисляем порядок матрицы.

    for i in range(0, n):
        sum += user_matrix[i][i] + user_matrix[n - 1 - i][i]

    last_digit = sum % 10
    return last_digit


# Функция выводит индексы последнего минимального элемента матрицы.
def last_minimal(user_matrix):
    min = user_matrix[0][0]
    indexes = [0, 0]

    for i in range(0, len(user_matrix)):
        for j in range(0, len(user_matrix[i])):
            if user_matrix[i][j] < min:
                min = user_matrix[i][j]
                indexes = [i, j]
            elif user_matrix[i][j] == min:
                indexes = [i, j]

    return {"min": min, "index_i": indexes[0], "index_j": indexes[1]}


main()