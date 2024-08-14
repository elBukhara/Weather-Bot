import os
import math
import pyowm
from pyowm.utils.config import get_default_config
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')

def return_data(city):
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = pyowm.OWM(WEATHER_TOKEN, config_dict)
    mgr = owm.weather_manager()
    
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        data = {
            'city': city,
            'status': w.detailed_status,
            'wind': w.wind()['speed'],
            'humidity': w.humidity,
            'temperature': w.temperature('celsius'),
            'rain': w.rain,
            'heat_index': w.heat_index,
            'clouds': w.clouds
        }

        responses = {
            'city': f"Город: {data['city']}",
            'status': f"Текущий статус: {data['status']}.",
            'temperature': f"Температура: {math.ceil(data['temperature']['temp'])} ℃",
            'wind': f"Скорость ветра: {math.ceil(data['wind'])} метр/в секунду",
            'humidity': f"Влажность: {data['humidity']}%",
            'high-temperature': f"Макс. Температура: {math.ceil(data['temperature']['temp_max'])} ℃",
            'min-temperature': f"Мин. Температура: {math.ceil(data['temperature']['temp_min'])} ℃",
            'feels_like': f"Ощущается как: {math.ceil(data['temperature']['feels_like'])} ℃"
        }

        result = ""
        for key, value in responses.items():
            result += f"{value}\n" 
        return result.strip()
    except:
        return f"Что-то пошло не так! Возможно город '{city}' не существует?\nНапишите действительный город."