def main():
  text_a = "This is unusual string"
  text_b = "А эта строка совершенно обыкновенная"

  print(text_a, text_b, sep=" -/- ")

  # List Unpacking и Tuple Unpacking всё ещё хорошо работают.
  text_a, text_b = (text_b, text_a)
  print(text_a, text_b, sep=" -/- ")

  # Можно также определить сложение и вычитание двух строк на манер того, что мы делали с числами.
  (text_a, text_b) = swap_strings(text_a, text_b)
  print(text_a, text_b, sep=" -/- ")

# ----------------

def swap_strings(str_a, str_b):
  str_a = str_a + str_b
  str_b = str_a[:str_a.rfind(str_b)]
  str_a = str_a[len(str_b):]
  return (str_a, str_b)

# ----------------

main()