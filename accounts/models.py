from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import TraderUserManager
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator


phone_regex = r'^0[0-9]{9}$'
phone_validator = RegexValidator(
    regex=phone_regex,
    message="Phone numbers must start with 0 and have 10 digits."
)

# Create your models here.
class TraderUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = "email"

    objects = TraderUserManager()


class TraderProfile(models.Model):
    user = models.OneToOneField(TraderUser, on_delete=models.CASCADE, primary_key=True)
    slug = models.SlugField(unique=True)
    profile_picture = models.ImageField(upload_to="profile_pics")
    phone_number = models.CharField(max_length=10, validators=[phone_validator], blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    place_of_living = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.email)
        return super().save(*args, **kwargs)