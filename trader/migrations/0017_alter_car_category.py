# Generated by Django 4.2 on 2023-05-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0016_remove_car_pictures_carpictures_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('VAN', 'Van'), ('SUV', 'SUV'), ('CAB', 'Cabrio'), ('UNI', 'Station Wagon'), ('COU', 'Coupe'), ('MIN', 'Minivan'), ('PIC', 'Pickup'), ('SED', 'Sedan'), ('LIM', 'Limousine'), ('HAT', 'Hatchback')], max_length=3),
        ),
    ]
