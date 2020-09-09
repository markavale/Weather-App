from django.urls import path
from .views import city_create_view, index,list_creat_city_view

urlpatterns = [
    path('', index, name="city-list"),
    path('api/city/', city_create_view, name="city-post"),
    path('api/city/weather/', list_creat_city_view, name="city-weather"),

]
