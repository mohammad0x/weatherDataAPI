from django.urls import path
from .views import *

urlpatterns = [
    path('get-weather/', getWeather , name = "getWeather"),
    path('index/', index , name = "index"),

]