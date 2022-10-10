# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

import random
a = int(input('Введите размер массива: '))
array1 = []
array2 = []
b = 1
for i in range(a):
    array1.append(random.randint(1, 10))
print(f'Исходный массив: {array1}')
if a % 2 == 0:
    for i in range(a // 2):
        array2.append(array1[i] * array1[len(array1) - b])
        b = b + 1
else:
    for i in range((a + 1) // 2):
        array2.append(array1[i] * array1[len(array1) - b])
        b = b + 1
print(f'Массив произведений пар чисел: {array2}')