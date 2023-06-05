# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import TraderProfile, TraderUser
# from django.utils.text import slugify


# @receiver(post_save ,sender=TraderUser)
# def create_trader_profile(sender, instance, created, **kwargs):
#     if created:
#         TraderProfile.objects.create(user_id=instance, slug=slugify(instance.email))