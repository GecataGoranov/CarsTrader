# Generated by Django 4.2 on 2023-04-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0014_carpictures_car_id_alter_carpictures_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carpictures',
            name='car_id',
        ),
        migrations.AddField(
            model_name='car',
            name='pictures',
            field=models.ManyToManyField(to='trader.carpictures'),
        ),
    ]