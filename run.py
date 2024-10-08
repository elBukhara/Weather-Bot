import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.database.models import async_main

async def main():
    await async_main()
    load_dotenv()
    bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO) # Turn Off in Production
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')