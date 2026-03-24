from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")


import requests as r
#Base URLs
# CWEATHER_BASE = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"


def get_coords():
    while True:
        city_name = input("\nWhich city do you want to search for? (make sure to spell correctly)")
        limit = "50"    #make sure this is in quotes
        GEOCODE_BASE = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_KEY}"  #adds city name and limit, takes API key from "env"
        response = r.get(GEOCODE_BASE) #gives a status code
        coords_json = response.json()   #returns an empty list if nothing is found
        
        if len(coords_json) == 0:   #location check
            print("City not found, check your spelling and try again.")
            continue
        
        lat = coords_json[0]['lat'] #finds latitude
        lon = coords_json[0]['lon'] #finds longitude
        return lat, lon

#NEXT: Put coords into weather url to truly start