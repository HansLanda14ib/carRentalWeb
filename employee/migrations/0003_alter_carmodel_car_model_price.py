# Generated by Django 4.2 on 2023-05-03 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carmodel",
            name="car_model_price",
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
