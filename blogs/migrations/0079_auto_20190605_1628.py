# Generated by Django 2.2.1 on 2019-06-05 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0078_auto_20190605_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 5, 16, 28, 44, 47865)),
        ),
    ]
