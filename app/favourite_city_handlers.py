from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.database.requests import add_favourite_city_to_db, remove_favourite_city_from_db, get_favourite_cities
from .weather import return_data

import app.keyboards as kb

router = Router()

class AddCity(StatesGroup):
    city = State()

@router.message(Command('favourites'))
async def get_favourite_cities_handler(message: Message):
    await send_favourite_cities(message.from_user.id, message)

@router.callback_query(F.data == 'back_to_favourite_cities')
async def back_to_favourite_cities(callback: CallbackQuery):
    await send_favourite_cities(callback.from_user.id, callback)

@router.callback_query(lambda c: c.data.startswith('favourite_city:'))
async def weather_about_favourite_city(callback: CallbackQuery):
    city_name = callback.data.split(':')[1]
    response = return_data(city_name)  # gives weather information about the city

    await callback.message.edit_text(response, reply_markup=kb.button_back_to_favourites)

@router.callback_query(F.data == 'remove_favourite_cities_list')
async def remove_favourite_cities_list(callback: CallbackQuery):
    cities = await get_favourite_cities(callback.from_user.id)

    if not cities:
        await callback.message.edit_text("Нет избранных городов, чтобы удалять...", reply_markup=kb.button_add_favourite_city)
        return

    # Create keyboard dynamically
    keyboard = kb.remove_favourite_cities_keyboard(cities)
    await callback.message.edit_text("Выберите город чтобы удалить:", reply_markup=keyboard)

@router.callback_query(lambda c: c.data.startswith('remove_favourite_city:'))
async def remove_favourite_city(callback: CallbackQuery):
    city_name = callback.data.split(':')[1]
    
    success, response = await remove_favourite_city_from_db(callback.from_user.id, city_name)
    await send_favourite_cities(callback.from_user.id, callback)
    await callback.answer(response)

@router.callback_query(F.data =='add_favourite_city')
async def add_favourite_city_handler(callback: CallbackQuery, state: FSMContext):
    
    await state.set_state(AddCity.city)
    await callback.message.edit_text('Отправьте название города', reply_markup=kb.button_back_to_favourites)

@router.message(AddCity.city)
async def add_favourite_city(message: Message, state: FSMContext):
    city = message.text
    await state.update_data(city=city)
    data = await state.get_data()
    
    success, response = await add_favourite_city_to_db(message.from_user.id, city)
    await send_favourite_cities(message.from_user.id, message)
    # await message.answer(response, show_alert=True)
    
    await state.clear()    


async def send_favourite_cities(user_id, event):
    cities = await get_favourite_cities(user_id)

    if not cities:
        if isinstance(event, Message):
            await event.reply("У вас нет избранных городов.", reply_markup=kb.button_add_favourite_city)
        elif isinstance(event, CallbackQuery):
            await event.message.edit_text("У вас нет избранных городов.", reply_markup=kb.button_add_favourite_city)
        return

    # Create keyboard dynamically
    keyboard = kb.create_favourite_cities_keyboard(cities)
    
    if isinstance(event, Message):
        await event.reply("Ваши избранные города:", reply_markup=keyboard)
    elif isinstance(event, CallbackQuery):
        await event.message.edit_text("Ваши избранные города:", reply_markup=keyboard)
