import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    print("Error: OPENWEATHER_API_KEY not set in .env")
    exit()

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.json().get('message', 'Unknown error')}")
        return
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Weather in {city}: {temp}°C, {desc}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
    else:
        get_weather(sys.argv[1])
