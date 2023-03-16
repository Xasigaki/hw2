import random
import os
from aiogram import types
"""
    это функция чтоб бот скидывал фото
"""
async def image_send(message: types.Message):
    await message.answer_photo(
        photo=open('image/' + random.choice(os.listdir('images')), 'rb')
    )
    await message.delete()

