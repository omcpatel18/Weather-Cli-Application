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
            fetch_geoapi(city)
    except Exception as e:
        return f"An error occured {e}"

def fetch_geoapi(city):
    base_url = "https://geocoding-api.open-meteo.com/v1/search"
    my_params = {
        "name": city,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "auto"
    }
    response = requests.get(base_url, params=my_params)
    data = response.json()
    location = data["results"][0]
    lat = location["latitude"]
    log = location["longitude"]
    weatherapi(lat,log)

def weatherapi(lat,log):
    base_url = "https://api.open-meteo.com/v1/forecast"
    my_params = {
        "latitude" : lat,
        "longitude" : log,
        "hourly" : "temperature_2m,wind_speed_10m,rain,visibility,temperature",
        "daily" : "wind_speed_10m_max,temperature_2m_max,sunrise,sunset",
        "current" : "temperature_2m,relative_humidity_2m,is_day,surface_pressure",
        "timezone" : "auto"
    }
    response = requests.get(base_url, params=my_params)
    data = response.json()
    print(data)
    print(response.url)

if __name__ == "__main__":
    main()


# import requests

# def get_weather_by_city(city_name):
#     # --- STEP 1: GEOCODING (The Bridge) ---
#     # Convert City Name -> Coordinates
#     geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    
#     try:
#         geo_response = requests.get(geo_url)
#         geo_data = geo_response.json()

#         # Check if the city exists in the results
#         if "results" not in geo_data:
#             return f"Sorry, I couldn't find '{city_name}'."

#         # Shortlisting the tech data we need
#         location = geo_data["results"][0]
#         lat = location["latitude"]
#         lon = location["longitude"]
#         full_name = location["name"]
#         country = location.get("country", "")

#         # --- STEP 2: WEATHER API ---
#         # Use Coordinates -> Get Temperature
#         weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
        
#         weather_response = requests.get(weather_url)
#         weather_data = weather_response.json()
        
#         temp = weather_data["current"]["temperature_2m"]
#         unit = weather_data["current_units"]["temperature_2m"]

#         print(weather_data)
        
#         return f"The current temperature in {full_name}, {country} is {temp}{unit}."

#     except Exception as e:
#         return f"An error occurred: {e}"

# # --- USER INTERFACE ---
# user_query = input("Enter city name: ")
# result = get_weather_by_city(user_query)
# print(result)
