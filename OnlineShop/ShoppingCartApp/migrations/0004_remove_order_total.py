# Generated by Django 4.2.4 on 2023-09-07 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingCartApp', '0003_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]
