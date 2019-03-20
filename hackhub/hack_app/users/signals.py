from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Progress

#when a user is saved send the post_save signal received by this function (receiver)
#the fun arguments are passed by post_save signal
#kwargs accepts any additional keyword arguments
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    #if user was created
    if created:
        #create a Profile project with the user = the instance of user created
        Profile.objects.create(user=instance)
        Progress.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.progress.save()
