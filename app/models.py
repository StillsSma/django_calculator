from django.db import models

# Create your models here.

class Calculator(models.Model):
    num1 = models.CharField(max_length=20)
    num2 = models.CharField(max_length=20)
