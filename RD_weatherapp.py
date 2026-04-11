from dotenv import load_dotenv
import os
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")

import requests as r


def get_coords():
    '''
    Prompts ths user for a city name and fetches the coordinates using the OpenWeatherMap and Geocoding API
    Returns:
        tuple: (lat, lon, city_name)
    '''
    while True:
        city_name = input("\nWhich city do you want to search for? (make sure to spell correctly)")
        limit = "50"
        GEOCODE_BASE = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_KEY}"
        coords_resp = r.get(GEOCODE_BASE)  # Returns 200 even if city is not found
        coords_json = coords_resp.json()
        
        if len(coords_json) == 0:
            print("City not found, check your spelling and try again.")
            continue
        
        lat = coords_json[0]['lat']
        lon = coords_json[0]['lon'] 
        return lat, lon, city_name


def get_weather(lat, lon, name):
    '''
    Uses coords from get_coords to get weather details 

    Args:
        lat (string): latitude
        lon (string): longitude
        name (string): name of city
    '''
    CWEATHER_BASE = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial" #Adding the longitude and latitude to the URL request
    weath_resp = r.get(CWEATHER_BASE) 
    weath_data = weath_resp.json()
    weath_descr = weath_data['weather'][0]['description']  # Finding the weather description
    weath_maintemp = weath_data['main']['temp']  # Finding the main temperature
    print(f"The weather in {name} is {weath_descr} and the temperature is {weath_maintemp} Fahreinheit.")  # Prints city and weather conditions together
    
def temp_details(lat, lon, name):
    TEMP_BASE = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
    tempweath_resp = r.get(TEMP_BASE)
    temp_data = tempweath_resp.json()


lat, lon, city_name = get_coords() 
get_weather(lat, lon, city_name)