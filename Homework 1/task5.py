# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите х1= '))
y1 = int(input('Введите y1= '))
x2 = int(input('Введите х2= '))
y2 = int(input('Введите y2= '))
x = (x1 - x2)**2
y = (y1 - y2)**2
a = (x + y)**0.5
print(round(a, 2))