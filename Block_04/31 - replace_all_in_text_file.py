import os

content = ""
path_to_file = os.path.dirname(__file__) + "/../resources/Half-Life Replace.txt"

with open(path_to_file, "r", encoding="UTF-8") as read_file:

    content = read_file.read()
    content = content.replace("Игр", "Rooock!")
    content = content.replace("игр", "Rooock!")

with open(path_to_file, "w", encoding="UTF-8") as write_file:

    write_file.write(content)