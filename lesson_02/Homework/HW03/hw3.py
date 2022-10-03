# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = int(input("Задайте n: "))
list = [round((1+1/(n+1))**(n+1)) for n in range(num)]
print (f"{list} -> {sum(list)}")