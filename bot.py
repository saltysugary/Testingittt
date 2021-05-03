from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config.config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    executor.start_polling(dp)


