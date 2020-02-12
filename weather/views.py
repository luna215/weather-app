from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=19b3b8c0da1d8b61cf8280b923446727'
    city = 'San Diego'
    city_weather = requests.get(url.format(city)).json() # request the API data and convert the JSON to Python data types

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {
        'weather': weather
    }
    return render(request, 'weather/index.html', context) # returns the index.html template