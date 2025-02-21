import streamlit as st

def display_weather_data(weather_data):
    if weather_data:
        st.write(f"**City:** {weather_data['name']}")
        st.write(f"🌡️**Temperature:** {weather_data['main']['temp']}°C")
        st.write(f"💧**Humidity:** {weather_data['main']['humidity']}%")
        st.write(f"☁️**Weather:** {weather_data['weather'][0]['description']}")
        st.write(f"🍃**Wind Speed:** {weather_data['wind']['speed']} m/s")
    else:
        st.error("Failed to fetch weather data. Please try again.")
        
def city_input():
    return st.text_input("Enter a city name", "")
