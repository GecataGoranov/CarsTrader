# Generated by Django 4.2 on 2023-06-07 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_user_id_traderprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traderprofile',
            name='additional_info',
        ),
    ]