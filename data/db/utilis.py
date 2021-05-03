import sqlite3

conn = sqlite3.connect("language.db") #подключение базы данных?
cursor = conn.cursor() #создание cursor объекта

def initialize():
    with open(r"data/db/build.sql", "r", encoding="utf-8") as file:
        cursor.executescript(file.read())

    conn.commit()

#file = open("C:\\Users\\Анна\\Documents\\pyeverybody\\bot\\data\\db\\build.sql")
#script = file.read()
#file.close()
#cursor.executescript("CREATE TABLE IF NOT EXISTS translations"\
 #   "(id integer PRIMARY KEY AUTOINCREMENT,russian text,translation text)")
