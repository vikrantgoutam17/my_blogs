# Generated by Django 2.2.1 on 2019-06-01 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20190601_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 15, 51, 23, 64935), verbose_name='date published'),
        ),
    ]
