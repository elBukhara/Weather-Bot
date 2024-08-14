from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from .weather import return_data

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message):
    reply = (
        "Welcome to the Weather bot! To know the weather in your city, simply type in the city name.\n\n"
        "Commands:\n"
        "/start - start the bot\n"
        "/about - get information about bot\n"
        "/help - get help\n"
        "/profile - view your profile"
    )
    await message.answer(reply)

@router.message(Command('about'))
async def get_about(message: Message):
    reply = (
        "Introducing \"Weather 24/7\" - your ultimate Telegram bot for all your weather needs!\n"
        "Stay informed about the latest weather conditions, forecasts, and more, right at your fingertips.\n"
        "Get real-time updates on temperature, humidity, wind speed, and precipitation levels in your area.\n"
        "Stay ahead of the elements with Weather 24/7!\n\n"
        "Write the city name to get the weather information."
    )
    await message.answer(reply)

@router.message(Command('help'))
async def get_help(message: Message):
    reply = (
        "Commands:\n\n"
        "/start - start the bot\n"
        "/about - get information about bot\n"
        "/help - get help\n"
        "/profile - view your profile"
    )
    await message.answer(reply)

@router.message(Command('profile'))
async def get_profile(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    reply = (
        "Your Profile\n\n"
        f"id: {user_id}\n"
        f"username: {user_name}\n"
    )
    
    await message.answer(reply)

@router.message(F.photo)
async def photo_handler(message: Message):
    await message.answer_photo(photo=f'{message.photo[-1].file_id}', caption='Nice photo!')

@router.message()
async def message_handler(message: Message):
    # Returns data about city from weather.py
    try:
        response = return_data(message.text)
        await message.answer(response)
    except TypeError:
        await message.answer("Nice try!")
