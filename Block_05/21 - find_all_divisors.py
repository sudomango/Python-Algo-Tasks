import sys, math
sys.path.append("..")

import useful_functions as useful

def main():
  print("Все делители числа 128:", end = " ")
  useful.print_array(find_divisors(128))
  print("Все делители числа 303:", end = " ")
  useful.print_array(find_divisors(303))
  print("Все делители числа 1139:", end = " ")
  useful.print_array(find_divisors(1139))
  print("Все делители числа 2080:", end = " ")
  useful.print_array(find_divisors(2080))

# ----------------

# Проверить правильность работы программы можно здесь:
# https://onlinemathtools.com/find-all-divisors

# ----------------

def find_divisors(number):
  divisors = []

  # Как и в случае с простыми числами, поиск ведём только до sqrt(number).
  max_border = math.floor(math.sqrt(number))

  for div in range(1, max_border + 1):
    if number % div == 0:
      divisors.append(div)
      # Подбираем вторую пару для первого делителя.
      if number // div != div:
        divisors.append(number // div)

  divisors.sort()
  return divisors

# ----------------

main()