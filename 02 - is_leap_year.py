def main():
  year = int(input("Введите желаемый год для проверки: "))
    
  # Использование тернарного оператора.
  is_leap = "Високосный" if is_leap_year(year) else "Не високосный"
  print(f"{year}-й год = {is_leap}.")

# ------------------------------------------------------

def is_leap_year(year):
  if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    return True
  else:
    return False

# ------------------------------------------------------

main()