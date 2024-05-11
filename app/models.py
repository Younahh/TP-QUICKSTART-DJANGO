from django.contrib.auth.models import AbstractUser
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    description2 = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
