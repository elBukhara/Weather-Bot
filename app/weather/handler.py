import os
from dotenv import load_dotenv

from aiogram import Router
from aiogram.types import Message
from .weather import WeatherBot


load_dotenv()
weather_bot = WeatherBot(api_key=os.getenv('WEATHER_TOKEN'))


router = Router()

@router.message()
async def message_handler(message: Message):
    """
    This is the main handler, which accepts every kind of messages (except Commands, Callbacks)
    It returns with the weather data of given city/town/region/area
    """
    try:
        response = weather_bot.get_weather(message.text)
        await message.answer(response)
    except TypeError:
        await message.answer("Хорошая попытка!")