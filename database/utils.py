import sqlite3
from config.config import BUILD_PATH, DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


def initialize():
    with open(BUILD_PATH, "r", encoding="utf-8") as file:
        cursor.executescript(file.read())

    conn.commit()


def find_translation(text: str) -> str:
    try: 
        text = message.text 
        cursor.execute("SELECT * FROM translations WHERE russian = (?)", [text,])
        result = cursor.fetchall() 

        await bot.send_message(msg.from_user.id, result.text)
        
    else: 
        await bot.send_message(msg.from_user.id, "Перевод не найден")
    
    # TODO Make check if text is not empty
    # TODO don't forget to make text lower and strip it
    # TODO Write correct request to database to find translation
    # TODO fetch just first entry of response
    # TODO return translated text or "Nothing found" string
    pass
