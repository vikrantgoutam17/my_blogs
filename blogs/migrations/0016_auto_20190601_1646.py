# Generated by Django 2.2.1 on 2019-06-01 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_auto_20190601_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 16, 46, 12, 868660), verbose_name='date published'),
        ),
    ]
