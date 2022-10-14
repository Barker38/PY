# 4. * Задана натуральная степень k. Сформировать случайным образом
#      список коэффициентов (от 0 до 10) многочлена, записать в файл

from random import choice


def CreatePoly(num: int):
    if num < 1:
        return 0

    poly = ""
    num_list = range(0, 10)

    with open("poly.txt", "a", encoding="utf-8") as file:
        for i in range(num, 0, -1):
            value = choice(num_list)
            if value:
                poly += f"{value}*x^{i} {choice('+-')} "

        file.write(f"{poly}{choice(num_list)} = 0\n")


CreatePoly(int(input()))