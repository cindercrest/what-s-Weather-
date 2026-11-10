import json
from typing import Any
from requests.models import Response
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

#Load the Environment Variables
load_dotenv()


#Current Weather of city
def get_current_weather(city="New Delhi"):
    #Getting Co-ordinates from city
    coordinate_url: str = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={1}&appid={os.getenv('API_KEY')}"
    coordinateresponse: Response= requests.get(coordinate_url)
    if coordinateresponse.status_code != 200:
        return coordinateresponse.status_code
    coordinate_data = coordinateresponse.json()
    coordinates: dict[Any, Any] = {}
    if coordinate_data:
        for place in coordinate_data:
            latitude = place.get("lat")
            longitude =place.get("lon")
            country = place.get("country")
            coordinates["latitude"] = latitude
            coordinates["longitude"] = longitude
        response: dict[Any, Any] = coordinates
        url: str = f"https://api.openweathermap.org/data/2.5/weather?lat={response['latitude']}&lon={response['longitude']}&appid={os.getenv('API_KEY')}&units=metric"
        o : Response = requests.get(url)
        weather_data = o.json()
        return weather_data
     # FIX 2: Handle cases where OpenWeather returns an empty list (city not found)
    if not coordinate_data:
        return {
            "cod": "404",
            "message": f"city not found: '{city}'"
        }

        

def main():
    city: str = input("Please Enter the city : ").strip()
    if not bool(city):
        city = 'New Delhi'
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)

if __name__ == "__main__":
    main()
