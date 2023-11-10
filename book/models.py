from django.db import models
from .choices import *
from django.conf import settings
import random
import string

def generate_random_number_for_slug():
    # we should change the 123 inside start number veriable, 
    # by doing so, we are safe to create multiple
    # random number for that field
    start_number = 'OlaRooms-123-' + ''.join(random.choices(string.digits, k=10))
    return start_number

def generate_random_number():
    # we should change the 123 inside start number veriable, 
    # by doing so, we are safe to create multiple
    # random number for that field
    start_number = 'OlaRooms-123' + ''.join(random.choices(string.digits, k=10))
    return start_number

class Room(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=225, choices=ROOM_TYPE)
    price = models.BigIntegerField()
    currency = models.CharField(max_length=255, choices=CURRENCY_TYPE)
    country = models.CharField(max_length=200, choices=COUNTRIES)
    state = models.CharField(max_length=300)
    town = models.CharField(max_length=225)
    is_available = models.BooleanField(default=True)
    address = models.CharField(max_length=200)
    description = models.TextField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()

    slug = models.SlugField(unique=True, default=generate_random_number_for_slug)

    def __str__(self):
        return str(self.room_name)

class Invitation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    state = models.CharField(max_length=225)
    town = models.CharField(max_length=225)
    address = models.CharField(max_length=250)
    id_type = models.CharField(max_length=225, choices=ID_TYPE)
    id_number = models.CharField(max_length=20)
    occupation = models.CharField(max_length=200, choices=OCCUPATION)
    number_of_day = models.IntegerField()
    visited_for = models.CharField(max_length=200, choices=VISITED_FOR)
    room_type = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, default=generate_random_number)

    def __str__(self):
        return str(self.first_name)

class House(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house_type = models.CharField(max_length=225, choices=HOUSE_TYPE)
    currency = models.CharField(max_length=100, choices=CURRENCY_TYPE)
    price = models.BigIntegerField()
    country = models.CharField(max_length=225, choices=COUNTRIES)  
    state = models.CharField(max_length=225)
    house_address = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=15)
    town = models.CharField(max_length=225)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()
    image_5 = models.ImageField()

    slug = models.SlugField(unique=True, default=generate_random_number_for_slug)
    def __str__(self):
        return self.user

class Land(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    currency = models.CharField(max_length=100, choices=CURRENCY_TYPE)
    price = models.BigIntegerField()
    country = models.CharField(max_length=225, choices=COUNTRIES)
    state = models.CharField(max_length=225)
    town = models.CharField(max_length=225)
    land_address = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=15)
    land_type = models.CharField(max_length=100, choices=LAND_TYPE)

    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, default=generate_random_number_for_slug)

    def __str__(self):
        return str(self.user)

class LocalRoom(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=225, choices=ROOM_TYPE)
    currency = models.CharField(max_length=100, choices=CURRENCY_TYPE)
    price = models.BigIntegerField()
    country = models.CharField(max_length=225, choices=COUNTRIES)
    state = models.CharField(max_length=225)
    town = models.CharField(max_length=225)
    room_address = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=15)

    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()
    image_5 = models.ImageField()
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, default=generate_random_number)

    def __str__(self):
        return str(self.user)

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    message = models.TextField()
    link = models.URLField()
    room_id_number = models.CharField(max_length=225, unique=True)

    def __str__(self):
        return str(self.message)