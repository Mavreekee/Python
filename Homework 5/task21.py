from random import *
import os

rules = ('Сегодня поиграем с конфетками :)\n'
        'Правила:\n'
        'Есть 150 конфет, вы берете их по очереди,\n'
        'за один раз можно взять не больше 28 конфет.\n'
        'Выигрывает тот, кто последним ходом заберет все конфеты.')
print(rules)

message = ['Твоя очередь,', 'Бери еще,', 'Можешь взять еще,','Бери быстрее,', 'Да, еще бери']

def player_vs_player():
    candies_total = 150
    max_take = 28
    count = 0
    player_1 = input('\nКак тебя зовут? ')
    player_2 = input('\nА тебя? ')

    print('\nДля начала опеределим, кто начнет игру.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю, {lucky}, ты ходишь первым!')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nМожно взять только {max_take} конфет, {lucky}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОсталось еще: {candies_total} конфет')
            count = 1
        else:
            print('Всё, конфет больше нет')

        if count == 1:
            step = int(input(f'\n{choice(message)} {loser} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nМожно взять только {max_take} конфет, {loser}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОсталось еще {candies_total}, конфет')
            count = 0

    if count == 1:
        print(f'{loser} победил!')
    if count == 0:
        print(f'{lucky} победил!')

player_vs_player()