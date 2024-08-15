from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text='Home')],
    [KeyboardButton(text='About'), KeyboardButton(text='Help')],
],
                           resize_keyboard=True,
                           input_field_placeholder='Choose an option')


favourite_cities = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Бухара', callback_data='settings:Бухара')],
    [InlineKeyboardButton(text='Москва', callback_data='settings:Москва')],
    [InlineKeyboardButton(text='Мадрид', callback_data='settings:Мадрид')],
    [InlineKeyboardButton(text='Париж', callback_data='settings:Париж')],
    [InlineKeyboardButton(text='Видное', callback_data='settings:Видное')],
])

button_back_to_favourites = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<- Назад', callback_data='back_to_favourite_cities')]
])