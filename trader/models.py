from django.db import models
from django.contrib.auth.models import AbstractUser


class Engine(models.Model):
    engine_types = [
        ("P", "Petrol"),
        ("D", "Diesel"),
        ("E", "Electric"),
        ("H", "Hybrid"),
        ("I", "Plug-in Hybrid")
    ]
        
    type = models.CharField(max_length=1, choices=engine_types)
    power = models.IntegerField()
    volume = models.IntegerField()


class Car(models.Model):
    gearbox_types = [
        ("M", "manual"),
        ("A", "automatic"),
        ("S", "semi-automatic")
    ]

    manufacturer = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    gearbox_type = models.CharField(max_length=1, choices=gearbox_types)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
    eurostandard = models.IntegerField()
    mileage = models.IntegerField()
    production_date = models.DateField()
    color = models.CharField(max_length=20)
    price = models.IntegerField()
    region = models.CharField(max_length=64)
    place = models.CharField(max_length=64)