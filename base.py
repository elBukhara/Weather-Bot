import telebot 
import pyowm
from config import telegram_token, weather_token
from weather import return_data

bot = telebot.TeleBot(telegram_token, parse_mode=None)
owm = pyowm.OWM(weather_token)
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    observation = mgr.weather_at_place('London,GB')
    w = observation.weather

    response = return_data(message.text)

    bot.send_message(message.chat.id, response)
	
bot.infinity_polling()