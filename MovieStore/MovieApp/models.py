from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    image = models.ImageField()

class Message(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField(max_length=255)
     