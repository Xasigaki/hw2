import random
import os
"""
    это для импорта из аиограмма и питон-дотенва
"""
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv


load_dotenv()
bot = Bot(getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


"""
    это функция для старта бота
"""
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=f"OHAIO, {message.from_user.first_name}, I'm MONKEY D LUFFY")
    await message.delete()

"""
    это функция чтоб узнать инфо о себе
"""
@dp.message_handler(commands=['myinfo'])
async def echo(message: types.Message):
    await message.answer(text=f'your id ->{message.from_user.id},name->{message.from_user.first_name},username->{message.from_user.username}')
    await message.delete()



"""
    это функция чтоб бот показывал какие функции в боте есть
"""
@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    await message.answer(text=f'СПИСОК КОМАНД ЭТОГО БОТА:\n/start->начало беседы\n/help->список всех команд\
    \n/myinfo->информация о пользователе\n/picture->рандомная картинка')
    await message.delete()

"""
    это функция чтоб бот скидывал фото
"""
@dp.message_handler(commands=['picture'])
async def image_send(message: types.Message):
    await message.answer_photo(
        photo=open('images/' + random.choice(os.listdir('images')), 'rb')
    )
    await message.delete()





@dp.message_handler()
async def echo(message: types.Message):
    letters = message.text.split(' ')
    if len(letters) >= 3:
        await message.answer(message.text.upper())
    else:
        await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)







