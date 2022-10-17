# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d или 11a3b7c1d => aaaaaaaaaaabbbcccccccd

import random

def random_data1():
    count1 = 0
    count2 = 0
    count3 = 0
    while count1 == 0 or count2 == 0 or count3 == 0:
        a = random.randint(10, 25)
        b = random.randint(1, 5)
        c = random.randint(6, 9)
        array = []
        for i in range(a):
            if i <= b:
                array.append('a')
            elif (a - c) >= i > b:
                array.append('b')
            elif (a - b) >= i > (a - c):
                array.append('c')
            else:
                array.append('d')
        for i in range(a):
            if array[i] == 'b':
                count1 = count1 + 1
            if array[i] == 'c':
                count2 = count2 + 1
            if array[i] == 'd':
                count3 = count3 + 1
    return array

def random_data2(array):
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    for i in range(len(array)):
        if array[i] == 'a':
            a_count = a_count + 1
        elif array[i] == 'b':
            b_count = b_count + 1
        elif array[i] == 'c':
            c_count = c_count + 1
        else:
            d_count = d_count + 1
    array = [f'{a_count}a{b_count}b{c_count}c{d_count}d']
    return array

def unzip(array_str):
    a = ''
    b = ''
    for i in range(len(array_str)):
        if not array_str[i].isalpha():
            a += array_str[i]
        else:
            b = b + array_str[i] * int(a)
            a = ''
    return b

choice1 = int(input('Будем сжимать (0) или восстанавливать (1)? Введи 0 или 1\n'))
if choice1 == 0:
    choice2 = int(input('Окей, будем сжимать. Данные мне сформировать (0) или ты сам (1)? Введи 0 или 1\n'))
    if choice2 == 0:
        array = random_data1()
        array_str = ''.join(array)
        print(f'Я сформировал, смотри что получилось: {array_str}')
        print('Входные данные я записал в файл in.txt, можешь проверить')
        with open('in.txt', 'w') as file:
            file.write(array_str)
        array_str1 = ''.join(random_data2(array))
        print(f'Результат RLE алгоритма: {array_str} => {array_str1}')
        print('Выходные данные я записал в файл out.txt, можешь проверить')
        with open('out.txt', 'w') as file:
            file.write(array_str1)
    else:
        array = input("Введи данные, например, abbccddd (обязательно по алфавиту)\n")
        array_str = list(array)
        print(f'Посмотри, что у тебя получилось: {array}')
        print('Входные данные я записал в файл in.txt, можешь проверить')
        with open('in.txt', 'w') as file:
            file.write(array)
        array_str1 = ''.join(random_data2(array_str))
        print(f'Результат RLE алгоритма: {array} => {array_str1}')
        print('Выходные данные я записал в файл out.txt, можешь проверить')
        with open('out.txt', 'w') as file:
            file.write(array_str1)
else:
    choice2 = int(input('Окей, будем восстанавливать. Данные мне сформировать (0) или ты сам (1)? Введи 0 или 1\n'))
    if choice2 == 0:
        array = random_data2(random_data1())
        array_str = ''.join(array)
        print(f'Я сформировал, смотри что получилось: {array_str}')
        print('Входные данные я записал в файл in.txt, можешь проверить')
        with open('in.txt', 'w') as file:
            file.write(array_str)
        array_str1 = ''.join(unzip(array_str))
        print(f'Результат RLE алгоритма: {array_str} => {array_str1}')
        print('Выходные данные я записал в файл out.txt, можешь проверить')
        with open('out.txt', 'w') as file:
            file.write(array_str1)
    else:
        array = input("Введи данные, например, 1a2b2c3d (обязательно по алфавиту)\n")
        array_str = list(array)
        print(f'Посмотри, что у тебя получилось: {array}')
        print('Входные данные я записал в файл in.txt, можешь проверить')
        with open('in.txt', 'w') as file:
            file.write(array)
        array_str1 = ''.join(unzip(array_str))
        print(f'Результат RLE алгоритма: {array} => {array_str1}')
        print('Выходные данные я записал в файл out.txt, можешь проверить')
        with open('out.txt', 'w') as file:
            file.write(array_str1)