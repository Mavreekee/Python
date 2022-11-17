from aiogram import types
from create_bot import bot

async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет! Сегодня будем делить конфеты'
                                                 f', вот тебе немного моих команд:'
                                                 f'\n/play - начать игру (но сначала все настрой);'                                                 
                                                 f'\n/set ... - так можно изменить количество конфет;'
                                                 f'\n/setone ... - так можно изменить количество конфет,'
                                                 f' которые можно взять за один ход;'
                                                 f'\n/level ... - так можно выбрать уровень сложности бота'
                                                 f' (1 - hard, 2 - easy)')                                                 