from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text


start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(
    InlineKeyboardButton('Menu', callback_data='menu_command'),
    InlineKeyboardButton('Adress', callback_data='adress')
)



async def adress(cb:types.CallbackQuery):
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text=f"Region:Issyk-Kol, city-Karakol,\n street-Toktogul, cross street-Lenin,\n Named=ICHIRAKU RAMEN",
    )
    await cb.bot.send_photo(
        chat_id=cb.from_user.id,
        photo=open('handlers/images/rrr.jpg', 'rb'),
    )







"""
    это функция для старта бота
"""

async def start_command(message: types.Message):
    await message.answer(text=f"OHAIO, {message.from_user.first_name}, I'm MONKEY D LUFFY",
                         reply_markup=start_kb)
    await message.delete()





async def echo(message: types.Message):
    letters = message.text.split(' ')
    if len(letters) >= 3:
        await message.answer(message.text.upper())
    else:
        await message.answer(message.text)