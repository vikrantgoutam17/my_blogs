# Generated by Django 2.2.1 on 2019-06-03 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0045_auto_20190603_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 3, 21, 8, 43, 719788), verbose_name='date published'),
        ),
    ]
