from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text='Home')],
    [KeyboardButton(text='About'), KeyboardButton(text='Help')],
],
                           resize_keyboard=True,
                           input_field_placeholder='Choose an option')


settings = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='Settings', callback_data='settings')],    
])

apps = ['TikTok', 'Instagram', 'Youtube']

async def inline_apps():
    keyboard = InlineKeyboardBuilder()
    for app in apps:
        keyboard.add(InlineKeyboardButton(text=app, url='https://google.com'))
    return keyboard.adjust(2).as_markup()