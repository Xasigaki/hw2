from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.add(
    KeyboardButton('Big'),
    KeyboardButton('Normal'),
    KeyboardButton('For_kids')
)

async def menu_command(cb:types.CallbackQuery):
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text=f'выберите порцию!!!',
        reply_markup=menu_kb
    )
    await message.delete()

