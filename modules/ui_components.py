import streamlit as st

def display_weather_data(weather_data):
    if weather_data:
        st.write(f"### Weather in {weather_data['city']}")
        st.write(f"🌡️**Temperature**: {weather_data['temperature']}°C")
        st.write(f"🌧️**Humidity**: {weather_data['humidity']}%")
        st.write(f"☁️**Condition**: {weather_data['condition']}")
        st.write(f"🍃**Wind Speed**: {weather_data['wind_speed']} m/s")
    else:
        st.write("Sorry, unable to retrieve the weather data.")

def city_input():
    city = st.text_input("Enter city name:", "")
    return city
