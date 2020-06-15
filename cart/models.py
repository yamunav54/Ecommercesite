from django.db import models

# Create your models here.

def directory():
    return 'uploads/% Y/% M/% D'


class Product(models.Model):
    title = models.TextField(max_length=200)
    price=models.TextField()
    summary=models.TextField(default="This is a new product")
    image=models.ImageField(upload_to='uploads/',default='uploads/')



