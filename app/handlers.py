from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from .weather import return_data

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message):
    reply = (
        "Добро пожаловать в Weather bot! Чтобы узнать погоду в вашем городе, просто введите название города.\n\n"
        "Команды:\n"
        "/start - запустить бота\n"
        "/about - получить информацию о боте\n"
        "/help - получить помощь\n"
        "/profile - просмотреть свой профиль"
    )
    await message.answer(reply)

@router.message(Command('about'))
async def get_about(message: Message):
    reply = (
        "Представляем \"Weather 24/7\" — ваш лучший Telegram-бот для всех ваших погодных нужд!\n"
        "Будьте в курсе последних погодных условий, прогнозов и многого другого прямо у вас под рукой.\n"
        "Получайте обновления в режиме реального времени о температуре, влажности, скорости ветра и уровне осадков в вашем регионе.\n"
        "Опережайте стихии с Weather 24/7!\n\n"
        "Напишите название города, чтобы получить информацию о погоде."
    )
    await message.answer(reply)

@router.message(Command('help'))
async def get_help(message: Message):
    reply = (
        "Команды:\n\n"
        "/start - запустить бота\n"
        "/about - получить информацию о боте\n"
        "/help - получить помощь\n"
        "/profile - просмотреть свой профиль"
    )
    await message.answer(reply)

@router.message(Command('profile'))
async def get_profile(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    reply = (
        "Ваш профиль\n\n"
        f"id: {user_id}\n"
        f"username: {user_name}\n"
    )
    
    await message.answer(reply)

@router.message(F.photo)
async def photo_handler(message: Message):
    await message.answer_photo(photo=f'{message.photo[-1].file_id}', caption='Хорошее фото!')


@router.message(Command('favourites'))
async def get_favourite_cities(message: Message):
    reply = "Ваши избранные города:"
    await message.answer(reply, reply_markup=kb.favourite_cities)

@router.callback_query(F.data == 'back_to_favourite_cities')
async def back_to_favourite_cities(callback: CallbackQuery):
    reply = "Ваши избранные города:"
    await callback.message.edit_text(reply, reply_markup=kb.favourite_cities)

@router.callback_query(lambda c: c.data.startswith('settings:'))
async def process_callback_city(callback: CallbackQuery):
    city_name = callback.data.split(':')[1]
    response = return_data(city_name)
    
    await callback.message.edit_text(response, reply_markup=kb.button_back_to_favourites)


@router.message()
async def message_handler(message: Message):
    # Returns data about city from weather.py
    try:
        response = return_data(message.text)
        await message.answer(response)
    except TypeError:
        await message.answer("Хорошая попытка!")
