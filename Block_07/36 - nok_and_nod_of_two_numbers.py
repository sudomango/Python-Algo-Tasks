def main():
  number_a = int(input("Введите первое натуральное число: "))
  number_b = int(input("Введите второе натуральное число: "))

  print(f"\nНОД двух чисел {number_a} и {number_b} будет равен {find_nod(number_a, number_b)}.")
  print(f"НОК двух чисел {number_a} и {number_b} будет равен {find_nok(number_a, number_b)}.")

# ----------------

# Находим НОД, используя Алгоритм Евклида: Всегда делим большее число на меньшее до тех пор, пока одно из них не разделится на другое без остатка.

def find_nod(num_a, num_b):

  while num_a != 0 and num_b != 0:
    if num_a > num_b:
      num_a = num_a % num_b
    elif num_a < num_b:
      num_b = num_b % num_a
    else:
      return num_a # Если оба числа равны, то одно из них - точно НОД.

  return (num_a + num_b) # Одно из них будет равно 0 (условие выхода из цикла), поэтому фактически мы возвращаем только одно число.
  # Альтернативные варианты: max(num_a, num_b) и num_a if num_a > num_b else num_b.

# Примечание: Кстати, в Python есть встроенная функция для нахождения НОД двух чисел: math.gcd(a, b).

# ----------------

# Есть ещё алгоритм нахождения НОД через вычитание. Принцип в целом довольно похож на Алгоритм Евклида.

def find_gcd(num_a, num_b):

  while num_a != num_b:
    if num_a > num_b:
      num_a = num_a - num_b
    else:
      num_b = num_b - num_a

  return num_a # Так как равенство num_a и num_b - это условие выхода из цикла, то нам всё равно какое из них возвращать.

# ----------------

# Для вычисления НОК существует формула: НОК(a, b) = a * b / gcd(a, b).

def find_nok(num_a, num_b):
  return num_a * num_b // find_gcd(num_a, num_b)

# ----------------

main()