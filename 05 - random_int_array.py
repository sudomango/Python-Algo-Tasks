import random

def main():

  # Получаем входные данные от пользователя.
  min_value = int(input("Введите минимальное значение: "))
  max_value = int(input("Введите максимальное значение: "))
  count = int(input("Введите количество случайных элементов: "))
  repeat = input("Могут ли числа повторяться? (y или n): ")

  print(random_array(min_value, max_value, count, repeat))

# ------------------------------------------------------

def random_array(min, max, count, rep):
  
  # Проверяем, не ввёл ли пользователь количество элементов больше, чем возможно уникальных чисел в указанном диапазоне.
  if (rep == "n") and (count > max - min + 1):
    print("Запрашиваемое количество элементов превышает допустимый диапазон. Будут выведены все числа указанного диапазона в случайном порядке.")
    count = max - min + 1
  
  result_array = []

  for index in range(0, count):
    if rep == "y":
      result_array.append(random.randint(min, max))
    else:
      
      # Пока не получим уникальное значение, повторяем генерацию случайного числа.
      rand_number = random.randint(min, max)

      while rand_number in result_array:
        rand_number = random.randint(min, max)
      else:
        result_array.append(rand_number)
  
  return result_array

# ------------------------------------------------------

main()