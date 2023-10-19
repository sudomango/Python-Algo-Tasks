from datetime import datetime, timedelta

# ------------------------------------------------------

def main():

  products = [
    ["Banana", datetime(2023, 6, 12), "60 days"],
    ["Apples", datetime(2023, 8, 23), "80 days"],
    ["Juice", datetime(2023, 3, 10), "120 days"],
    ["Butter", datetime(2023, 7, 18), "60 days"],
    ["Coca-Cola", datetime(2023, 1, 8), "360 days"]
  ]

  date_now = datetime(2023, 9, 10)

  # Проверяем каждый продукт в списке на свежесть.
  for pr in products:
    fresh = is_still_fresh(pr, date_now)
    print(f"Продукт = {pr[0]}, Свежий = {fresh}")

# ------------------------------------------------------

def is_still_fresh(product, today):
  plus_days = int(product[2].split()[0]) # Получаем количество дней в сроке годности.
  start_date = product[1]
  end_date = start_date + timedelta(days = plus_days) # Прибавляем количество дней к дате изготовления.

  if end_date < today:
    return False
  else:
    return True

# ------------------------------------------------------

main()