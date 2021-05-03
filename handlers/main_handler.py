from bot import dp, bot
from aiogram import types
from database.utils import find_translation


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Я бот-переводчик с русского на ульчский! Пожалуйста, напишите слово или фразу для " \
                        "перевода.")


@dp.message_handler()
async def echo_message(message: types.Message):
    text = message.text 
    find_translation(text) 
   
    #await bot.send_message(message.from_user.id, text)