import asyncio
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from aiogram import Dispatcher, Bot
from telegramm.handlers import router
from vhod import Ui_reg2
from telegramm.token_settings import TOKEN


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.ui = Ui_reg2()
        self.ui.setupUi(self)


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("off")
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
