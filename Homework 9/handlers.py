from aiogram import types, Dispatcher

import commands

def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start0, commands=['start'])
    dp.register_message_handler(commands.start1, commands=['play'])
    dp.register_message_handler(commands.set_total_candies, commands=['set'])
    dp.register_message_handler(commands.set_max_take, commands=['setone'])
    dp.register_message_handler(commands.set_level, commands=['level'])
    # dp.register_message_handler(commands.player_turn)