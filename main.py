import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "99a396ac76ab4cf444f6b473e5ee270b"
CITY = "Harrison"

def kelvin_to_celsius_fh(kelvin):
    celsius = kelvin - 273.15
    fh = celsius * (9/5) + 32
    return celsius, fh

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_cel, temp_fh = kelvin_to_celsius_fh(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_cel, feels_like_fh = kelvin_to_celsius_fh(feels_like_kelvin)
wind_speed = response['wind']['speed']
humididty = response['main']['humidity']
desciption = response['weather'][0]['description'] 
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_cel:.2f}C or {temp_fh:.2f}F")
print(f"Temperature in {CITY} feels like {feels_like_cel:.2f}C or {feels_like_fh:.2f}F")
print(f"Humidity in {CITY} is {humididty}%")
print(f"Wind speed in {CITY} is {wind_speed}m/hr")
print(f"General weather in {CITY}: {desciption}")
print(f"Sun rises in {CITY} at {sunrise_time} local time")
print(f"Sun sets in {CITY} at {sunset_time} local time")