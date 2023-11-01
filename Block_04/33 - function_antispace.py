# Утилита для удаления случайных лишних пробелов в конце строк в исходном коде.

file = input("Вставьте название или путь до файла (с расширением и без кавычек): ")

with open(file, "r", encoding="UTF-8") as source_file:

    content = source_file.read()
    content_list = content.splitlines()

    for i in range(0, len(content_list)):
        if len(content_list[i]) > 0:
            content_list[i] = content_list[i].rstrip(" ")

with open(file, "w", encoding="UTF-8") as write_file:

    content = "\n".join(content_list)
    write_file.write(content)