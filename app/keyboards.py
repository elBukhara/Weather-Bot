from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Команды'), KeyboardButton(text='Профиль')],
    [KeyboardButton(text='Избранные города')],    
],
                           resize_keyboard=True,
                           input_field_placeholder='Введите город...',
                           )
