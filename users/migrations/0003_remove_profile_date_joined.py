# Generated by Django 4.2.1 on 2023-05-24 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bio_profile_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_joined',
        ),
    ]
