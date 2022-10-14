# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint
import itertools
k = int(input('Задайте натуральную степень k: '))
array = list([randint(0, 101) for i in range(k+1)])
if array[0] == 0:
    array[0] = randint(1, 101)
def get_array(k, array):
    str1 = ['x^']*(k-1) + ['x']
    newArray = [[a, b, c] for a, b, c  in itertools.zip_longest(array, str1, range(k, 1, -1), fillvalue = '') if a != 0]
    for x in newArray:
        x.append(' + ')
    newArray = list(itertools.chain(*newArray))
    newArray[-1] = ' = 0'
    return "".join(map(str, newArray)).replace('1x',' x')
list = get_array(k, array)
with open('task4.txt', 'w') as data:
    data.write(list)