# Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random

import random
a = int(input('Введите N: '))
array = []
repeat = [0] * 100
for i in range(a):
    array.append(random.randint(1, 99))
    repeat[array[i]] = repeat[array[i]] + 1
    while repeat[array[i]] > 1:
        array[i] = random.randint(1, 99)
print(f'Исходный массив: {array}')
for i, value in enumerate(array):
    swap = random.randint(i, len(array) - 1)
    array[i], array[swap] = array[swap], value
print(f'Массив после перемешивания: {array}')