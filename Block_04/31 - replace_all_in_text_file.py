content = ""

with open("../resources/Half-Life Replace.txt", "r", encoding = "UTF-8") as read_file:

  content = read_file.read()
  content = content.replace("Игр", "Rooock!")
  content = content.replace("игр", "Rooock!")

with open("../resources/Half-Life Replaced.txt", "w", encoding = "UTF-8") as write_file:

  write_file.write(content)