# Generated by Django 4.2 on 2023-04-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0005_alter_car_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('W', 'White'), ('B', 'Black'), ('G', 'Gray'), ('S', 'Silver'), ('U', 'Blue'), ('R', 'Red'), ('N', 'Brown'), ('G', 'Green'), ('O', 'Orange'), ('L', 'Gold'), ('Y', 'Yellow'), ('P', 'Purple')], max_length=1),
        ),
    ]
