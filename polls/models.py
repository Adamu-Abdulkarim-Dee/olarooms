from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.utils.text import slugify
from django.conf import settings
from .choices import *

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        REALTOR = "REALTOR", 'Realtor'
        OLAROOM = "OLAROOM", 'Olaroom'
    
    base_role = Role.ADMIN

    role = models.CharField(max_length=225, choices=Role.choices)
    username = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.username)


class OlaroomsManger(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.OLAROOM)

class Olaroom(User):
    base_role = User.Role.OLAROOM

    company_name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=15, unique=True)
    country = models.CharField(max_length=225, choices=COUNTRIES)

    olaroom = OlaroomsManger()

    def welcome(self):
        return "Only for Olaroom"

class RealtorManger(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.REALTOR)

class RealtorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Realtor(User):

    base_role = User.Role.REALTOR
    address = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=15, unique=True)
    country = models.CharField(max_length=225, choices=COUNTRIES)
    state = models.CharField(max_length=225)

    realtor = RealtorManger()

    def welcome(self):
        return "Only for Realtor"

class OlaroomProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    about = models.TextField()
    thumbnails = models.ImageField(upload_to='thumbnails')
    country = models.CharField(max_length=225, choices=COUNTRIES)
    twitter = models.URLField(unique=True)
    website = models.URLField(unique=True)
