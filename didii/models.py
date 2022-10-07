from django.db import models

# Create your models here.
class House(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    
class House_1(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)