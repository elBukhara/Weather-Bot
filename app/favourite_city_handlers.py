from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from .weather import return_data

import app.keyboards as kb

router = Router()


@router.message(Command('favourites'))
async def get_favourite_cities(message: Message):
    reply = "Ваши избранные города:"
    await message.answer(reply, reply_markup=kb.favourite_cities)

@router.callback_query(F.data == 'back_to_favourite_cities')
async def back_to_favourite_cities(callback: CallbackQuery):
    reply = "Ваши избранные города:"
    await callback.message.edit_text(reply, reply_markup=kb.favourite_cities)

@router.callback_query(lambda c: c.data.startswith('favourite_city:'))
async def process_callback_city(callback: CallbackQuery):
    city_name = callback.data.split(':')[1]
    response = return_data(city_name)
    
    await callback.message.edit_text(response, reply_markup=kb.button_back_to_favourites)
