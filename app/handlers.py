from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from .weather import return_data

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!",
                         reply_markup=kb.settings)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('/start - Start the bot')

@router.message(Command('about'))
async def get_about(message: Message):
    await message.answer('The bot is under deveolpment, here are our social medias',
                         reply_markup=await kb.inline_apps())

@router.message(F.text == 'About')
async def get_about(message: Message):
    await message.answer('The bot is under deveolpment')

@router.message(Command('home'))
async def get_home(message: Message):
    await message.answer('Write your city to get the weather information')

@router.message(F.text == 'Home')
async def get_home(message: Message):
    await message.answer('Write your city to get the weather information')

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

