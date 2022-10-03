# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def numbers(N):
    number = 1
    for i in range(N):
        result = number * i
        print(result)



def factorial(number):
    factorial = 1
    while number != 1:
        factorial = factorial * number
        number = number - 1
    return factorial

num = int(input('Enter a number: '))
list = [factorial(i + 1) for i in range(num)]


print(f'{num} -> {list}')



