from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #overrides save method of model
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Progress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ch1ex1 = models.BooleanField(default=False)
    ch1ex2 = models.BooleanField(default=False)
    ch1ex3 = models.BooleanField(default=False)
    ch2ex1 = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Progress'

    def save(self, *args, **kwargs):
        super(Progress, self).save(*args, **kwargs)
