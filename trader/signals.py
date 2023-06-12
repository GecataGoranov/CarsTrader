from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Car, CarManufacturer, CarModel

@receiver(post_save, sender=Car)
def add_manufacturer(sender, instance, **kwargs):
    car_manufacturer = CarManufacturer.objects.get_or_create(manufacturer=instance.manufacturer)
    CarModel.objects.get_or_create(manufacturer=car_manufacturer[0], model=instance.model)