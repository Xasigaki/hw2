from aiogram import types
from aiogram.dispatcher.filters import Text


async def r_big(message: types.Message):
    await message.answer(text='Пожалуйста! Большая порция!')
    await message.answer_photo(open(f'handlers/images/b1.jpg', 'rb')),
    await message.answer(text='цена=599(cом)')





async def r_norm(message: types.Message):
    await message.answer(text='Пожалуйста! Средняя порция!')
    await message.answer_photo(open(f'handlers/images/b2.jpg', 'rb')),
    await message.answer(text='цена=299(cом)')





async def f_kds(message: types.Message):
    await message.answer(text='Пожалуйста! Средняя порция!')
    await message.answer_photo(open(f'handlers/images/b3.jpg', 'rb')),
    await message.answer(text='цена=199(cом)')

















