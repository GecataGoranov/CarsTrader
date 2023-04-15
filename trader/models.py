from django.db import models
from django.contrib.auth.models import AbstractUser


class Car(models.Model):
    gearbox_types = [
        ("M", "manual"),
        ("A", "automatic"),
        ("S", "semi-automatic")
    ]

    engine_types = [
        ("P", "Petrol"),
        ("D", "Diesel"),
        ("E", "Electric"),
        ("H", "Hybrid"),
        ("I", "Plug-in Hybrid")
    ]

    categories = [
        ("VAN", "Van"),
        ("SUV", "SUV"),
        ("CAB", "Cabrio"),
        ("UNI", "Universal"),
        ("COU", "Coupe"),
        ("MIN", "Minivan"),
        ("PIC", "Pickup"),
        ("SED","Sedan"),
        ("LIM", "Limousine"),
        ("HAT", "Hatchback")
    ]
        
    colors = [
        ("W", "White"),
        ("B", "Black"),
        ("G", "Gray"),
        ("S", "Silver"),
        ("U", "Blue"),
        ("R", "Red"),
        ("N", "Brown"),
        ("G", "Green"),
        ("O", "Orange"),
        ("L", "Gold"),
        ("Y", "Yellow"),
        ("P", "Purple"),
    ]

    manufacturer = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    category = models.CharField(max_length=3, choices=categories)
    gearbox_type = models.CharField(max_length=1, choices=gearbox_types)
    engine_type = models.CharField(max_length=1, choices=engine_types)
    engine_power = models.IntegerField()
    engine_volume = models.IntegerField()
    eurostandard = models.IntegerField()
    mileage = models.IntegerField()
    production_date = models.DateField()
    color = models.CharField(max_length=1, choices=colors)
    price = models.IntegerField()
    region = models.CharField(max_length=64)
    place = models.CharField(max_length=64)