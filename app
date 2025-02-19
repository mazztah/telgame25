from flask import Flask, send_file
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
import asyncio
import os
from dotenv import load_dotenv

# Lade Umgebungsvariablen aus der .env Datei
load_dotenv()

# Bot-Token aus der Umgebungsvariable
TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

app = Flask(__name__)

@app.route("/")
def serve_game():
    return send_file("index.html")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="🎮 Balance Tower", web_app=WebAppInfo(url=WEB_APP_URL))
    keyboard.add(button)
    await message.answer("Starte das Spiel!", reply_markup=keyboard)

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    app.run(host="0.0.0.0", port=5000)
