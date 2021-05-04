from loader import bot, dp
from aiogram.types import Message
from database.utils import find_translation


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.reply("Я бот-переводчик с русского на ульчский! Пожалуйста, напишите слово или фразу для " \
                        "перевода.")


@dp.message_handler()
async def echo_message(message: Message):
    text = message.text
    answer = find_translation(text)
    await bot.send_message(message.from_user.id, answer)
    pass