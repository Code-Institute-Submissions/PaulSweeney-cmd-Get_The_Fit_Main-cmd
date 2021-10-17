from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItem


# handling signals from the post_save event
@receiver(post_save, sender=OrderItem)
def update_when_saved(sender, instance, created, **kwargs):

    # updating order total on lineitem create
    instance.order.update_total()


# handling signals from the post_delete event
@receiver(post_delete, sender=OrderItem)
def update_when_deleted(sender, instance, **kwargs):

    # updating order total on line item delete
    instance.order.update_total()
