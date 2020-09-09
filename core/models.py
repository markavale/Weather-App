from django.db import models


class City(models.Model):
    name                = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Weather(models.Model):
    city_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    temperature  = models.FloatField()
    icon = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name

    def get_celsius(self):
        fahrenheit = self.temperature
        celsius = (fahrenheit-32) / 1.8000
        return celsius

    