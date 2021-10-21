import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=30, null=False, editable=False)
    first_name = models.CharField(max_length=40, null=False, blank=False)
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
    delivery_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
        )
    bag_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )

    # a function to generate an order number using uuid
    def _generate_order_number(self):

        return uuid.uuid4().hex.upper()

    # updates grand total when new item is added
    def update_total(self):
        self.bag_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.bag_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_total = self.bag_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_total = 0
        self.grand_total = self.bag_total + self.delivery_total
        self.save()

    # a default function incase the original order number hasnt been generated
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=15, null=True, blank=True)
    item_quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False, editable=False)

    # a default function to set line item total and update order total
    def save(self, *args, **kwargs):

        self.lineitem_total = self.product.price * self.item_quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'sku: {self.product.sku} on following order: {self.order.order_number}'
