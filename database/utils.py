import sqlite3
from config.config import BUILD_PATH, DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


def initialize():
    with open(BUILD_PATH, "r", encoding="utf-8") as file:
        cursor.executescript(file.read())

    conn.commit()


def find_translation(text: str) -> str:
    text = (text.lower()).strip()
    cursor.execute("SELECT translation FROM translations WHERE russian = (?)", (text,))
    result = cursor.fetchone() 
    
    if result:
        return result[0]

    else: 
        return "Перевод не найден"

