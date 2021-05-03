import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
#import config as cfg #файл с созданием директории бд
#import utilis as utls 

conn = sqlite3.connect("language.db") #подключение базы данных?
cursor = conn.cursor() #создание cursor объекта

bot = Bot(token="")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Я бот-переводчик с русского на ульчский! Пожалуйста, напишите слово или фразу для "\
                        "перевода.")

@dp.message_handler()
async def echo_message(message: types.Message):
    #mycursor = connect.cursor() #создание cursor объекта 

    #sql = "SELECT * FROM language WHERE rus = ?", (str(message))
    msg = str(message.from_user.id)
    cursor.execute("SELECT * FROM translations WHERE russian = (?)", [str(msg)]) 
    myresult = cursor.fetchall() 
    word = str(myresult)


    await bot.send_message(message.from_user.id, word)
    

if __name__ == '__main__':
    executor.start_polling(dp)


