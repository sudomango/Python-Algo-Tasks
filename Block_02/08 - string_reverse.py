import sys
sys.path.append("..")

import useful_functions as useful

def main():
  print(string_reverse("Hello, World!"))
  print(string_reverse(string_reverse("Hello, Python!")))
  print(string_reverse("Функция генерирует массив случайных чисел"))

# ------------------------------------------------------

def string_reverse(text):
  result_string = ""
  for index in useful.irange(len(text) - 1, 0, -1):
    result_string += text[index]
  return result_string

# Конечно, адекватным вариантом будет использовать slicing: string[::-1].

# ------------------------------------------------------

main()