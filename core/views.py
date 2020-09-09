from django.shortcuts import render
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CitySerializer, WeatherSerializer
from .models import City, Weather
from django.conf import settings

weather_api = settings.WEATHER_API_KEY


def index(request):
    return render(request, 'index.html')
# def index(request):
#     #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
#     # url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=13417a3f4de1d1d1f86ccf8e6fd1277f'
#     cities = City.objects.all()
#     weather_obj = {}
#     weather_data = []
#     # for city in cities:
#     #     res = requests.get(url.format(city, weather_api)).json() 
#     #     city_weather = {
#     #         'city': city.name,
#     #         'temperature': res['main']['temp'],
#     #         'description': res['weather'][0]['description'],
#     #         'icon': res['weather'][0]['icon'],
#     #     }
#     #     #print(city_weather)
#     #     weather_obj.update(city_weather)
#     #     weather_data.append(city_weather)
#     city_weather= "test"
#     print("data--------------------")
#     print(weather_data)
#     print("data object--------------------")
#     print(weather_obj)
#     context = {
#         'city_weather': city_weather,
#         'weather_data':weather_data,
#     }
#     return render(request,'index.html', context)

@api_view(['GET', 'POST'])
def city_create_view(request):
    # 13417a3f4de1d1d1f86ccf8e6fd1277f
    url = 'api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=13417a3f4de1d1d1f86ccf8e6fd1277f'
    if request.method == 'GET':
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def list_creat_city_view(request):
    if request.method == 'GET':
        weathers = Weather.objects.all().order_by('-created_at')
        serializer = WeatherSerializer(weathers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)