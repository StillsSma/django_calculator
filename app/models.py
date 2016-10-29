from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


ACCESS_LEVELS = [
        ('o', 'owner'),
        ('u', 'user'),

]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=10, choices=ACCESS_LEVELS)

    def __str__(self):
        return str(self.user)

    @property
    def is_owner(self):
        return self.access_level == 'o'
    @property
    def is_user(self):
        return self.access_level == 'u'

    @receiver(post_save, sender='auth.user')
    def create_profile(sender, **kwargs):
        instance = kwargs["instance"]
        created = kwargs["created"]
        if created:
            Profile.objects.create(user=instance)

class Operation(models.Model):
    user = models.ForeignKey('auth.User')
    num1 = models.FloatField()
    num2= models.FloatField()
    operator = models.CharField(max_length=1)
    timestamp = models.DateTimeField(auto_now_add=True)
