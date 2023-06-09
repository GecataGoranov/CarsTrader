# Generated by Django 4.2 on 2023-06-14 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trader', '0005_rename_manufacturer_id_carmodel_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='users_who_favourited_car',
            field=models.ManyToManyField(related_name='potential_buyers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='car',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carpictures',
            name='car_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.car'),
        ),
    ]
