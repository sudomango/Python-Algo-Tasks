def main():
  orig_string = ""

  with open("../resources/long_string.txt", "r", encoding = "UTF-8") as file:
    orig_string = file.read()

  print("Оригинальная строка:\n", orig_string, sep = "")
  user_input = input("\nУкажите, какой символ (подстроку) мы ищем в строке: ").lower()

  elem_count = orig_string.lower().count(user_input)
  # Примечание: этот же метод (count) справедлив и для поиска количества элементов в списке (массиве).

  print(f"Было найдено {elem_count} {correct_text_output(elem_count)} символа (подстроки) \"{user_input}\".")

# ----------------

def correct_text_output(number):
  if (number in range(11, 15)):
    return "вхождений"

  if (number % 10 == 1):
    return "вхождение"
  elif (number % 10 in (2, 3, 4)):
    return "вхождения"
  else:
    return "вхождений"

# ----------------

main()