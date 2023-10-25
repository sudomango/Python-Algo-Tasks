def main():

  str_a = "Реверс"
  str_b = "Сервер"

  print("\n" + str_a)
  print(str_b)
  print(f"Являются ли эти строки анаграммами? Ответ: {'Да' if is_anagram(str_a, str_b) else 'Нет'}.")

  str_c = "Полотно навсегда останется свежим"
  str_d = "А всегда ли свет стекает сквозь жалюзи"

  print("\n" + str_c)
  print(str_d)
  print(f"Являются ли эти строки анаграммами? Ответ: {'Да' if is_anagram(str_c, str_d) else 'Нет'}.")

  str_e = "Ракета"
  str_f = "Карета"

  print("\n" + str_e)
  print(str_f)
  print(f"Являются ли эти строки анаграммами? Ответ: {'Да' if is_anagram(str_e, str_f) else 'Нет'}.")

  str_g = "Мангуст"
  str_h = "Мустанг"

  print("\n" + str_g)
  print(str_h)
  print(f"Являются ли эти строки анаграммами? Ответ: {'Да' if is_anagram(str_g, str_h) else 'Нет'}.")

# ----------------

def is_anagram(text_a, text_b):
  # Переводим обе строки в одинаковый регистр (например, нижний).
  text_a_lower = text_a.lower()
  text_b_lower = text_b.lower()

  # Составляем из каждой строки множество, чтобы потом не проверять повторяющиеся буквы.
  text_a_set = set(text_a_lower)
  text_b_set = set(text_b_lower)

  # Нужно очистить множества от всего, кроме значащих символов.
  remove_chars = (' ', '.', ',', '-', '\'', '?', '!')

  for ch in remove_chars:
    text_a_set.discard(ch)
    text_b_set.discard(ch)

  # Здесь уже сравниваем сами множества, и количество вхождений каждой буквы в исходные строки.
  if text_a_set == text_b_set:
    for letter in text_a_set:
      if text_a_lower.count(letter) != text_b_lower.count(letter):
        return False
    else:
      return True # Если цикл прошёлся по всем буквам множества и False ни разу не выпал, тогда всё совпадает.
  else:
    return False # Если множества содержат разные элементы, то и смысла проверять что-то дополнительно нет.

# ----------------

# Альтернативная реализация задачи с помощью другого алгоритма.

def is_anagram_second(text_a, text_b):
  text_a_list = list(text_a.lower())
  text_b_list = list(text_b.lower())

  # Оставляем в списках только буквы и числа.
  text_a_list = list(filter(lambda ch: ch.isalpha() or ch.isdigit(), text_a_list))
  text_b_list = list(filter(lambda ch: ch.isalpha() or ch.isdigit(), text_b_list))

  # Сортируем оба списка, и проверяем, получились ли эти списки одинаковыми.
  text_a_list.sort()
  text_b_list.sort()

  return text_a_list == text_b_list

# ----------------

main()