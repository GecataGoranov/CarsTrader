from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Car, CarManufacturer, CarModel

@receiver(post_save, sender=Car)
def add_manufacturer(sender, instance, **kwargs):
    car_manufacturer = CarManufacturer.objects.get_or_create(manufacturer=instance.manufacturer)
    CarModel.objects.get_or_create(manufacturer=car_manufacturer[0], model=instance.model)


@receiver(pre_delete, sender=Car)
def remove_manufacturer(sender, instance, **kwargs):
    cars_with_same_manufacturer = Car.objects.filter(manufacturer=instance.manufacturer)

    if len(cars_with_same_manufacturer) <= 1:
        manufacturer_to_delete = CarManufacturer.objects.get(manufacturer=instance.manufacturer)
        manufacturer_to_delete.delete()

