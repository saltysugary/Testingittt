from bot import dp, bot
from aiogram import types
from database.utils import find_translation


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Я бот-переводчик с русского на ульчский! Пожалуйста, напишите слово или фразу для " \
                        "перевода.")


@dp.message_handler()
async def echo_message(message: types.Message):

    
    # TODO Message have a field which contains message text, check it in the docs

    # TODO You also should name variable to show its designation.
    # TODO Word isn't really good name
    # TODO (especially in case you got the whole phrase from user, not just word)

    word = str(message)

    # TODO here you should call find_translation func. from utils
    # TODO remember to write it in utils
    await bot.send_message(message.from_user.id, word)