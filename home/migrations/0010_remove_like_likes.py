# Generated by Django 3.0.8 on 2020-08-21 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likes',
        ),
    ]
