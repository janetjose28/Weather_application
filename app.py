import streamlit as st
from modules.api_handler import get_weather
from modules.ui_components import city_input, display_weather_data
from PIL import Image
import io
import base64

def set_default_background():
    """Set a default background image when the app starts."""
    try:
        # Load and set the default background image
        set_background_image("assets/bg.jpg")  # Adjust this with your default background path
    except Exception as e:
        st.error(f"Error setting default background: {e}")

def set_background_image(image_path):
    """Function to set background image using base64 encoding."""
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Convert image to base64
        img_base64 = image_to_base64(image)
        
        # Set background image using HTML/CSS
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{img_base64}"); 
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Error loading background image: {e}")

def image_to_base64(image):
    """Convert image to base64 encoding."""
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="JPEG")
    img_byte_arr = img_byte_arr.getvalue()
    return base64.b64encode(img_byte_arr).decode()

def set_background_image_based_on_weather(weather_description):
    """Function to set background image based on weather description."""
    try:
        # Map weather descriptions to image paths (adjust with your own images)
        weather_images = {
            "clear sky": "assets/clear_sky.jpg",
            "few clouds": "assets/few_clouds.jpg",
            "light rain": "assets/light_rain.jpg",
            "smoke": "assets/smoke.jpg",
            "fog": "assets/fog.jpg",
            "mist": "assets/mist.jpg",
            "broken clouds": "assets/few_clouds.jpg",
            "overcast clouds": "assets/few_clouds.jpg",
            "scattered clouds": "assets/few_clouds.jpg",
            "default": "assets/default.jpg"  # A fallback image
        }

        # Get the corresponding image path based on the weather description
        image_path = weather_images.get(weather_description.lower(), weather_images["default"])

        # Check if the image exists
        try:
            # Load and set the background image using base64 encoding
            set_background_image(image_path)
        except Exception as e:
            st.error(f"Error setting weather background image: {e}")
        
    except Exception as e:
        st.error(f"Error loading background image based on weather: {e}")

def main():
    # Set a default background image when the app loads
    set_default_background()
    
    st.title("Real-time Weather App")
    
    # Get city input
    city = city_input()
    if st.button("Submit"):
        if city:
            try:
                # Fetch weather data
                weather_data = get_weather(city)

                # Get the weather description (ensure it's a valid key)
                weather_description = weather_data.get("weather", [{}])[0].get("description", "").lower()

                # Set the background based on the weather description
                set_background_image_based_on_weather(weather_description)

                # Display weather data
                display_weather_data(weather_data)
            except Exception as e:
                st.error(f"Error fetching weather data: {e}")
        else:
            st.error("Please enter a city")

if __name__ == "__main__":
    main()


