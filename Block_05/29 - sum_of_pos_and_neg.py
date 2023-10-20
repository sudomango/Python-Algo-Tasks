import sys
sys.path.append("..")

import useful_functions as useful

def main():
  new_array = useful.random_array(-100, 100, 40)

  print("Array = ", end = "")
  useful.print_array(new_array)

  result_sums = sum_of_pos_and_neg(new_array)

  print(f"Сумма положительных элементов = {result_sums[0]}.")
  print(f"Сумма отрицательных элементов = {result_sums[1]}.")


def sum_of_pos_and_neg(array):
  pos_sum = 0
  neg_sum = 0
  for number in array:
    if (number < 0): neg_sum += number
    if (number > 0): pos_sum += number

  return (pos_sum, neg_sum)


main()