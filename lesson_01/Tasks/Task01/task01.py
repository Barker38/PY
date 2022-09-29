def array(m):


    x = [ ]
    for i in range(m):
            a = int(input(f'Введите x{i + 1}: '))
    x.append(a)

    return x


def max_el(array):


    maxim = 0

    for i in range(len(array)):
     if array[i] > array[maxim]:
        maxim = i
    return array[maxim]

l = int(input('Введите количество элементов: '))
new_array = array(l)
maxim = max_el(new_array)
print(f'Максимальный элемент: {maxim}')
