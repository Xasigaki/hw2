from aiogram import types

async def adress(cb: types.CallbackQuery):
    '''
    Функция показывает улицу
    '''
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='деревня-КОНОХА'
    )