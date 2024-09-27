from os import getenv
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    TOKEN = input("Введите TOKEN телеграм-бота:\n")
    with open(".env", "w", encoding="utf-8") as file:
        file.write(f"TOKEN = {TOKEN}\n")

load_dotenv()

TOKEN = getenv("TOKEN")