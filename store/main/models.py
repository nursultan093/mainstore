from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='default-slug')

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='default-slug')
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
