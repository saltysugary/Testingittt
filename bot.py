
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token="")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Я бот-переводчик с русского на ульчский! Пожалуйста, напишите слово или фразу для "\
                        "перевода.")


if __name__ == '__main__':
    executor.start_polling(dp)


