# Generated by Django 4.2.4 on 2023-09-07 13:04

import ShoppingCartApp.context_processor
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingCartApp', '0002_alter_elements_options_alter_elements_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
