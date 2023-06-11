from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Car, CarManufacturer, CarModel

@receiver(post_save, sender=Car)
def add_manufacturer(sender, instance, **kwargs):
    if len(CarManufacturer.objects.filter(manufacturer=instance.manufacturer)) != 0:
        cars_with_existing_manufacturer = Car.objects.filter(manufacturer=instance.manufacturer)
        print(instance.manufacturer)
        model_exists = False
        for car in cars_with_existing_manufacturer:
            if car.model == sender.model:
                model_exists = True
            else:
                pass
        if not model_exists:
            manufacturer = CarManufacturer.objects.get(manufacturer=instance.manufacturer)
            new_model = CarModel.objects.create(manufacturer_id=manufacturer, model=instance.model)
            new_model.save()

    else:
        print("Ozon")
        new_manufacturer = CarManufacturer.objects.create(manufacturer=instance.manufacturer)
        new_manufacturer.save()
        new_model = CarModel.objects.create(manufacturer_id=new_manufacturer, model=instance.model)
        new_model.save()