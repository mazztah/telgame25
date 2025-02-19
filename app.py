from flask import Flask, send_file
from aiogram import Bot, Dispatcher
from aiogram.types import WebAppInfo, Message
from aiogram.utils.executor import start_polling
import asyncio
import os
from dotenv import load_dotenv

# .env laden
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

# Flask-App
app = Flask(__name__)

@app.route("/")
def serve_game():
    return send_file("index.html")

# Aiogram Bot und Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()  # Keine Argumente mehr nötig

@dp.message_handler(commands=["start"])
async def start(message: Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="🎮 Balance Tower", web_app=WebAppInfo(url=WEB_APP_URL))
    keyboard.add(button)
    await message.answer("Starte das Spiel!", reply_markup=keyboard)

async def main():
    dp.include_router(dp)  # Router explizit hinzufügen
    await bot.delete_webhook(drop_pending_updates=True)  # Vermeidet alte Nachrichten
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    app.run(host="0.0.0.0", port=5000)
