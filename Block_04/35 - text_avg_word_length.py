import re, os

path_to_file = os.path.dirname(__file__) + "/../resources/some_plain_text.txt"

with open(path_to_file, "r", encoding="UTF-8") as file:
    content = file.read()

# Очищаем слова в тексте от посторонних символов, типа знаков препинания (с помощью регулярного выражения).
words = re.findall(r"\b\w+[\-‑]?\w*\b", content, flags=re.I | re.U | re.M)

if len(words) < 1:
    print("Кажется, вы указали пустой файл. Мне нечего считать.")
    exit()

# Можно распечатать список слов, чтобы убедиться, что ничего лишнего в него не попало.
# print(words, "\n", sep = "")

total_letters = 0

for word in words:
    total_letters += len(word)

avg_length = total_letters / len(words)


def correct_text_output(number):
    if number in range(11, 15):
        return "символов"

    if number % 10 == 1:
        return "символ"
    elif number % 10 in (2, 3, 4):
        return "символа"
    else:
        return "символов"


print(f"Средняя длина слова в тексте составляет {avg_length:.2f} {correct_text_output(int(avg_length))}.")