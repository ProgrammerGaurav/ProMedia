# Generated by Django 3.0.8 on 2020-08-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200820_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='connection',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
