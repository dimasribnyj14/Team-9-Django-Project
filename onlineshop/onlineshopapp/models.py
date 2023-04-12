from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    category = models.ForeignKey("Category", on_delete = models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()


class Message(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField(max_length=255)