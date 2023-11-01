def main():
    sum_a = {"rub": 102, "kop": 36}
    sum_b = {"rub": 49, "kop": 55}

    print(f"Первая сумма = {sum_a['rub']} руб. {sum_a['kop']} коп.")
    print(f"Вторая сумма = {sum_b['rub']} руб. {sum_b['kop']} коп.")

    result_add = money_add(sum_a, sum_b)
    result_sub = money_sub(sum_a, sum_b)

    print(f"Результат сложения двух сумм равен = {result_add['rub']} руб. {result_add['kop']} коп.")
    print(f"Результат вычитания двух сумм равен = {result_sub['rub']} руб. {result_sub['kop']} коп.")


def money_add(dict_a, dict_b):
    res_kop = dict_a["kop"] + dict_b["kop"]
    memory = 0
    if res_kop >= 100:
        memory = 1
        res_kop -= 100

    res_rub = dict_a["rub"] + dict_b["rub"] + memory

    return {"rub": res_rub, "kop": res_kop}


def money_sub(dict_a, dict_b):
    minus_flag = 0  # Отражает, нужно ли будет в конце добавить минус перед результатом.

    if dict_a["rub"] < dict_b["rub"]:
        minus_flag = 1
        dict_a, dict_b = dict_b, dict_a

    res_kop = dict_a["kop"] - dict_b["kop"]
    memory = 0
    if res_kop < 0:
        memory = 1
        res_kop += 100

    res_rub = dict_a["rub"] - dict_b["rub"] - memory

    return {"rub": res_rub if not minus_flag else -res_rub, "kop": res_kop}


main()