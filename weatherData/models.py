from django.db import models
from django.utils import timezone


# Create your models here.
class weather(models.Model):
    time = models.DateTimeField(default= timezone.now())
    name = models.CharField(max_length=100)
    Latitude = models.IntegerField()
    Longitude = models.IntegerField()
    temp = models.FloatField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()