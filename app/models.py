from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


ACCESS_LEVELS = [
        ('u1', 'user1'),
        ('u2', 'user2'),

]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=10, choices=ACCESS_LEVELS)

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender='auth.user')
    def create_profile(sender, **kwargs):
        instance = kwargs["instance"]
        created = kwargs["created"]
        if created:
            Profile.objects.create(user=instance)
