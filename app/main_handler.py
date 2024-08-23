import os
from dotenv import find_dotenv, load_dotenv

from aiogram import Router
from aiogram.types import Message
from .weather import WeatherBot

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')
weather_bot = WeatherBot(api_key=WEATHER_TOKEN)


router = Router()

@router.message()
async def message_handler(message: Message):
    # Returns data about city from weather.py
    try:
        response = weather_bot.get_weather(message.text)
        await message.answer(response)
    except TypeError:
        await message.answer("Хорошая попытка!")