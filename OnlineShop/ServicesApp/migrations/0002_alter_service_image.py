# Generated by Django 4.2.4 on 2023-08-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServicesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='ServicesApp'),
        ),
    ]