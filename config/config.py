from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
DB_PATH = r"data/db/database.db"
BUILD_PATH = r"data/db/build.sql"
