# Generated by Django 4.2.4 on 2023-09-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingCartApp', '0004_remove_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
