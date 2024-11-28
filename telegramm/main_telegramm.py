import asyncio

from PyQt6.QtWidgets import QApplication, QMainWindow
from aiogram import Dispatcher, Bot
from telegramm.handlers import router
from token_settings import TOKEN

async def start_bot():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


try:
    asyncio.run(start_bot())
except KeyboardInterrupt:
    print("off")