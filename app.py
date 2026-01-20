import requests
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    try:
        temp_city = input("Enter City name:")
        Perm_city = temp_city.strip()
        if Perm_city == "":
            print("Brother you forgot to write City name.")
        else:
            print(f"I am confirming your city name {Perm_city} ?") 
            fetch_weatherapi(Perm_city)
    except NameError:
        print("try again")

def fetch_weatherapi(Perm_city):
    base_url = "https://api.openweathermap.org"
    end_point = "/data/2.5/weather"
    api_key = os.getenv("api_key")
    if not api_key:
        print("API key not available in environment variables.")
        return
    url = f"{base_url}{end_point}?q={Perm_city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    print(url)
    print(data)
    display_weather(data)

def display_weather(data):
    """Display weather information in a formatted way"""
    if "main" in data:
        print("\n=== Weather Information ===")
        print(f"Temperature: {data['main']['temp']}K")
        print(f"Feels Like: {data['main']['feels_like']}K")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("Could not retrieve weather information.")

if __name__ == "__main__":
    main()
