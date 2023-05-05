# Generated by Django 4.2 on 2023-04-30 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0013_remove_car_picture_carpictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpictures',
            name='car_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='trader.car'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carpictures',
            name='picture',
            field=models.ImageField(upload_to='car_images'),
        ),
    ]