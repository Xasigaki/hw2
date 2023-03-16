from aiogram import types


"""
    это функция чтоб бот показывал какие функции в боте есть
"""

async def help_command(message: types.Message):
    await message.answer(text=f'СПИСОК КОМАНД ЭТОГО БОТА:\n/start->начало беседы\n/help->список всех команд\
    \n/myinfo->информация о пользователе\n/picture->рандомная картинка\n/menu->вывод меню')
    await message.delete()