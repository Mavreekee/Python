# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
a = int(input('Введите длину массива: '))
array = []
max = 0
min = 1
for i in range(a):
    array.append(round(random.uniform(0, 10), 2))
print(f'Исходный массив: {array}')
for i in array:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(f'Разница между max и min значением дробной части элементов = {(round((max), 2)) - (round((min), 2))}')