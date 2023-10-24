import re

with open("../resources/Half-Life Replace.txt", "r", encoding = "UTF-8") as read_file:
  content = read_file.read()

  words = re.findall(r"\b\w+[\-‑]?\w*\b", content, flags = re.I | re.U | re.M)

  words.sort(key = len)
  words = tuple(map(lambda a: a.lower(), words)) # Для верности переводим все слова в нижний регистр.

  # Чтобы слова в результате не повторялись, используем множество вместо списка и кортежа.
  shortest = set(filter(lambda x: len(x) == len(words[0]), words))
  longest = set(filter(lambda s: len(s) == len(words[-1]), words))

  print("Longest words(s) in the text:", longest)
  print("Shortest word(s) in the text:", shortest)