# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти: '))
if a == 1:
    print('I четверть: x = (0 ; +∞], y = (0 ; +∞]') 
elif a == 2:
    print('II четверть: x = (0 ; -∞], y = (0 ; +∞]')  
elif a == 3:
    print('III четверть: x = (0 ; -∞], y = (0 ; -∞]')
elif a == 4:
    print('IV четверть: x = (0 ; +∞], y = (0 ; -∞]')
else:
    print('Такой четверти нет, их всего 4 (I, II, III, IV)')