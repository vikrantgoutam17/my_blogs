# Generated by Django 2.2.1 on 2019-06-03 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0041_auto_20190603_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 3, 14, 52, 44, 208324), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]