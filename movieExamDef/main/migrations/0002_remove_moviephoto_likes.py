# Generated by Django 4.0.3 on 2022-04-14 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviephoto',
            name='likes',
        ),
    ]
