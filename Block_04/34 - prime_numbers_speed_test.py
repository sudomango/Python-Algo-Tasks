import math, time

def main():
  print("Замер скорости Решета Эратосфена против наивного улучшенного алгоритма, поиск простых чисел в диапазоне от 2 до 5e6.")

  max_number = 5 * 10 ** 6 # Если вы долго ожидаете завершения, лучше снизить данное значение.

  time_a = time.time()
  list_soe = prime_soe(max_number)
  time_b = time.time()

  time_c = time.time()
  # Тоже самое, что проверять циклом, разница на уровне погрешности.
  list_prime = list(filter(is_prime_number, range(2, max_number + 1)))
  time_d = time.time()

  print(f"Время выполнения Решета Эратосфена = {(time_b - time_a):.5f} секунд.")
  print(f"Время выполнения наивного улучшенного алгоритма = {(time_d - time_c):.5f} секунд.")

  # На моём компьютере наивный улучшенный алгоритм начинает заметно проигрывать при значениях max_number от 30'000.
  # Примечание: В будущем можно реализовать наивный улучшенный алгоритм с функцией "запоминания" простых чисел.

# ----------------

def prime_soe(max_number):

  sieve = [True] * (max_number + 1)
  sieve[0:2] = [False, False]

  max_sqrt = math.floor(math.sqrt(max_number))

  for number in range(2, max_sqrt + 1):

    if sieve[number]:
      for multiple in range(number * number, max_number + 1, number):
        if multiple % number == 0:
          sieve[multiple] = False

  prime_numbers = []

  for index in range(0, len(sieve)):
    if sieve[index]:
      prime_numbers.append(index)

  return prime_numbers

# ----------------

def is_prime_number(number):

  if (number < 2): return False
  if (number == 2): return True
  if (number % 2 == 0): return False

  max_number = math.floor(math.sqrt(number))

  for divider in range(3, max_number + 1, 2):
    if (number % divider == 0):
      return False

  return True

# ----------------

main()