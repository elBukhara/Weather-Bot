from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Команды'), KeyboardButton(text='Профиль')],
    [KeyboardButton(text='Избранные города')],    
],
                           resize_keyboard=True,
                           input_field_placeholder='Введите город...',
                           )


def create_favourite_cities_keyboard(cities):
    if 5 > len(cities) > 0:
        inline_keyboard = [[InlineKeyboardButton(text=city, callback_data=f'favourite_city:{city}')] for city in cities]
        inline_keyboard.append([InlineKeyboardButton(text='🗑️ Удалить', callback_data='remove_favourite_cities_list'), InlineKeyboardButton(text='🔍 Добавить', callback_data='add_favourite_city')])
    elif len(cities) == 5:
        inline_keyboard = [[InlineKeyboardButton(text=city, callback_data=f'favourite_city:{city}')] for city in cities]
        inline_keyboard.append([InlineKeyboardButton(text='🗑️ Удалить', callback_data='remove_favourite_cities_list')])
    elif len(cities) == 0:
        inline_keyboard = [[InlineKeyboardButton(text=city, callback_data=f'favourite_city:{city}')] for city in cities]
        
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

def remove_favourite_cities_keyboard(cities):
    inline_keyboard = [[InlineKeyboardButton(text=city, callback_data=f'remove_favourite_city:{city}')] for city in cities]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


button_back_to_favourites = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅ Назад', callback_data='back_to_favourite_cities')]
])

button_add_favourite_city = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🔍 Добавить город', callback_data='add_favourite_city')]
])