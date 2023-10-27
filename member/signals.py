from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        user_profile = Profile.objects.create(
            user=user,
            email=user.email,
            last_name=user.last_name,
            first_name=user.first_name,
            username=user.username
        )
        user_profile.follow.set([instance.profile.id])


@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()


