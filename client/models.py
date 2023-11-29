from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Client


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_vip = models.BooleanField(default=False)


# @receiver(post_save, sender=Client)
# def create_custom_user(sender, instance, created, **kwargs):
#     if created:
#         # Создаем CustomUser при создании Client
#         user = settings.AUTH_USER_MODEL.objects.create(
#             username=f"customuser_{instance.id}")  # Подставьте нужные атрибуты CustomUser
#         instance.user = user
#         instance.save()


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()