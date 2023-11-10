from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from .models import OlaroomProfile, Olaroom, RealtorProfile, Realtor

'''@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(
            user=instance
        )'''

@receiver(post_save, sender=Olaroom)
def create_profile(sender, instance, created, **kwargs):
    if created:
        OlaroomProfile.objects.create(
            user=instance
        )

@receiver(post_save, sender=Realtor)
def create_profile_for_realtor(sender, instance, created, **kwargs):
    if created:
        RealtorProfile.objects.create(
            user=instance
        )