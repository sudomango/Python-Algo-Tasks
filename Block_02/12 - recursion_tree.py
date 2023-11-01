def main():
    height = int(input("Введите высоту ёлочки, не больше 40: "))

    if height < 1:
        print("Вы указали слишком маленькое значение.")
        exit()

    if height > 40:
        print("Вы ввели слишком большое значение, высота будет автоматически уменьшена до 40.")
        height = 40

    print()
    print_figure(height)


# Функция выводит паттерн вида "* *" указанное количество раз.
def pattern(n):
    pattern_array = []
    for x in range(0, n):
        pattern_array.append("*")
    return " ".join(pattern_array)


# Функция выводит указанное количество пробелов подряд.
def space(n):
    return " " * n


# Основная функция, которая рисует ёлочку по формуле space + pattern + space.
def print_figure(height):
    max_tree_width = 2 * height - 1

    def draw_recursive(i, height, width):
        if i <= height:
            content = pattern(i)
            spaces = space((width - len(content)) // 2)
            print(spaces + content + spaces)
            draw_recursive(i + 1, height, width)

    draw_recursive(1, height, max_tree_width)


main()