# Generated by Django 4.2.2 on 2023-06-22 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities_main', '0002_rename_trains_train'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Train',
            new_name='City',
        ),
    ]
