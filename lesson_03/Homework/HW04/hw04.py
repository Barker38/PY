# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def des(num:int):
    list = []
    while num > 0:
        list.insert(0,num%2)
        num //= 2
    print(*list)
des(int(input()))