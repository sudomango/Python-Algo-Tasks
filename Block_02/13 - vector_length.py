import math

def vector_length(x, y, z):
  return math.sqrt((x ** 2) + (y ** 2) + (z ** 2))

# Запрашиваем координаты у пользователя.
coord_x = float(input("Введите x-координату вектора: "))
coord_y = float(input("Введите y-координату вектора: "))
coord_z = float(input("Введите z-координату вектора: "))

result = vector_length(coord_x, coord_y, coord_z)

print(f"Длина вектора с координатами x = {coord_x}, y = {coord_y}, z = {coord_z} равна {result:.5f}.")