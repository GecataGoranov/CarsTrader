from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import TraderUserManager
from django.utils.text import slugify

# Create your models here.
class TraderUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    
    USERNAME_FIELD = "email"

    objects = TraderUserManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.email)
        return super().save(*args, **kwargs)
