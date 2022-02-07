from django.db.models.signals import post_save
# Sender
from django.contrib.auth.models import User
from django.dispatch import receiver
from. models import Profile

@receiver(post_save,sender=User)
def create_Profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_Profile(sender,instance,**kwargs):
    instance.profile.save()
