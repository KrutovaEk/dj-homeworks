import datetime
from datetime import date

from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    # id = models.ForeignKey
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    temperature = models.FloatField()
    date_of_measurement = models.DateField(default=date.today)
    time = models.TimeField(default=datetime.datetime.now)
    # sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)

