# Weather Bot

This is a responsive Telegram bot created using Python and the Aiogram library. It provides real-time weather information fetched from the OpenWeatherAPI. The bot allows users to search for weather conditions in any city, navigate through various commands, and save up to five cities as favorites for quick access.

## Features

- Real-Time Weather Data: The bot retrieves accurate weather information from OpenWeatherAPI.
- Search Functionality: Users can search for the current weather in any city by simply typing the city name.
- Favorites Management: Users can save up to five cities as their favorite locations for quicker access to weather updates.
- Interactive Commands: Easy-to-use command navigation system to check saved cities, manage favorites, and get help.
- Responsive Design: Built using Aiogram to ensure smooth and efficient interaction.
- Requirements

You need:

A Telegram Bot Token, which can be obtained from BotFather on Telegram.
An API Key from OpenWeatherAPI.

## Installation

1. Clone the repository

        git clone https://github.com/elBukhara/Weather-Bot
        cd Weather-Bot
        python -m venv .venv
        .venv/Scripts/activate 

2. Install the required dependencies:

        pip install -r requirements.txt

3. Set up your environment variables: Create a .env file in the root directory and add the following:

        TELEGRAM_TOKEN=token
        WEATHER_TOKEN=token
        DATABASE_URL='sqlite+aiosqlite:///db.sqlite3' # by deault

## Usage 

Run the bot by the following command: 

    python run.py