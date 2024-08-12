import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TELEGRAM_TOKEN
from app.handlers import router


async def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO) # Turn Off in Production
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')