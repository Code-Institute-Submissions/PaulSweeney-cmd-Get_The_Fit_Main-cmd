from django.db import models


class Order(models.Model):
    first_name = models.Charfield(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)
    email_address = models.EmailField(max_length=300, null=False, blank=False)
    phone_number = models.CharField(max_length=25, null=False, blank=False)
    address1 = models.CharField(max_length=100, null=False, blank=False)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    town_or_city = models.CharField(max_length=30, null=False, blank=False)
    county = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    delivery_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    bag_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)



