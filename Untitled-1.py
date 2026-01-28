import streamlit as st
import requests

# App title
st.title("🌦️ Weather Detection App")

# Input city name
city = st.text_input("Enter City Name")

# OpenWeatherMap API
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

if st.button("Get Weather"):
    if city == "":
        st.warning("Please enter a city name")
    else:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            st.error("City not found ❌")
        else:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]
            wind = data["wind"]["speed"]

            st.success(f"Weather in {city}")
            st.write(f"🌡️ Temperature: {temp} °C")
            st.write(f"💧 Humidity: {humidity}%")
            st.write(f"☁️ Condition: {weather.title()}")
            st.write(f"🌬️ Wind Speed: {wind} m/s")
