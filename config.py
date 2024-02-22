import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

telegram_token = os.getenv('telegram_token')
weather_token = os.getenv('weather_token')