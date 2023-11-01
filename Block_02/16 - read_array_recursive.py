def main():

    new_array_2d = ((1, 10, 1, 20), (-10, 4, 5, 0), (-3, 3, 123, 12), (10, 4, -10, 20))
    recursion_array(0, 0, new_array_2d)


def recursion_array(index_a, index_b, array):
    if index_a < len(array):
        if index_b < len(array[index_a]) - 1:
            print(array[index_a][index_b], end=", ")
        else:
            print(array[index_a][index_b])
        if index_b + 1 < len(array[index_a]):
            recursion_array(index_a, index_b + 1, array)
        else:
            index_b = 0
            recursion_array(index_a + 1, index_b, array)

# Для элементов первой глубины вложенности используем index_a, для элементов внутри вложенных списков = index_b.


main()