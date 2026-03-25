#Hello! This is where all the building gets done, and when it's finished I'll polish it up and remove the comments.
from dotenv import load_dotenv
import os
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")


import requests as r
#Base URLs


def get_coords():
    while True:
        city_name = input("\nWhich city do you want to search for? (make sure to spell correctly)")
        limit = "50"    #make sure this is in quotes
        GEOCODE_BASE = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_KEY}"  #adds city name and limit, takes API key from "env"
        coords_resp = r.get(GEOCODE_BASE) #gives a status code
        coords_json = coords_resp.json()   #returns an empty list if nothing is found
        
        if len(coords_json) == 0:   #location check
            print("City not found, check your spelling and try again.")
            continue
        
        lat = coords_json[0]['lat'] #finds latitude
        lon = coords_json[0]['lon'] #finds longitude
        return lat, lon, city_name

#NEXT: Put coords into weather url to truly start

def get_weather(lat, lon, name):
    CWEATHER_BASE = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
    weath_resp = r.get(CWEATHER_BASE)   #getting the data from the URL

    data = weath_resp.json() #reading the file stream directly

    weath_descr = data['weather'][0]['description'] #finding the weather description
    weath_maintemp = data['main']['temp']   #finding the main temperature
    print(f"The weather in {name} is {weath_descr} and the temperature is {weath_maintemp} Fahreinheit")   #putting vars into a string
    # user_choice = input("What action would you like to do?\n 1 - ")


lat, lon, city_name = get_coords() #introducing arguments
get_weather(lat, lon, city_name) #running with those arguments