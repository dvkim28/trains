# Generated by Django 4.2.2 on 2023-06-22 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities_main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trains',
            new_name='Train',
        ),
    ]