from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


r_kb = InlineKeyboardMarkup()
r_kb.add(InlineKeyboardButton('меню', callback_data='menu'))

async def Big(message: types.Message):
    '''
    menu ramen
    '''
    photo1 = open('images/b1.jpg', 'rb')
    await message.answer(text='большая порция')
    await message.answer_photo(photo1)
    await message.answer(text='ramen №1', reply_markup=r_kb)



async def Normal(message: types.Message):
    '''
        menu ramen
    '''
    photo2 = open('images/b2.jpg', 'rb')
    await message.answer(text='среднее порция')
    await message.answer_photo(photo2)
    await message.answer(text='ramen №2', reply_markup=r_kb)



async def F_kids(message: types.Message):

    photo3 = open('images/b3.jpg', 'rb')

    await message.answer(text='для малышей')
    await message.answer_photo(photo3)
    await message.answer(text='ramen №3', reply_markup=r_kb)

