# Generated by Django 2.2.1 on 2019-06-04 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0058_auto_20190604_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 4, 12, 30, 59, 140336)),
        ),
    ]