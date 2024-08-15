from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from .favourite_city_handlers import router as favourite_router
from .main_handler import router as main_router

import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    await rq.register_user(message.from_user.id) # Add user to database
    reply = (
        "Добро пожаловать в Weather bot! Чтобы узнать погоду в вашем городе, просто введите название города.\n\n"
        "Команды:\n"
        "/start - запустить бота\n"
        "/about - получить информацию о боте\n"
        "/help - получить помощь\n"
        "/profile - просмотреть свой профиль\n"
        "/favourites - просмотреть избранные города"        
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
        "/profile - просмотреть свой профиль\n"
        "/favourites - просмотреть избранные города"        
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

router.include_router(favourite_router)
router.include_router(main_router)