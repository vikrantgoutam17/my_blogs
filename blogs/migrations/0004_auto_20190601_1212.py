# Generated by Django 2.2.1 on 2019-06-01 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20190530_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 12, 12, 38, 707248), verbose_name='date published'),
        ),
    ]
