from django.db import models

class EngineType(models.Choices):
    PETROL = "P", "Petrol"
    DIESEL = "D", "Diesel"
    ELECTRIC = "E", "Electric"
    HYBRID = "H", "Hybrid"
    PLUG_IN_HYBRID = "PH", "Plug-in Hybrid"# Create your models here.


class Category(models.Model):
    pass


class Manufacturer(models.Model):
    pass


class Car(models.Model):
    engine_types = [
        ("P", "Petrol"),
        ("D", "Diesel"),
        ("E", "Electric"),
        ("H", "Hybrid"),
        ("I", "Plug-in Hybrid")
    ]

    gearbox_types = [
        ("M", "manual"),
        ("A", "automatic"),
        ("S", "semi-automatic")
    ]

    manufacturer = models.ForeignKey(Manufacturer, related_name="manufacturer", on_delete=models.CASCADE)
    model = models.CharField(max_length=30)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    engine_type = models.CharField(max_length=1, choices=engine_types)
    gearbox_type = models.CharField(max_length=1, choices=gearbox_types)
    power = models.IntegerField(name="power", max_length=2000)
    eurostandard = models.IntegerField(name="eurostandard", max_length=6)



