# В данной программе при переводе в двоичную и hex систему счисления будем использовать побитовые операторы.
# Деление на степень двойки (2^n): x >> n.
# Взятие остатка при делении на степень двойки (2^n): x & ((1 << n) - 1).

# ------------------------------------------------------

def main():
  print(f'Dec 250 = Hex {dec_to_hex("250")}')
  print(f'Hex DACA = Dec {hex_to_dec("DACA")}')
  print(f'Dec 1080 = Bin {dec_to_bin("1080")}')
  print(f'Bin 101010011001 = Dec {bin_to_dec("101010011001")}')

  print(f'Hex Color #FFE4C4 = RGB {hex_to_rgb("#FFE4C4")}')
  print(f'RGB Color (255, 228, 196) = Hex {rgb_to_hex((255, 228, 196))}')

# ------------------------------------------------------

# Вспомогательная функция, помогает конвертировать числа (10, 11, ...) в hex-литералы (A, B, ...).

def to_hex_char(number):
  hex_chars = ['A', 'B', 'C', 'D', 'E', 'F']
  if number >= 10:
    return hex_chars[number % 10]
  else:
    return str(number)

# ------------------------------------------------------

def dec_to_hex(str_number: str) -> str:
  dec = int(str_number)
  if (dec < 0):
    print("Перевод отрицательных чисел не поддерживается.")
    exit()
  
  result = [] # Работаем со списком, а не со string, потому что string при каждом изменении создаёт новый объект.
  
  while dec >= 16:
    digit = dec & ((1 << 4) - 1)
    dec = dec >> 4
    result.append(to_hex_char(digit))
  else:
    result.append(to_hex_char(dec))
  
  hex = "".join(result[::-1])
  return hex

# ------------------------------------------------------

def hex_to_dec(str_number: str) -> str:
  result_sum = 0

  hex_dict = { 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }

  for index in range(0, len(str_number)):
    ch = str_number[index]
    if ch.isalpha():
      result_sum += hex_dict[ch.upper()] << (4 * (len(str_number) - 1 - index))
    else:
      result_sum += int(ch) << (4 * (len(str_number) - 1 - index))
  
  return str(result_sum)

# ------------------------------------------------------

def dec_to_bin(str_number: str) -> str:
  dec = int(str_number)
  if (dec < 0):
    print("Перевод отрицательных чисел не поддерживается.")
    exit()
  
  result = []

  while dec >= 2:
    digit = dec & ((1 << 1) - 1)
    dec = dec >> 1
    result.append(str(digit))
  else:
    result.append(str(dec))
  
  bin = "".join(result[::-1])
  return bin

# ------------------------------------------------------

def bin_to_dec(str_number: str) -> str:
  result_sum = 0

  for index in range(0, len(str_number)):
    ch = str_number[index]
    result_sum += int(ch) << (1 * (len(str_number) - 1 - index))
  
  return str(result_sum)

# ------------------------------------------------------

def rgb_to_hex(rgb_color: tuple[int]) -> str:
  result = ""
  for x in rgb_color:
    result += dec_to_hex(x)
  return "#" + result

# ------------------------------------------------------

def hex_to_rgb(hex_color: str) -> tuple[int]:
  result = []
  hex_tuple = (hex_color[1:3], hex_color[3:5], hex_color[5:7])

  for x in hex_tuple:
    result.append(int(hex_to_dec(x)))
  
  return tuple(result)

# ------------------------------------------------------

main()