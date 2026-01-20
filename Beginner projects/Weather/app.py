import requests
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    try:
        city = input("Enter City name:").strip()
        if city == "":
            print("Brother you forgot to write City name.")
        else:
            print(f"I am confirming your city name {city} ?") 
            geoapi(city)
    except NameError:
        print("try again")

def geoapi(city):
    # First, get coordinates from city name using geocoding API
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }
    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()
    
    # Check if city was found
    if "results" not in geo_data or len(geo_data["results"]) == 0:
        print(f"City '{city}' not found.")
        return
    
    # Extract latitude and longitude
    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]
    
    # Now get weather data using coordinates
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code,relative_humidity_2m"
    }
    weather_response = requests.get(weather_url, params=weather_params)
    weather_data = weather_response.json()
    print(f"Weather in {city}:")
    print(weather_data)

if __name__ == "__main__":
    main()
