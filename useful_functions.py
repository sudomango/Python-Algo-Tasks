import math, random, copy

# ------------------------------------------------------

# Функция is_leap_year проверяет, является ли указанный год високосным.

def is_leap_year(year):
  if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    return True
  else:
    return False

# ------------------------------------------------------

# Функция delta_time вычисляет разницу между двумя временными точками в секундах.
# Может быть полезно для замеров времени работы алгоритма.
# Для установки временной точки используйте функцию time_a = datetime.datetime.now()

# Альтернатива = использовать модуль time. time_a = time.time(), time_b = time.time(), print(time_b - time_a).

def delta_time(time_a, time_b):
  return (time_b - time_a).total_seconds()

# ------------------------------------------------------

# Функция irange = inclusive range делает тоже самое, что range(), но вторая граница будет включена в диапазон.

def irange(start, end, step = 1):
  if step > 0:
    return range(start, end + 1, step)
  else:
    return range(start, end - 1, step)

# ------------------------------------------------------

# Функция is_prime_number проверяет, является ли указанное число простым (улучшенный наивный алгоритм).

def is_prime_number(number):

  if (number < 2): return False
  if (number == 2): return True
  if (number % 2 == 0): return False

  max_number = math.floor(math.sqrt(number))

  for divider in irange(3, max_number, 2):
    if (number % divider == 0):
      return False
  
  return True

# ------------------------------------------------------

# Функция random_array генерирует массив случайных целых чисел.

def random_array(min = -100, max = 100, count = 10, rep = "y"):

  if (rep == "n") and (count > max - min + 1):
    print("Запрашиваемое количество элементов превышает допустимый диапазон. Будут выведены все числа указанного диапазона в случайном порядке.")
    count = max - min + 1
  
  result_array = []

  for index in range(0, count):
    if rep == "y":
      result_array.append(random.randint(min, max))
    else:

      rand_number = random.randint(min, max)

      while rand_number in result_array:
        rand_number = random.randint(min, max)
      else:
        result_array.append(rand_number)
  
  return result_array

# ------------------------------------------------------

# Функция print_array распечатывает массив в одну строку через запятую.

def print_array(user_array):
  array_copy = copy.deepcopy(user_array) # Так как в Python список передаётся в функцию по ссылке, стоит сделать его копию.
  for index in range(0, len(array_copy)):
    array_copy[index] = str(array_copy[index])
  print(", ".join(array_copy))

# ------------------------------------------------------

# Функция string_reverse переворачивает строку задом наперёд (удобный синоним для слайсов).

def string_reverse(user_string):
  return user_string[::-1]

# ------------------------------------------------------

# Функция factorize раскладывает указанное в параметрах число на простые множители.

def factorize(the_number):

  factors = []

  div = 2

  while div * div <= the_number:
    if the_number % div == 0:
      factors.append(div)
      the_number = the_number // div
    else:
      if (div == 2): div += 1
      else: div += 2

  if the_number > 1: factors.append(the_number)
  return factors