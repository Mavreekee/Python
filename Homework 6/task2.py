# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12

import random
a = int(input('Введите размер массива: '))
array = []
sum = 0

# for i in range(a):
#     array.append(random.randint(1, 10))
array = [random.randint(1, 10) for i in range(a)] #list comprehension

print(f'Исходный массив: {array}')
for i in range (a):
    if i % 2 != 0:
        sum = sum + array[i]
print(f'Сумма нечетных элементов = {sum}')