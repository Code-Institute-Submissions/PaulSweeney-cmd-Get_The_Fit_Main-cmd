# Generated by Django 3.2.7 on 2021-10-20 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_checkout', '0005_alter_orderitem_item_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='item_total',
            new_name='lineitem_total',
        ),
    ]
