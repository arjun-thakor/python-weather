"""
    This program will demonstrate working with openwethearapi
"""

# importing requests module, in order to fetch data from JSON
import requests

# API address + user key to access JSON data
api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=1a8d31cac550511d792284d7d0f7dd5d&q='

# Prompting user to enter city name
city = input('Please enter your city name: ').upper()

# Concatenating URL address and city name to find data and pass to requests.get() method
url = api_address + city

# Converting data to JSON format
json_data = requests.get(url).json()

# Storing single value in local variables, so that we can use later on
city_name = json_data['name']
country_name = json_data['sys']['country']
condition = json_data['weather'][0]['main']
temp = json_data['main']['temp']
pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
min_temp = json_data['main']['temp_min']
max_temp = json_data['main']['temp_max']
visibility = json_data['visibility']
wind_speed = json_data['wind']['speed']
wind_deg = json_data['wind']['deg']

# Printing fetched data
print('Location: {}, {}'.format(city_name, country_name))
print('Condition : {}'.format(condition))
print('Temperature : {}'.format(temp))
print('Pressure : {}'.format(pressure))
print('Humidity : {}'.format(humidity))
print('Min. temperature : {}'.format(min_temp))
print('Max. temperature : {}'.format(max_temp))
print('Visibility : {}'.format(visibility))
print('Wind speed : {} per km'.format(wind_speed))
print('Wind deg : {}'.format(wind_deg))
