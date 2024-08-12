from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from .weather import return_data

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('/start - Start the bot')

@router.message(Command('about'))
async def get_about(message: Message):
    await message.answer('The bot is under deveolpment')

@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('Нормально')

@router.message()
async def message_handler(message: Message):
    # Returns data about city from weather.py
    try:
        response = return_data(message.text)
        await message.answer(response)
    except TypeError:
        await message.answer("Nice try!")

