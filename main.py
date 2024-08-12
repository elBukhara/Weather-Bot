import asyncio
import pyowm

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from weather import return_data

from config import TELEGRAM_TOKEN, WEATHER_TOKEN


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

owm = pyowm.OWM(WEATHER_TOKEN)
mgr = owm.weather_manager()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")


@dp.message()
async def message_handler(message: Message):
    try:
        response = return_data(message.text)
        await message.answer(response)
    except TypeError:
        await message.answer("Nice try!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye!')