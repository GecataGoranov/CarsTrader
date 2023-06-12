from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.core.files.storage import FileSystemStorage
from accounts.models import TraderUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class Car(models.Model):
    gearbox_types = [
        ("M", "Manual"),
        ("A", "Automatic"),
        ("S", "Semi-automatic")
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
        ("UNI", "Station Wagon"),
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

    condition_choices = [("N", "New"),
                         ("U", "Used"),
                         ("F", "For parts")]
    
    
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
    condition = models.CharField(max_length=1, choices=condition_choices, null=True, blank=True, default="U")
    price = models.IntegerField()
    region = models.CharField(max_length=64)
    place = models.CharField(max_length=64)
    seller = models.ForeignKey(TraderUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.manufacturer} {self.model} for {self.price}lv"
    

class CarPictures(models.Model):
    picture = models.ImageField(upload_to="car_images")
    car_id = models.ForeignKey(Car, on_delete=models.DO_NOTHING)


class CarManufacturer(models.Model):
    manufacturer = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.manufacturer

class CarModel(models.Model):
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.model


from trader.signals import add_manufacturer
post_save.connect(add_manufacturer, sender=Car)