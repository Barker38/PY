
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

n = int (input('Enter the value of N: '))
position_one = int (input("Position one: "))
position_two = int (input("Position two: "))

list = [i for i in range(-n,n+1)]
math = list[position_one-1] * list [position_two-1]
print(list)
print(math)