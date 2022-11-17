import asyncio
import random

import view
from create_bot import dp
from aiogram import types

import model
from create_bot import bot

async def start0(message: types.Message):
    player = message.from_user
    model.set_player(player)
    await view.hello(message)

async def start1(message: types.Message):
    player = message.from_user
    model.set_player(player)
    dp.register_message_handler(player_turn)
    first_turn = random.randint(0,1)
    if first_turn == 0:
        await bot.send_message(message.from_user.id, f'Результаты жеребьевки - начинает бот')
    else:
        await bot.send_message(message.from_user.id, f'Результаты жеребьевки - начинаешь ты')
    if first_turn:
        await await_player(player)
    else:
        await enemy_turn(player)

async def player_turn(message: types.Message):
    player = message.from_user
    model.set_player(player)
    max_take = model.get_max_take()
    if (message.text).isdigit():
        if 0 < int(message.text) < (max_take + 1):
            total_count = model.get_total_candies()
            player_take = int(message.text)
            total = total_count - player_take
            await bot.send_message(player.id, f'{player.first_name} взял {player_take} конфет, и на столе осталось {total}')
            if model.check_win(total):
                await bot.send_message(player.id, f'Победил {player.first_name}!')
                return
            model.set_total_candies(total)
            await enemy_turn(player)
        if int(message.text) == 0:
            await bot.send_message(message.from_user.id, '0 - круто, но так нельзя')            
        if int(message.text) > max_take:
            await bot.send_message(message.from_user.id, 'Не много ли?')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, количество измеряется в цифрах'
                                                     f' и точно должно быть > 0, попробуй еще раз')

async def enemy_turn(player):
    total_count = model.get_total_candies()
    max_take = model.get_max_take()
    level = model.get_level()
    if level == 1:
        if total_count < (max_take + 1):
            enemy_take = total_count
        else:
            enemy_take = (total_count - 1)%max_take
    if level == 2:
        if total_count < (max_take + 1):
            enemy_take = random.randint(1,(total_count + 1))
        else:
            enemy_take = random.randint(1,(max_take + 1))
    total = total_count - enemy_take
    await bot.send_message(player.id, f'Бот взял {enemy_take} конфет, и на столе осталось {total}')
    if model.check_win(total):
        await bot.send_message(player.id, f'{player.first_name}, бот победил, а ты - нет')
        return
    model.set_total_candies(total)
    await asyncio.sleep(1)
    await await_player(player)

async def await_player(player):
    max_take = model.get_max_take()
    await bot.send_message(player.id, f'{player.first_name}, бери конфеты, но не > {max_take}')

async def set_total_candies(message: types.Message):
    count = int((message.text).split(" ")[1])
    model.set_total_candies(count)
    await bot.send_message(message.from_user.id, f'Максимально количество конфет изменено на {count}')

async def set_max_take(message: types.Message):
    count = int((message.text).split(" ")[1])
    model.set_max_take(count)
    await bot.send_message(message.from_user.id, f'Максимально количество конфет, которое можно взять за один ход'
                                                 f' изменено на {count}')

async def set_level(message: types.Message):
    count = int((message.text).split(" ")[1])
    model.set_level(count)
    if count == 1:
        await bot.send_message(message.from_user.id, f'Будешь биться с ботом уровня hard')
    else:
        await bot.send_message(message.from_user.id, f'Будешь биться с ботом уровня easy')