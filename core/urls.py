from django.urls import path
from .views import city_create_view, index

urlpatterns = [
    path('', index, name="city-list"),
    path('api/city/', city_create_view, name="city-post")
]
