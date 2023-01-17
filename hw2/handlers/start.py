from aiogram import types
from handlers import constans
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(InlineKeyboardButton('меню', callback_data='menu'),
             InlineKeyboardButton('адрес', callback_data='adress')
             )


async def start_command(message: types.Message):
    '''
    Функция для запуска бота и перехода к его командам
    '''
    await message.answer(text=constans.START_BOT,
                         reply_markup=start_kb
                         )
