# Generated by Django 4.2 on 2023-06-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traderuser',
            name='slug',
            field=models.SlugField(default=None, unique=True),
            preserve_default=False,
        ),
    ]
