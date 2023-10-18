from math import floor, sqrt

# Пока мы используем только простые оптимизации, без применения сложных алгоритмов.

def main():
  
  # Проверяем, верно ли работает созданная нами функция is_prime_number на разных числах.
  print("Является ли то или иное число простым?")
  
  print("\n1 =", is_prime_number(1)) # = False
  print("5 =", is_prime_number(5)) # = True
  print("123 =", is_prime_number(123)) # = False
  print("-10 =", is_prime_number(-10)) # = False
  print("13 =", is_prime_number(13)) # = True
  print("23 =", is_prime_number(23)) # = True
  print("511 =", is_prime_number(511)) # = False
  print("160789903 =", is_prime_number(160789903)) # = False
  print("323 =", is_prime_number(323)) # = False
  print("1095672487 =", is_prime_number(1095672487)) # = False

  print("\nПроверка чисел от 1 до 100:", end = " ")
  
  for number in irange(1, 100):
    if (is_prime_number(number)): print(number, end = " ")
  print() # Добавляем конец строки в конце списка чисел.

# ------------------------------------------------------

# Основная функция, которая проверяет, является ли число простым.
def is_prime_number(number):

  if (number < 2): return False
  if (number == 2): return True
  if (number % 2 == 0): return False

  max_number = floor(sqrt(number)) # Поиск множителей только в диапазоне 2..sqrt(x).

  for divider in irange(3, max_number, 2): # Действуем с шагом 2, так как чётные множители нас не интересуют.
    if (number % divider == 0):
      return False
  
  return True

# ------------------------------------------------------

# Вспомогательная функция = inclusive range. По умолчанию в Python вторая граница диапазона (range) не включается в него.
def irange(start, end, step = 1):
  if step > 0:
    return range(start, end + 1, step)
  else:
    return range(start, end - 1, step)

# ------------------------------------------------------

main()