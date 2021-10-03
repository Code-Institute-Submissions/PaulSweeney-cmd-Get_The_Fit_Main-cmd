from django.db import models
from decimal import Decimal


class Category(models.Model):
    name = models.CharField(max_length=300)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=25, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    detail_01 = models.CharField(max_length=100, default='some detail')
    detail_02 = models.CharField(max_length=100, default='some detail')
    detail_03 = models.CharField(max_length=100, default='some detail')
    old_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=Decimal('0.00'))
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name