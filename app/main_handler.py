from aiogram import Router
from aiogram.types import Message
from .weather import return_data

router = Router()

@router.message()
async def message_handler(message: Message):
    # Returns data about city from weather.py
    try:
        response = return_data(message.text)
        await message.answer(response)
    except TypeError:
        await message.answer("Хорошая попытка!")