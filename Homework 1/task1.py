# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

numday = int(input('Введите № дня недели: '))
if numday > 7 or numday < 1:
    print('Дни недели - это массив целых чисел от 1 до 7')
elif numday == 6 or numday == 7:
    print(numday, '- это выходной')
else:
    print(numday, '- будний день')