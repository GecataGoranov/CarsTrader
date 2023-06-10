from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Car

@receiver(post_save, sender=Car)
def add_manufacturer(sender, **kwargs):
    if Car.objects.filter(manufacturer=sender.manufacturer):
        pass
    else:
        ...