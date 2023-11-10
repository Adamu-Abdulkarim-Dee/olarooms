from .models import Invitation, Notification
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
import random
import string
from django.conf import settings
from django.shortcuts import render, get_object_or_404


def generate_random_number():
    # we should change the 123 inside start number veriable, 
    # by doing so, we are safe to create multiple
    # random number for that field
    start_number = 'OlaRooms:123:' + ''.join(random.choices(string.digits, k=10))
    return start_number

@receiver(post_save, sender=Invitation)
def notification_signals(sender, instance, created, **kwargs):
    message = f"{instance.first_name} {instance.last_name} booked our {instance.room_type.room_type} room for {instance.number_of_day} day"
    link = reverse('Invitation_Information', args=[str(instance.slug)])
    invitation = get_object_or_404(Invitation, slug=instance.slug)
    room_id_number = generate_random_number()
    notification = Notification.objects.create(
        user=instance.room_type.user, message=message, link=link,
        room_id_number=room_id_number
    )
    notification.save()