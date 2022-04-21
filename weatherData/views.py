from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import json
from .models import *

# Create your views here.
def getWeather(request):
    url='https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=bf65d8b174418831a16055a19f50144f'
    data = requests.get(url)
    dumpedData = json.dumps(data.json())
    jsonData = json.loads(dumpedData)
    latitude = jsonData['coord']['lat']
    longitude = jsonData['coord']['lon']
    pressure = jsonData['main']['pressure']
    temp_min = jsonData['main']['temp_min']
    temp_max = jsonData['main']['temp_max']
    humidity = jsonData['main']['humidity']
    temp = jsonData['main']['temp']
    name = jsonData['name']
    print(pressure)
    createdWeather = weather.objects.create(Latitude = latitude,Longitude=longitude,pressure=pressure,
                           temp=temp,temp_min=temp_min,temp_max=temp_max,name=name,humidity=humidity)
    return JsonResponse(createdWeather)
#

def index(request):
    weathers = weather.objects.all()
    return render(request , 'weatherData/index.html',{'weathers':weathers})