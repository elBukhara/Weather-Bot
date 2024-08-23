import math
import pyowm
import logging

from pyowm.utils.config import get_default_config

class WeatherBot:
    def __init__(self, api_key, language='ru'):
        config_dict = get_default_config()
        config_dict['language'] = language
        self.owm = pyowm.OWM(api_key, config_dict)
        self.mgr = self.owm.weather_manager()
    
    def format_response(self, city, weather):
        data = {
            'city': city,
            'status': weather.detailed_status,
            'wind': weather.wind()['speed'],
            'humidity': weather.humidity,
            'temperature': weather.temperature('celsius'),
            'rain': weather.rain,
            'heat_index': weather.heat_index,
            'clouds': weather.clouds
        }
        
        response = (
            f"Город: {data['city']}\n"
            f"Текущий статус: {data['status']}\n"
            f"Температура: {math.ceil(data['temperature']['temp'])} ℃\n"
            f"Скорость ветра: {math.ceil(data['wind'])} метр/в секунду\n"
            f"Влажность: {data['humidity']}%\n"
            f"Макс. Температура: {math.ceil(data['temperature']['temp_max'])} ℃\n"
            f"Мин. Температура: {math.ceil(data['temperature']['temp_min'])} ℃\n"
            f"Ощущается как: {math.ceil(data['temperature']['feels_like'])} ℃\n"
        )

        return response
    
    def get_weather(self, city):
        try:
            observation = self.mgr.weather_at_place(city)
            w = observation.weather
            return self.format_response(city, w)
        
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return f"Что-то пошло не так! Возможно город '{city}' не существует?\nПожалуйста, проверьте правильность написания."