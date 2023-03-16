from aiogram import types

"""
    это функция чтоб узнать инфо о себе
"""
async def my_info(message: types.Message):
    await message.answer(text=f'your id ->{message.from_user.id},name->{message.from_user.first_name},username->{message.from_user.username}')
    await message.delete()
