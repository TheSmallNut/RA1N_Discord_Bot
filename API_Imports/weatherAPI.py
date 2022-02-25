import requests
import json
import secret

BASE_URL = f"http://api.weatherapi.com/v1/forecast.json?key={secret.WEATHERAPIKEY}"
#r = requests.get(BASEURL).json()

# Location can be (Lat, Long), City Name, US Zip Code, UK Postal Code, Canada Postal Code, IP ADDRESS


def getWeather(location):
    URL = BASE_URL + f"&q={location}&days=3&aqi=no&alerts=no"
    r = requests.get(URL).json()
    return r


def willItRain(JSON_Data):
    chancesOfRain = []
    for day in JSON_Data["forecast"]["forecastday"]:
        chanceOfRain = day["day"]["daily_chance_of_rain"]
        chancesOfRain.append(chanceOfRain)
    return max(chancesOfRain)
