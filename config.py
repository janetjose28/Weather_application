import os
from dotenv import load_dotenv

load_dotenv() #loading the env variables defined in .env file

API_KEY = os.getenv('OPENWEATHERMAP_API_KEY') #to get the apikey stored in .env file


BASE_URL = "http://api.openweathermap.org/data/2.5/weather" #base url to which we'll append the specific city names
