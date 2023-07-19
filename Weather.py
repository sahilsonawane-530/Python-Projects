import datetime
import requests

baseURL = "https://api.openweathermap.org/data/2.5/weather?"
apiKey = open("C:/API/Weather.txt", "r").read()
city = input("Enter city : ")

def kelvinToCelsiusFahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * (9/5) + 32
    return celsius, fahrenheit

url = baseURL + "appid=" + apiKey + "&q=" + city

response = requests.get(url).json()

tempKelvin = response["main"]["temp"]
tempCelsius, tempFahrenheit = kelvinToCelsiusFahrenheit(tempKelvin)
FeelsLikeKelvin = response["main"]["feels_like"]
FeelsLikeCelsius, FeelsLikeFahrenheit = kelvinToCelsiusFahrenheit(FeelsLikeKelvin)
windSpeed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunriseTime = datetime.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"])
sunsetTime = datetime.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"])

print(f"Temperature in {city} : {tempCelsius:.2f}°C")
print(f"Feels Like Temperature in {city} : {FeelsLikeCelsius:.2f}°C")
print(f"Humidity in {city} : {humidity}%")
print(f"Wind Speed in {city} : {windSpeed}m/s")
print(f"Sun rises in {city} at {sunriseTime.strftime('%I:%M:%S %p')}")
print(f"Sun sets in {city} at {sunsetTime.strftime('%I:%M:%S %p')}")
print(f"General Weather in {city} : {description}")