# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")

# find_txt = "абв"
# res = [i for i in txt.split() if find_txt not in i]
res = list(filter(lambda x: x != 'абв', txt.split())) #filter and lambda

print(f'Результат: {" ".join(res)}')