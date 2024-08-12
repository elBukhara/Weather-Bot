import os
import pyowm
import math
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')

def return_data(city):
    owm = pyowm.OWM(WEATHER_TOKEN)
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
            'city': f"City: {data['city']}",
            'status': f"Current Status: {data['status']}.",
            'temperature': f"Temperature: {math.ceil(data['temperature']['temp'])} ℃",
            'wind': f"Wind speed: {math.ceil(data['wind'])} meter/per second",
            'humidity': f"Hummidity: {data['humidity']}",
            'high-temperature': f"Highest temperature: {math.ceil(data['temperature']['temp_max'])} ℃",
            'min-temperature': f"Minimum temperature: {math.ceil(data['temperature']['temp_min'])} ℃",
            'feels_like': f"Feels Like: {math.ceil(data['temperature']['feels_like'])} ℃"
        }

        result = ""
        for key, value in responses.items():
            result += f"{value}\n"
        return result.strip()
    except:
        return f"Something went wrong! Perhaps the city '{city}' does not exist?\nEnter a valid city."