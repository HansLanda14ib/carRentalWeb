# Generated by Django 4.2 on 2023-05-03 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0003_alter_carmodel_car_model_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carmodel",
            name="car_model_price",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="rental",
            name="rental_price",
            field=models.FloatField(),
        ),
    ]
