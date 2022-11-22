import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b, c, d, e):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

k = [-12, -18, 5, 10, -30]
limit = [-10, 10]
x = np.arange(limit[0], limit[1], 0.01)
color = 'r'
change = []
root = []
root_out = []
func_direct = -1

def change_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color

for i in range(len(x) - 1):
    if func_direct == -1:
        if func(x[i], *k) < func(x[i+1], *k):
            func_direct = 1
            change.append((x[i], func(x[i], *k)))
    else:
        if func(x[i], *k) > func(x[i+1], *k):
            func_direct = -1
            change.append((x[i], func(x[i], *k)))

for i in range(len(x) - 1):
    if (func(x[i], *k) > 0 and func(x[i+1], *k) < 0) or (func(x[i], *k) < 0 and func(x[i+1], *k) > 0):
        root.append((x[i], func(x[i], *k)))
        root_out.append(round(x[i], 2))

cur = np.arange(limit[0], change[0][0], 0.1)
plt.plot(cur, func(cur, *k), change_color())
for i in range(len(change) - 1):
    cur = np.arange(change[i][0], change[i+1][0], 0.1)
    plt.plot(cur, func(cur, *k), change_color())
cur = np.arange(change[-1][0], limit[1], 0.1)
plt.plot(cur, func(cur, *k), change_color())

for cur in root:
    plt.plot(cur[0], func(cur[0], *k), 'gx')

plt.grid(visible=True)

plt.title(f'Корни функции: {root_out}'
          f'\nОстальные параметры визуально определимы')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.plot(0, 0, 'r', label="убывание")
plt.plot(0, 0, 'b', label="возрастание")
plt.legend()
plt.show()