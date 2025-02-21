import requests
from config import API_KEY, BASE_URL

def get_weather(city_name):
    # Define parameters for the API request
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # the unit system here is set to metric
    }

    try:
        # Send a GET request to the OpenWeatherMap API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()

        # on successful result returns the data
        if data.get('cod') == 200:
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'condition': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed']
            }
            return weather
        else:
            print("Error:", data.get('message'))
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
