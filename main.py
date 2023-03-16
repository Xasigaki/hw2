
"""
    это для импорта из аиограмма и питон-дотенва
"""
from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from os import getenv
from handlers.start import start_command, echo, adress
from handlers.menu import menu_command
from handlers.my_info import my_info
from handlers.help import help_command
from handlers.photo import image_send
from handlers.ramen import r_big
from handlers.ramen import r_norm
from handlers.ramen import f_kds





load_dotenv()
bot = Bot(getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
dp.register_message_handler(start_command, commands=['start'])
dp.register_message_handler(my_info, commands=['myinfo'])
dp.register_message_handler(help_command, commands=['help'])
dp.register_message_handler(image_send, commands=['picture'])
dp.register_callback_query_handler(adress, text='adress')
dp.register_callback_query_handler(menu_command, text='menu')
dp.register_message_handler(r_big, Text(equals='Big'))
dp.register_message_handler(r_norm, Text(equals='Normal'))
dp.register_message_handler(f_kds, Text(equals='For_kids'))
dp.register_message_handler(echo)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)







