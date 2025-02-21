import requests
from config import API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None