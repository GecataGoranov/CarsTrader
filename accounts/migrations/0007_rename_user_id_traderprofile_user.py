# Generated by Django 4.2 on 2023-06-07 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_traderprofile_first_name_traderprofile_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traderprofile',
            old_name='user_id',
            new_name='user',
        ),
    ]
