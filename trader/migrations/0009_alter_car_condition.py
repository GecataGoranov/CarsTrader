# Generated by Django 4.2 on 2023-04-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0008_alter_car_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(blank=True, choices=[('N', 'New'), ('U', 'Used'), ('F', 'For parts')], default='U', max_length=1, null=True),
        ),
    ]