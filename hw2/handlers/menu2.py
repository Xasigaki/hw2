from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    KeyboardButton('BIG'),
    KeyboardButton('NORMAL'),
    KeyboardButton('FOR KIDS')
)

async def buy_command(cb: types.CallbackQuery):
    '''
    Функция для выбора порции
    '''
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Выберите порцию',
        reply_markup=menu
    )
