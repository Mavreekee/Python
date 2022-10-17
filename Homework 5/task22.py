from random import *
import os

rules = ('Сегодня поиграем с конфетками :)\n'
        'Правила:\n'
        'Есть 150 конфет, вы берете их по очереди,\n'
        'за один раз можно взять не больше 28 конфет.\n'
        'Выигрывает тот, кто последним ходом заберет все конфеты.')
print(rules)

message = ['Твоя очередь', 'Бери еще', 'Можешь взять еще','Бери быстрее', 'Да, еще бери']

def player_vs_bot():
    candies_total = 150
    max_take = 28
    player_1 = input('\nКак тебя зовут? ')
    player_2 = 'БОТ'
    players = [player_1, player_2]
    print('\nДля начала опеределим, кто начнет игру.\n')

    lucky = randint(-1, 0)

    print(f'Поздравляю, {players[lucky+1]}, ты ходишь первым!')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'БОТ':
            print(f'\nХодит {players[lucky%2]} \nОсталось {candies_total} конфет. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nТвой ход, {players[lucky%2]} \nОсталось {candies_total} конфет. \n{choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'Осталось {candies_total} конфет. \nПобедил {players[lucky%2]}')

player_vs_bot()