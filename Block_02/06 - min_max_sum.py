import sys
sys.path.append("..")

import useful_functions as useful

def main():

  array = useful.random_array(-100, 100, 20)

  result = min_max_sum(array)

  print("Source Array = ", end = "")
  useful.print_array(array)

  # Сортируем массив для удобства проверки работы функции.
  array.sort()
  print("Sorted Array = ", end = "")
  useful.print_array(array)

  print(f"Min = {result['min']}, Max = {result['max']}, Sum = {result['sum']}, Avg = {result['avg']:.4f}")

# ------------------------------------------------------

def min_max_sum(user_array):
  min = user_array[0]
  max = user_array[0]
  sum = 0

  for element in user_array:
    if element < min: min = element
    if element > max: max = element
    sum += element
  
  avg = sum / len(user_array)

  return {"min": min, "max": max, "sum": sum, "avg": avg}

# ------------------------------------------------------

main()